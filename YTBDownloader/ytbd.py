import youtube_dl

url = input("Enter the YouTube URL: ")
start_time = "00:00"
end_time = "02:50"

ydl_opts = {
    "format": "bestvideo[height<=720]+bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
    "writethumbnail": True,
    "outtmpl": "%(title)s.%(ext)s",
    "start_time": start_time,
    "end_time": end_time,
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
