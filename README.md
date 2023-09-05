## Audio Source Separation and Emotion+Text Transcription

This project is designed to take audio input with multiple speakers and perform the following tasks:

1. **Audio Source Separation:** Separating the input audio into multiple sources, with each source corresponding to one speaker in the recording.

2. **Emotion and Text Transcription:** Processing each audio source separately to transcribe the speech content and generate an emotion embedding vector for each utterance.

The project utilizes two distinct models:

1. **Speaker Separation Model:** This model is responsible for separating audio sources and isolating the speech of individual speakers.

2. **Speech-to-Emotion (S2(E&T)) Model:** This model takes the separated audio from each speaker and transcribes the speech while also producing emotion embedding vectors to capture the emotional content of the utterances.

### How It Works

1. Input Audio: Provide an audio file with multiple speakers speaking simultaneously.

2. Speaker Separation: The project uses a dedicated model to separate the audio into individual speaker sources. Each source corresponds to a single speaker's voice.

3. Speech-to-Emotion Processing: After separation, each speaker's audio is processed by the S2E model. This model transcribes the speech content and generates emotion embedding vectors, which represent the emotional aspects of what is being said.

4. Emotion Analysis: The emotion embedding vectors can be used for various downstream tasks, such as sentiment analysis, emotion recognition, or other applications that require understanding the emotional context of the speech.

### Project Structure

- `data/`: Store input audio files and any necessary data.
- `models/`: Contains the trained models for speaker separation and emotion transcription.
- `src/`: Source code for the project.
  - `speaker_separation.py`: Code for separating audio sources.
  - `emotion_transcription.py`: Code for transcribing speech and generating emotion embedding vectors.
- `requirements.txt`: List of dependencies required to run the project.
- `README.md`: This file, which provides an overview of the project.

### Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```
2. Install Dependencies: Use pip to install the required dependencies listed in the requirements.txt file:

   ```bash
   pip install -r requirements.txt
   ```

3. Prepare Input Audio: Place your input audio file in the data/ directory.

4. Run the Project: Execute the project's main script, specifying the input audio file as follows:

    ```bash

python src/main.py --input_audio data/input_audio.wav

    ```

These steps will initiate the audio source separation and emotion/text transcription processes.

## To-Do List

Here is a list of tasks and milestones to guide the development and improvement of the project:

- [ ] **Implement the Speaker Separation Model:** Develop the model responsible for separating audio sources into individual speakers.

- [ ] **Train and Fine-Tune the S2(E&T) Model:** Train the Speech-to-Emotion (S2E) Model to transcribe speech and generate emotion embedding vectors. Fine-tune the model for optimal performance.

- [ ] **Create a User-Friendly CLI:** Develop a user-friendly command-line interface (CLI) that simplifies the process of using the project for audio source separation and emotion transcription.

- [ ] **Add Unit Tests:** Implement unit tests to ensure the reliability and correctness of the codebase.

- [ ] **Provide a Comprehensive User Guide:** Create an extensive user guide that explains how to use the project, showcases examples, and offers guidance on interpreting emotion embedding vectors.

