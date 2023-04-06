# !/usr/bin/python
# -*- coding: utf-8 -*-

from moviepy.editor import *
from dotenv import load_dotenv
import os
import openai


load_dotenv("cred.env")

# this Part generate a mp3 file

file_path = input("Bitte den Daten eingeben:")

temp_typ = file_path.split(".")[-1]
temp_str = file_path.split("\\")[-1]

txt_path = file_path.replace(temp_str, "output.txt")

if temp_typ in os.getenv("VIDEO_FILE_TYPE"):
    print("Video wurde eigegeben.")
    mp3_path = file_path.replace(temp_str, "temp.mp3")
    video = VideoFileClip(file_path)
    audio = video.audio
    audio.write_audiofile(mp3_path)
    del_flg = True
    print("mp3 Daten wurde erzeugt.")
elif temp_typ in os.getenv("AUDEO_FILE_TYPE"):
    print("Audio wurde eigegeben.")
    mp3_path = file_path
    del_flg = False
else:
    print("Falsche Datatype !")
    sys.exit()

# imput the api-key
openai.api_key = os.getenv("OPENAI_API_KEY")

# exchange daten with openai
with open(mp3_path, "rb") as audio_file:
    print("Bitte warte eine Minute oder so ... ")
    transcript = openai.Audio.transcribe("whisper-1", audio_file, response_format="text")
# write
with open(txt_path, "w") as text_file:
    text_file.write(transcript)

if del_flg:
    os.remove(mp3_path)

print('Danke für deine Geduld, schon fertig ! Bitte finde die Daten in Output.txt.')

