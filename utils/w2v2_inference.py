from models.w2v2 import Wav2vec2Regression
from transformers import AutoConfig
import torch 


HUGGING_FACE_MODEL_PATH = 'ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition'

class W2v2_Inference():
    
    def __init(self):  
        self.model_name_or_path = HUGGING_FACE_MODEL_PATH
        self.config = AutoConfig.from_pretrained(
                    self.model_name_or_path,
                    num_labels= 2,
                    problem_type="regression",
                    output_attention=False
                    )
        self.config.layers = 6
        self.model = Wav2vec2Regression.from_pretrained(self.model_name_or_path, config = self.config)
        
    def inference(self, input):
        self.model.eval()
        with torch.no_grad():
            output = self.model(input)
            return output