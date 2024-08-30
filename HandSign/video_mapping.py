import os

def get_video_path(word, video_folder="video"):
    video_file = os.path.join(video_folder, f"{word}.mp4")
    if os.path.exists(video_file):
        return video_file
    else:
        print(f"No video found for word: {word}")
        return None