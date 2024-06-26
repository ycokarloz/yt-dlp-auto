import subprocess
import os

def download_audio(url):
    yt_dlp_path = r"C:\path\to\yt-dlp.exe"  # Change path to yt-dlp.exe
    output_dir = os.path.dirname(yt_dlp_path)
    ffmpeg_location = r"C:\path\to\ffmpeg.exe" # Change path to ffmpeg.exe
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
