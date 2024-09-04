# Indian Sign Language Recognition Project

This project is an Indian Sign Language (ISL) recognition system that converts hand signs into text. It includes custom-made videos to train the model, ensuring high quality and consistency in sign recognition. The project aims to address the lack of comprehensive and high-quality datasets for ISL available online.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [Credits](#credits)

## Project Overview

This project is designed to recognize Indian Sign Language gestures and convert them into corresponding text. It utilizes Python libraries such as OpenCV for video processing, SpeechRecognition for capturing audio, and Google Translate API for language detection and translation. The custom video dataset created for this project ensures high accuracy in recognizing ISL signs.

## Features
- **Speech Recognition:** Captures and processes spoken words.
- **Language Detection & Translation:** Automatically detects the language and translates non-English text to English.
- **Sign Language to Text Conversion:** Converts ISL gestures captured in videos into text.
- **Video Segmentation:** Breaks down sign language videos into manageable parts for processing.

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/vaibhavkothari33/speech_to_handsign.git
    ```

2. **Install Required Dependencies:**
    You can install all required dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Project:**
    To run the main application:
    ```bash
    python main.py
    ```

## Usage

### Speech to Text Conversion
1. Run the `main.py` file.
2. Speak into your microphone, and the application will recognize the speech, detect the language, translate it if necessary, and process the text.
3. The processed text will be used to retrieve and play relevant videos corresponding to the recognized words.

### Uploading and Processing Custom Videos
1. Prepare your video in Indian Sign Language.
2. Upload the video using the frontend interface (or place it in the appropriate directory for testing).
3. The video will be automatically processed, segmented, and translated into text.

## How It Works

- **Speech Recognition:** Captures audio input and converts it into text using Google’s Speech Recognition API.
- **Language Detection & Translation:** The text is analyzed to detect its language. If the detected language is not English, it is translated to English using the Google Translate API.
- **Video Mapping:** The recognized words are mapped to corresponding videos representing ISL gestures. These videos are then played in sequence.

## Project Structure

- `main.py`: The main script for running the speech recognition and video mapping.
- `video_mapping.py`: Contains functions for mapping recognized text to videos.
- `videos/`: Directory containing ISL videos.
- `requirements.txt`: Contains the list of dependencies required for the project.

## Requirements

The project requires the following Python libraries:

- `opencv-python`
- `speechrecognition`
- `pyaudio`
- `googletrans==4.0.0-rc1`
- `numpy`

Install all dependencies using:
```bash
pip install -r requirements.txt
```
## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## Credits
This project was developed by Vaibhav Kothari. The custom video dataset and implementation were created me to ensure high-quality recognition of Indian Sign Language.

Special thanks to all contributors and open-source projects that made this possible.