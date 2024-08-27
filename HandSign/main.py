# import speech_recognition as sr
# from googletrans import Translator
# from video_mapping import get_video_path
# from video_player import play_video

# def recognize_speech_from_mic():
#     recognizer = sr.Recognizer()
#     mic = sr.Microphone()

#     with mic as source:
#         print("Adjusting for ambient noise... Please wait.")
#         recognizer.adjust_for_ambient_noise(source)
#         print("Listening...")
#         audio = recognizer.listen(source)

#     try:
#         print("Recognizing...")
#         text = recognizer.recognize_google(audio, language="hi-IN")  # Assuming you're speaking Hindi
#         print(f"Recognized text (Hindi): {text}")
#         return text
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand the audio.")
#         return ""
#     except sr.RequestError as e:
#         print(f"Could not request results from Google Speech Recognition service; {e}")
#         return ""

# def translate_text(text, target_language='en'):
#     translator = Translator()
#     translation = translator.translate(text, dest=target_language)
#     print(f"Translated text: {translation.text}")
#     return translation.text

# def main():
#     # Step 1: Recognize speech in Hindi
#     hindi_text = recognize_speech_from_mic()
#     if not hindi_text:
#         print("No text recognized. Exiting.")
#         return

#     # Step 2: Translate recognized Hindi text to English
#     english_text = translate_text(hindi_text, target_language='en')

#     # Step 3: Process the translated English text
#     words = english_text.split()
#     print(f"Processing words: {words}")  # Debug print to check the words

#     for word in words:
#         print(f"Looking for video for: {word}")  # Debug print to check which word is being processed
        
#         video_path = get_video_path(word)  # Get the path to the video for the current word
        
#         if video_path:
#             print(f"Playing video: {video_path}")  # Debug print to confirm the video path
#             play_video(video_path)  # Play the video
#         else:
#             print(f"No video found for: {word}")  # Debug print if no video is found

# if __name__ == "__main__":
#     main()


# the above modal uses the api method so it is working fine but takes 2 sec to start 
# the above modal uses the api method so it is working fine but takes 2 sec to start 
# the above modal uses the api method so it is working fine but takes 2 sec to start 
# the above modal uses the api method so it is working fine but takes 2 sec to start 
# the above modal uses the api method so it is working fine but takes 2 sec to start 


# import speech_recognition as sr
# from googletrans import Translator, LANGUAGES
# from video_mapping import get_video_path
# from video_player import play_video

# def recognize_speech_from_mic():
#     recognizer = sr.Recognizer()
#     mic = sr.Microphone()

#     with mic as source:
#         # print("Adjusting for ambient noise... Please wait.")
#         recognizer.adjust_for_ambient_noise(source)
#         print("Listening...")
#         audio = recognizer.listen(source)

#     try:
#         print("Recognizing speech...")
#         text = recognizer.recognize_google(audio)  # Broad language detection
#         print(f"Recognized text: {text}")
#         return text
#     except sr.UnknownValueError:
#         print("Could not understand the audio.")
#         return ""
#     except sr.RequestError as e:
#         print(f"Could not request results from the service; {e}")
#         return ""

# def detect_language(text):
#     translator = Translator()
#     detected = translator.detect(text)
#     print(f"Detected language: {LANGUAGES[detected.lang]}")
#     return detected.lang

# def translate_text(text, target_language='en'):
#     translator = Translator()
#     translation = translator.translate(text, dest=target_language)
#     print(f"Translated text: {translation.text}")
#     return translation.text

# def main():
#     # Step 1: Recognize speech
#     text = recognize_speech_from_mic()
#     if not text:
#         print("No text recognized. Exiting.")
#         return

#     # Step 2: Detect the language
#     language = detect_language(text)

#     # Step 3: If the language is not English, translate it to English
#     if language != 'en':
#         text = translate_text(text, target_language='en')

#     # Step 4: Process the translated or recognized English text
#     words = text.split()
#     print(f"Processing words: {words}")  # Debug print to check the words

#     for word in words:
#         # print(f"Looking for video for: {word}")  # Debug print to check which word is being processed
        
#         video_path = get_video_path(word)  # Get the path to the video for the current word
        
#         if video_path:
#             # print(f"Playing video: {video_path}")  # Debug print to confirm the video path
#             play_video(video_path)  # Play the video
#         else:
#             print(f"No video found for: {word}")  # Debug print if no video is found

# if __name__ == "__main__":
#     main()
    
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from video_mapping import get_video_path
import cv2  # OpenCV library to play videos

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print(f"Recognized text: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from the service; {e}")
        return ""

def detect_language(text):
    translator = Translator()
    detected = translator.detect(text)
    print(f"Detected language: {LANGUAGES[detected.lang]}")
    return detected.lang

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"Translated text: {translation.text}")
    return translation.text

def play_videos_in_sequence(video_paths):
    """Play a sequence of videos in the same OpenCV window."""
    for video_path in video_paths:
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print(f"Error opening video file {video_path}")
            continue
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow('Video', frame)

            # Exit if 'q' is pressed
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        
        cap.release()

    cv2.destroyAllWindows()

