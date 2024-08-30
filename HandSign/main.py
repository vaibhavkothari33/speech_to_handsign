import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from video_mapping import get_video_path
import cv2

def recognize_speech_from_mic(recognizer, mic):
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
    # Play a sequence of videos in a resized OpenCV window.
    for video_path in video_paths:
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print(f"Error opening video file {video_path}")
            continue
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Resize the frame
            frame = cv2.resize(frame, (940, 540))  # Resize
            
            cv2.imshow('Video', frame)

            # Exit if 'q' is pressed
            if cv2.waitKey(int(25 / 1.5)) & 0xFF == ord('q'):  # 1.5x speed
                cap.release()
                cv2.destroyAllWindows()
                return  # Exit function if 'q' is pressed
        
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
        
        # Step 2: Detect the language
        language = detect_language(text)

        # Step 3: If the language is not English, translate it to English
        if language != 'en':
            text = translate_text(text, target_language='en')

        # Check for stop command
        if 'stop' or 'terminate'  in text.lower():
            print("Stop command received. Exiting.")
            break

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
