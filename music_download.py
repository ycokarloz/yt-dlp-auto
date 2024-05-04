import subprocess
import os

def download_audio(url):
    yt_dlp_path = r"D:\Music\Music\yt-dlp.exe"  # Correct path to yt-dlp.exe
    output_dir = os.path.dirname(yt_dlp_path)
    ffmpeg_location = r"D:\Music\Music\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
    command = [
        yt_dlp_path,
        "--extract-audio",
        "--audio-format", "mp3",
        "--ffmpeg-location", ffmpeg_location,
        "-o", "%(title)s.%(ext)s",
        url
    ]
    subprocess.run(command, cwd=output_dir)

def main():
    url = input("Enter the YouTube video URL: ")
    download_audio(url)

if __name__ == "__main__":
    main()
