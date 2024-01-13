import openai
import re,os
import urllib.request
from gtts import gTTS
from moviepy.editor import *
from api_key import API_KEY
from paragraphs_array import paragraphs
os.makedirs("videos",exist_ok=True)
clips=[]
for i in range(1,len(paragraphs)+1):
    audio_clip = AudioFileClip(f"voiceovers/video_{i}.mp3")
    audio_duration = audio_clip.duration

    image_clip = ImageClip(f"images/img_{i}.png").set_duration(audio_duration)
    try:
        clip = image_clip.set_audio(audio_clip)
        final_clip = CompositeVideoClip([clip])
        clips.append(final_clip)

        final_clip.write_videofile(f"videos/video_{i}.mp4", fps=24)
        print(f"The video {i} has been successfully created.")
    except Exception as e:
        print(f"Error creating video {i}: {e}")

if clips:
    print("concatenate all video clips to create a final video")
    final_video = concatenate_videoclips(clips, method="compose")
    final_video.fps = 24  # Set the desired frames per second
    final_video.write_videofile("final_video.mp4")
    print("the video has been created")
else:
    print("No valid clips to concatenate.")