def main():
    # Step 1: Recognize speech
    text = recognize_speech_from_mic()
    if not text:
        print("No text recognized. Exiting.")
        return

    # Step 2: Detect the language
    language = detect_language(text)

    # Step 3: If the language is not English, translate it to English
    if language != 'en':
        text = translate_text(text, target_language='en')

    # Step 4: Process the translated or recognized English text
    words = text.split()
    print(f"Processing words: {words}")

    video_paths = []

    for word in words:
        video_path = get_video_path(word)
        
        if video_path:
            video_paths.append(video_path)
        else:
            print(f"No video found for: {word}")

    if video_paths:
        play_videos_in_sequence(video_paths)

if __name__ == "__main__":
    main()

    
    
# the above modal uses the api method so it is working fine but takes 2 sec to start 
# the above modal uses the api method so it is working fine but takes 2 sec to start 
# the above modal uses the api method so it is working fine but takes 2 sec to start 
# the above modal uses the api method so it is working fine but takes 2 sec to start 
# the above modal uses the api method so it is working fine but takes 2 sec to start 



# import vosk
# import sys
# import wave
# import json
# import os
# from transformers import MarianMTModel, MarianTokenizer
# from video_mapping import get_video_path
# from video_player import play_video
# import threading

# # Initialize Vosk for speech recognition
# model = vosk.Model("model")  # Download the Vosk model and place it in the "model" directory
# recognizer = vosk.KaldiRecognizer(model, 16000)

# # Initialize MarianMT for translation
# model_name = 'Helsinki-NLP/opus-mt-hi-en'  # For Hindi to English
# tokenizer = MarianTokenizer.from_pretrained(model_name)
# translator = MarianMTModel.from_pretrained(model_name)

# def recognize_speech_from_mic():
#     # Capture audio from the microphone
#     wf = wave.open(sys.stdin.buffer, "rb")
#     while True:
#         data = wf.readframes(4000)
#         if len(data) == 0:
#             break
#         if recognizer.AcceptWaveform(data):
#             result = recognizer.Result()
#             text = json.loads(result)["text"]
#             print(f"Recognized text: {text}")
#             return text

# def translate_text(text, target_language='en'):
#     # Translate text using MarianMT
#     translated = translator.generate(**tokenizer.prepare_seq2seq_batch([text], return_tensors="pt"))
#     translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
#     print(f"Translated text: {translated_text}")
#     return translated_text

# def process_and_play_videos(text):
#     # Split the text into words and play corresponding videos
#     words = text.split()
#     print(f"Processing words: {words}")

#     for word in words:
#         print(f"Looking for video for: {word}")
#         video_path = get_video_path(word)
#         if video_path:
#             print(f"Playing video: {video_path}")
#             play_video(video_path)
#         else:
#             print(f"No video found for: {word}")

# def main():
#     # Recognize speech in real-time using Vosk
#     text = recognize_speech_from_mic()

#     # Translate if necessary
#     language = detect_language(text)  # Implement this function or assume Hindi input
#     if language != 'en':
#         text = translate_text(text)

#     # Process the translated text and play videos
#     process_and_play_videos(text)

# if __name__ == "__main__":
#     main()

# import vosk
# import sys
# import wave
# import json
# import os
# from transformers import MarianMTModel, MarianTokenizer
# from video_mapping import get_video_path
# from video_player import play_video
# from langdetect import detect

# # Initialize Vosk for speech recognition
# model = vosk.Model("model")  # Download the Vosk model and place it in the "model" directory
# recognizer = vosk.KaldiRecognizer(model, 16000)

# # Initialize MarianMT for translation
# model_name = 'Helsinki-NLP/opus-mt-hi-en'  # For Hindi to English
# tokenizer = MarianTokenizer.from_pretrained(model_name)
# translator = MarianMTModel.from_pretrained(model_name)

# def recognize_speech_from_mic():
#     # Capture audio from the microphone
#     wf = wave.open(sys.stdin.buffer, "rb")
#     while True:
#         data = wf.readframes(4000)
#         if len(data) == 0:
#             break
#         if recognizer.AcceptWaveform(data):
#             result = recognizer.Result()
#             text = json.loads(result)["text"]
#             print(f"Recognized text: {text}")
#             return text

# def translate_text(text, target_language='en'):
#     # Translate text using MarianMT
#     translated = translator.generate(**tokenizer.prepare_seq2seq_batch([text], return_tensors="pt"))
#     translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
#     print(f"Translated text: {translated_text}")
#     return translated_text

# def detect_language(text):
#     try:
#         # Detect the language of the text
#         language = detect(text)
#         print(f"Detected language: {language}")
#         return language
#     except Exception as e:
#         print(f"Could not detect language: {e}")
#         return None

# def process_and_play_videos(text):
#     # Split the text into words and play corresponding videos
#     words = text.split()
#     print(f"Processing words: {words}")

#     for word in words:
#         print(f"Looking for video for: {word}")
#         video_path = get_video_path(word)
#         if video_path:
#             print(f"Playing video: {video_path}")
#             play_video(video_path)
#         else:
#             print(f"No video found for: {word}")

# def main():
#     # Recognize speech in real-time using Vosk
#     text = recognize_speech_from_mic()

#     # Detect the language of the recognized text
#     language = detect_language(text)

#     # Translate if necessary
#     if language != 'en':
#         text = translate_text(text)

#     # Process the translated text and play videos
#     process_and_play_videos(text)

# if __name__ == "__main__":
#     main()
