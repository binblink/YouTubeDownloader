# YouTubeDownloader

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/026a9012e36146949e83729c447d6923)](https://www.codacy.com/gh/binblink/YouTubeDownloader/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=binblink/YouTubeDownloader&amp;utm_campaign=Badge_Grade)

YouTubeDownloader is a webapp allowing you to download any YouTube video.
You can download either the video file (mp4) or the sound of the YouTube video (mp3).
Enjoy your files :)

## Requirements

- Python 3.10.6
- Flask 2.2
- Pydub <https://github.com/jiaaro/pydub>
- PyTube <https://github.com/pytube/pytube>
- FFMPEG <https://ffmpeg.org/>

### How to install
- Clone this repo locally on your computer
- Open the folder in your IDE
- Download FFMPEG and put the "mmpeg.exe" & "ffprobe.exe" files at the root of the project folder.
- Launch a flask server with the following command line :
  ```flask run```
- You can now access the application from <http://localhost:5000> (or different port according to your local web server settings)
