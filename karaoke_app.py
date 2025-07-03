from lyricsgenius import Genius
import yt_dlp
import threading
import time
import pygame
from mutagen.mp3 import MP3
import sys
from dotenv import load_dotenv
import os

# load environment variables and set up Genius API access
load_dotenv()
GENIUS_API_TOKEN = os.getenv("GENIUS_API_TOKEN")
genius = Genius(GENIUS_API_TOKEN)

# BASE_DIR setup
if getattr(sys, 'frozen', False):
    # if running from PyInstaller .exe
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AUDIO_PATH = os.path.join(BASE_DIR, "song.mp3")

# user input
song_name = input("Enter the song name: ")

# fetch lyrics
song = genius.search_song(song_name)
if song:
    print("\nLyrics found!\n")
    lyrics = song.lyrics
    lyrics_lines = lyrics.split('\n')
    # clean up the lyrics
    lyrics_lines = [
        line.strip() for line in lyrics_lines
        if line.strip() and not (line.strip().startswith('[') and line.strip().endswith(']'))
    ]
else:
    print("Lyrics not found.")
    sys.exit()

# download audio from YouTube using yt-dlp
print("Downloading audio from YouTube...")

def download_audio(search_query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'outtmpl': os.path.join(BASE_DIR, 'song.%(ext)s'),
        'quiet': False,
        'default_search': 'ytsearch',
        'ffmpeg_location': os.path.join(BASE_DIR, 'ffmpeg', 'bin'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query + " karaoke"])

download_audio(song_name)
print("Audio downloaded!")

# get audio duration
try:
    audio = MP3(AUDIO_PATH)
    audio_duration = audio.info.length
except Exception as e:
    print("Error reading MP3 file.")
    print(f"Details: {e}")
    sys.exit()

# display coloured lyrics function
def display_lyrics(lyrics_lines, total_duration):
    print("\nGet ready to sing!")
    for i in range(3, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)

    time.sleep(1) # small buffer after countdown

    interval = total_duration / len(lyrics_lines)

    for idx, current_line in enumerate(lyrics_lines):
        os.system('cls' if os.name == 'nt' else 'clear')
        print() # newline before first lyric

        for line_idx, line in enumerate(lyrics_lines):
            if line_idx == idx:
                print(f"\033[92m{line}\033[0m") # bright green
            else:
                print(f"\033[93m{line}\033[0m") # yellow

        time.sleep(interval)

# start karaoke
print("Starting the karaoke session...")

# initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load(AUDIO_PATH)

# start music playback
pygame.mixer.music.play()

# start lyrics display in parallel
lyrics_thread = threading.Thread(target=display_lyrics, args=(lyrics_lines, audio_duration))
lyrics_thread.start()

# wait for music to finish
while pygame.mixer.music.get_busy():
    time.sleep(1)

lyrics_thread.join()

# cleanup
pygame.mixer.quit()
try:
    os.remove(AUDIO_PATH)
except:
    pass

print("\nKaraoke session ended. Thanks for singing!")
input("Press Enter to exit...")