# GOSAI Voice Interaction Module

![GOSAI Logo](https://github.com/GOSAI-DVIC/gosai/raw/main/logo.png)

## Overview

The GOSAI Voice Interaction Module is an integral part of GOSAI, an operating system designed to simplify the creation of augmented reality applications. This module enables developers to incorporate advanced voice interaction capabilities into their augmented reality experiences. By combining three powerful models - a Speech-to-Text (STT) model, a speaker feature extraction model, and an emotion prediction model - this module can extract valuable insights from spoken language. It provides information on the emotion, transcription, and speaker identity associated with any speech input.

## Features

- **Speech-to-Text (STT) Conversion:** Transforms spoken language into text, enabling the system to work with the textual representation of speech.

- **Speaker Feature Extraction:** Identifies and extracts unique speaker characteristics, allowing for speaker identification and personalized interactions.

- **Emotion Prediction:** Analyzes speech to determine the emotional tone, providing valuable insights into the speaker's sentiment.

## Testing Without GOSAI

You can test the GOSAI Voice Interaction Module without integrating it into the GOSAI operating system. This allows you to quickly assess its functionality and capabilities. Follow these steps to get started:

1. **Clone This Repository:**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/electron260/MSERT.git
   ```

2. **Install Dependencies:**

   Install the dependencies required to run the module:

   ```bash
   pip install -r requirements.txt
   ```

3. **Test the Module:**

    Run the module to test its functionality:
  
    ```bash
    python main.py
    ```
  
    The module will prompt you to enter a path to an audio file. You can use the included sample audio file (`sample.wav`) to test the module. The module will then process the audio file and display the results.

4. **Customize and Experiment:**

  Feel free to customize the sample code and experiment with different speech inputs. You can also explore the module's capabilities by modifying the configuration and models as needed.


## TODO List

- [X] Implement the Emotion Prediction model and integrate it with the module.
- [X] Implement the Speaker Feature Extraction model and integrate it with the module.
- [ ] Implement the Speech-to-Text (STT) model and integrate it with the module.
- [ ] Convert all models to onnx format.
- [ ] Change some models if the inference time is too long.
- [ ] Create usage examples and tutorials.
- [ ] Conduct testing and gather user feedback.
- [ ] Explore potential integration with other GOSAI modules.



