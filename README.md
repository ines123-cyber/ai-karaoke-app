# AI Karaoke App

This project is a simple karaoke app. It fetches lyrics using the Genius API and downloads karaoke tracks from YouTube using `yt-dlp`.
It then displays the lyrics highlighted in sync with the music.

---

## Features

- Automatic fetching of lyrics using Genius API
- Karaoke track download from YouTube via `yt-dlp`
- Time-synced lyrics based on song duration
- Real-time lyric highlighting (current line: bright green, others: yellow)
- Cross-platform compatibility (Windows/Linux/Mac)

---

## AI Component

This project demonstrates a basic level of AI integration through:

- **Intelligent lyric parsing** using NLP-like filtering to clean up non-singing parts like `[Chorus]`, `[Verse]`, etc.
- **Synchronized timing logic**, where lyric display is mapped proportionally across the total audio duration.

---

## Technologies Used

- Language: **Python**
- [Genius](https://genius.com/) API
- **yt-dlp**
- **FFmpeg** (`ffmpeg.exe`, `ffplay.exe`, `ffprobe.exe`) used by `yt-dlp` to convert downloaded audio to `.mp3`
- **mutagen** (for getting MP3 duration)
- **pygame** (for audio playback)
- Standard Libraries: `os`, `time`, `threading`

---

## Installation

This repository uses [Git Large File Storage (LFS)](https://git-lfs.github.com/) to include FFmpeg executables (`ffmpeg.exe`, `ffplay.exe`, and `ffprobe.exe`) in the `ffmpeg/bin` folder. These are required by `yt-dlp` to convert downloaded YouTube audio into `.mp3` format.
You must install Git LFS before cloning this repo to run the app locally.

1. **Install Git LFS:**

   - On Windows: Download and run the [Git LFS installer](https://git-lfs.github.com/).
   - Or, use the command line:

    ```bash
    git lfs install
    ```

2. **Clone this repo:**

    ```bash
    git clone https://github.com/schak04/ai-karaoke-app
    cd ai-karaoke-app
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

---

## Genius API Key Setup

This app requires a Genius API key to fetch song lyrics.

### Steps

1. Go to the [Genius API Clients page](https://genius.com/api-clients) and log in or sign up.
2. Create a new API client (you can name it anything).
3. Click on "Generate Access Token", then copy the access token.
4. In the project folder:
    - Rename the `.env.example` file to `.env`
    - In your `.env` file, replace 'paste_your_genius_api_key_here' with your actual Genius API key:

      ```env
      GENIUS_ACCESS_TOKEN=paste_your_genius_api_key_here
      ```

5. You're now ready to run the app.

> **Note**: Never share your `.env` file publicly. It's already ignored in `.gitignore` for security reasons.

---

## How to Run

### Option 1: Run the script

1. Open a terminal in the project folder.
2. Run the script using:

    ```bash
    python karaoke_app.py
    ```

3. Enter the song name, and sit back as the system downloads lyrics and audio.
4. Sing along with the highlighted lyrics.

### Option 2: Build and Run EXE (Windows Only)

1. Run `build.bat` to build the `karaoke_app.exe` file in the `dist` folder.
2. Go to the `dist` folder and double-click `karaoke_app.exe`.
3. Enter the song name, and sit back as the system downloads lyrics and audio.
4. Sing along with the highlighted lyrics.

---

## Notes

- The base version of this app is purely CLI-based, with future plans for the addition of a proper GUI and more features.
- An internet connection is required for fetching lyrics and karaoke audio.
- If multiple songs have the same name, include the artist in your search.

    > Format: `<song> <artist>` instead of just `<song>`.

- Avoid using special characters in song names.
- Console must support ANSI escape codes, as it is essential for displaying coloured lyrics.

---

## Author

Copyright (c) 2025 [Saptaparno Chakraborty](https://github.com/schak04).  
All rights reserved.

---
