# import speech_recognition as sr
# from googletrans import Translator, LANGUAGES
# from video_mapping import get_video_path
# import cv2

# def recognize_speech_from_mic(recognizer, mic):
#     with mic as source:
#         recognizer.adjust_for_ambient_noise(source)
#         print("Listening...")
#         audio = recognizer.listen(source)

#     try:
#         # print("Recognizing speech...")
#         # text = "hello how are you"
#         text = recognizer.recognize_google(audio)
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

# def play_videos_in_sequence(video_paths):
#     # Play a sequence of videos in a resized OpenCV window.
#     for video_path in video_paths:
#         cap = cv2.VideoCapture(video_path)
        
#         if not cap.isOpened():
#             print(f"Error opening video file {video_path}")
#             continue
        
#         while cap.isOpened():
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             # Resize the frame
#             frame = cv2.resize(frame, (940, 540))  # Resize
            
#             cv2.imshow('Video', frame)

#             # Exit if 'q' is pressed
#             if cv2.waitKey(int(25 / 2.5)) & 0xFF == ord('q'):  # 1.5x speed
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 return  # Exit function if 'q' is pressed
        
#         cap.release()
    
#     cv2.destroyAllWindows()

# def main():
#     recognizer = sr.Recognizer()
#     mic = sr.Microphone()
    
#     while True:
#         # Step 1: Recognize speech
#         text = recognize_speech_from_mic(recognizer, mic)
#         if not text:
#             continue
        
#         # Step 2: Detect the language
#         language = detect_language(text)

#         # Step 3: If the language is not English, translate it to English
#         if language != 'en':
#             text = translate_text(text, target_language='en')

#         # Check for stop command
#         if 'exit' in text.lower():
#             print("Stop command received. Exiting.")
#             break

#         # Step 4: Process the translated or recognized English text
#         words = text.split()
#         print(f"Processing words: {words}")

#         video_paths = []
#         for word in words:
#             video_path = get_video_path(word)
            
#             if video_path:
#                 video_paths.append(video_path)
#             else:
#                 print(f"No video found for: {word}")

#         if video_paths:
#             play_videos_in_sequence(video_paths)

# if __name__ == "__main__":
#     main()

# import speech_recognition as sr
# from googletrans import Translator, LANGUAGES
# from video_mapping import get_video_path
# import cv2

# # Cache frequently used videos
# video_cache = {}

# def recognize_speech_from_mic(recognizer, mic):
#     with mic as source:
#         print("Listening...")
#         audio = recognizer.listen(source, timeout=2)  # Reduced timeout

#     try:
#         text = recognizer.recognize_google(audio)
#         print(f"Recognized text: {text}")
#         return text
#     except sr.UnknownValueError:
#         return ""
#     except sr.RequestError:
#         return ""

# def detect_language(text):
#     translator = Translator()
#     detected = translator.detect(text)
#     return detected.lang

# def translate_text(text, target_language='en'):
#     translator = Translator()
#     translation = translator.translate(text, dest=target_language)
#     return translation.text

# def get_cached_video(word):
#     if word in video_cache:
#         return video_cache[word]
#     else:
#         video_path = get_video_path(word)
#         if video_path:
#             video_cache[word] = video_path
#         return video_path

# def play_videos_in_sequence(video_paths):
#     for video_path in video_paths:
#         cap = cv2.VideoCapture(video_path)
        
#         if not cap.isOpened():
#             continue
        
#         while cap.isOpened():
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             # Resize the frame
#             frame = cv2.resize(frame, (940, 540))  # Smaller size
            
#             cv2.imshow('Video', frame)

#             # Exit if 'q' is pressed
#             if cv2.waitKey(int(25 / 2.5)) & 0xFF == ord('q'):  # 2.5x speed
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 return  # Exit function if 'q' is pressed
        
#         cap.release()
    
#     cv2.destroyAllWindows()

# def main():
#     recognizer = sr.Recognizer()
#     mic = sr.Microphone()
    
#     while True:
#         text = recognize_speech_from_mic(recognizer, mic)
#         if not text:
#             continue

#         language = detect_language(text)

#         if language != 'en':
#             text = translate_text(text, target_language='en')

