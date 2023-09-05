from transformers.file_utils import ModelOutput
import torch.nn as nn
from transformers.models.wav2vec2.modeling_wav2vec2 import (
    Wav2Vec2PreTrainedModel,
    Wav2Vec2Model,
    Wav2Vec2FeatureProjection
)
from dataclasses import dataclass
import torch


@dataclass
class SpeechClassifierOutput(ModelOutput):

    logits: torch.FloatTensor = None



class Wav2vec2RegressionHead(nn.Module):
  """Head for Wav2vec2 regression task."""

  def __init__(self, config):
      super().__init__()
      self.dense = nn.Linear(config.hidden_size, config.hidden_size)
      self.dropout = nn.Dropout(config.final_dropout)
      self.out_proj = nn.Linear(config.hidden_size, config.num_labels)
      self.config = config


  def forward(self, features, **kwargs):
      x = features
      x = self.dropout(x)
      x = self.dense(x)
      x = self.dropout(x)
      x = self.out_proj(x)
      return x
    
class Wav2vec2Regression(Wav2Vec2PreTrainedModel):
    def __init__(self, config):
        super().__init__(config)
        
        self.num_labels = config.num_labels
        self.config = config
        self.wav2vec2 = Wav2Vec2Model(config)
        self.regression = Wav2vec2RegressionHead(config)
        self.feature_projection = Wav2Vec2FeatureProjection(config)
        if config.layers != None : 
            oldModuleList = self.wav2vec2.encoder.layers
            newModuleList = nn.ModuleList()

            for i in range(0, config.layers):
                newModuleList.append(oldModuleList[i])

            self.wav2vec2.encoder.layers = newModuleList

        self.init_weights()

    def freeze_feature_extractor(self):
        self.wav2vec2.feature_extractor._freeze_parameters()
    

    def merged_strategy(
            self,
            hidden_states,
            mode="mean"
    ):
        if mode == "mean":
            outputs = torch.mean(hidden_states, dim=1)
        elif mode == "sum":
            outputs = torch.sum(hidden_states, dim=1)
        elif mode == "max":
            outputs = torch.max(hidden_states, dim=1)[0]
        else:
            raise Exception(
                "The pooling method hasn't been defined! Your pooling mode must be one of these ['mean', 'sum', 'max']")

        return outputs

    def forward(
            self,
            input_values,
            attention_mask=None,
            output_attentions=None,
            output_hidden_states=None,
            return_dict=None,
            labels=None,
           
    ):

        outputs = self.wav2vec2(
            input_values,
            attention_mask=attention_mask,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )        


        hidden_states = outputs[0]
        hidden_states = self.merged_strategy(hidden_states, mode="mean")
        logits = self.regression(hidden_states)        


        return SpeechClassifierOutput(

            logits=logits,
        )