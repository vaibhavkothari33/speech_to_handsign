import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from video_mapping import get_video_path
import cv2

# Dictionary to replace common abbreviations
abbreviation_corrections = {
    "r": "are",
    "u": "you",
    "pls": "please",
    "thx": "thank",
    "tala":"lock",
    "thank you":"thank",
    # Add more corrections as needed
}

def correct_abbreviations(text):
    words = text.split()
    corrected_words = [abbreviation_corrections.get(word.lower(), word) for word in words]
    corrected_text = " ".join(corrected_words)
    print(f"Corrected text: {corrected_text}")
    return corrected_text

def recognize_speech_from_mic(recognizer, mic):
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
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
    detected_language = detected.lang
    print(f"Detected language: {LANGUAGES[detected_language]}")
    return detected_language

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    translated_text = translation.text
    print(f"Translated text: {translated_text}")
    return translated_text

def play_videos_in_sequence(video_paths):
    for video_path in video_paths:
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print(f"Error opening video file {video_path}")
            continue
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, (640, 360))  # Smaller frame size for faster rendering
            cv2.imshow('Video', frame)

            if cv2.waitKey(10) & 0xFF == ord('q'):  # Faster playback
                cap.release()
                cv2.destroyAllWindows()
                return
        
        cap.release()
    
    cv2.destroyAllWindows()

def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    while True:
        # Step 1: Recognize speech
        text = recognize_speech_from_mic(recognizer, mic)
        if not text:
            continue
        
        # Step 2: Correct abbreviations
        text = correct_abbreviations(text)

        # Step 3: Detect the language
        language = detect_language(text)

        # Step 4: If the language is not English, translate it to English
        if language != 'en':
            text = translate_text(text, target_language='en')

        # Check for stop command
        if 'exit' in text.lower():
            print("Stop command received. Exiting.")
            break

        # Step 5: Process the translated or recognized English text
        words = text.split()
        print(f"Processing words: {words}")

        video_paths = [get_video_path(word) for word in words if get_video_path(word)]

        if video_paths:
            play_videos_in_sequence(video_paths)

if __name__ == "__main__":
    main()