#         if 'exit' in text.lower():
#             print("Stop command received. Exiting.")
#             break

#         words = text.split()

#         video_paths = []
#         for word in words:
#             video_path = get_cached_video(word)
#             if video_path:
#                 video_paths.append(video_path)

#         if video_paths:
#             play_videos_in_sequence(video_paths)

# if __name__ == "__main__":
#     main()




#gdsfyf huifhiudhgiuehgiuhdeighdughiruhbuhjhhgsvjhs iu fuih fih
#gdsfyf huifhiudhgiuehgiuhdeighdughiruhbuhjhhgsvjhs iu fuih fih
#gdsfyf huifhiudhgiuehgiuhdeighdughiruhbuhjhhgsvjhs iu fuih fih
#gdsfyf huifhiudhgiuehgiuhdeighdughiruhbuhjhhgsvjhs iu fuih fih
#gdsfyf huifhiudhgiuehgiuhdeighdughiruhbuhjhhgsvjhs iu fuih fihkdfnh 


# import speech_recognition as sr
# from googletrans import Translator, LANGUAGES
# from video_mapping import get_video_path
# import cv2

# def recognize_speech_from_mic(recognizer, mic):
#     with mic as source:
#         recognizer.adjust_for_ambient_noise(source)
#         print("Listening...")
#         audio = recognizer.listen(source, phrase_time_limit=5)  # Adjusted phrase time limit

#     try:
#         text = recognizer.recognize_google(audio)
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
#     detected_language = detected.lang
#     print(f"Detected language: {LANGUAGES[detected_language]}")
#     return detected_language

# def translate_text(text, target_language='en'):
#     translator = Translator()
#     translation = translator.translate(text, dest=target_language)
#     translated_text = translation.text
#     print(f"Translated text: {translated_text}")
#     return translated_text

# def play_videos_in_sequence(video_paths):
#     for video_path in video_paths:
#         cap = cv2.VideoCapture(video_path)
        
#         if not cap.isOpened():
#             print(f"Error opening video file {video_path}")
#             continue
        
#         while cap.isOpened():
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             frame = cv2.resize(frame, (640, 360))  # Smaller frame size for faster rendering
#             cv2.imshow('Video', frame)

#             if cv2.waitKey(10) & 0xFF == ord('q'):  # Faster playback
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 return
        
#         cap.release()
    
#     cv2.destroyAllWindows()

# def main():
#     recognizer = sr.Recognizer()
#     mic = sr.Microphone()
    
#     while True:
#         # Step 1: Recognize speech
#         text = recognize_speech_from_mic(recognizer, mic)
#         if not text:
#             continue
        
#         # Step 2: Detect the language
#         language = detect_language(text)

#         # Step 3: If the language is not English, translate it to English
#         if language != 'en':
#             text = translate_text(text, target_language='en')

#         # Check for stop command
#         if 'exit' in text.lower():
#             print("Stop command received. Exiting.")
#             break

#         # Step 4: Process the translated or recognized English text
#         words = text.split()
#         print(f"Processing words: {words}")

#         video_paths = [get_video_path(word) for word in words if get_video_path(word)]

#         if video_paths:
#             play_videos_in_sequence(video_paths)

# if __name__ == "__main__":
#     main()

# hbjfdsjfhsdbfuyi heruigdhgubjgbenjsij ksdnvklndfkjv kbsi j  fj jfghjdfbj
# hbjfdsjfhsdbfuyi heruigdhgubjgbenjsij ksdnvklndfkjv kbsi j  fj jfghjdfbj
# hbjfdsjfhsdbfuyi heruigdhgubjgbenjsij ksdnvklndfkjv kbsi j  fj jfghjdfbj
# hbjfdsjfhsdbfuyi heruigdhgubjgbenjsij ksdnvklndfkjv kbsi j  fj jfghjdfbj
# hbjfdsjfhsdbfuyi heruigdhgubjgbenjsij ksdnvklndfkjv kbsi j  fj jfghjdfbj


import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from video_mapping import get_video_path
import cv2

# Dictionary to replace common abbreviations
abbreviation_corrections = {
    "r": "are",
    "u": "you",
    "pls": "please",
    "thx": "thanks",
    "tala":"lock",
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
