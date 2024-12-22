import os

from moviepy.editor import VideoFileClip


def calculate_total_duration(folder_path):
    total_duration = 0
    vidCount = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp4"):
                file_path = os.path.join(root, file)
                vidCount += 1
                try:
                    clip = VideoFileClip(file_path)
                    total_duration += clip.duration
                    clip.close()
                except:
                    print(f"Error processing file: {file_path}")

    return total_duration, vidCount


# Example usage: calculate total duration of .mp4 videos in a folder and its subfolders
folder_path = input("Enter Path: ")
total_duration, vidCount = calculate_total_duration(folder_path)
print(f"Total duration of .mp4 videos: {total_duration/3600} hrs")
print(f"Total Lectures: {vidCount}")
