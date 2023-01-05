import youtube_dl

# Read in the YouTube URL and file type from the user
url = input("Enter the YouTube URL: ")
file_type = input("Enter the file type (mp3 or mp4): ")

if file_type == "mp3":
    # Set the download options for an mp3 file
    ydl_opts = {
        "format": "bestaudio/best",  # Download the best quality audio
        "postprocessors": [{
            "key": "FFmpegExtractAudio",  # Extract the audio
            "preferredcodec": "mp3",  # Use the mp3 codec
            "preferredquality": "192",  # Use a bitrate of 192k
        }],
        "writethumbnail": True,  # Write the thumbnail to the output file
        "outtmpl": "%(title)s.%(ext)s",  # Use the title of the video as the file name
    }
elif file_type == "mp4":
    # Set the download options for an mp4 file
    ydl_opts = {
        "format": "bestvideo[height<=720]+bestaudio/best",  # Download the best quality video with a height <= 720px
        "writethumbnail": True,  # Write the thumbnail to the output file
        "outtmpl": "%(title)s.%(ext)s",  # Use the title of the video as the file name
    }
else:
    print("Invalid file type. Please enter 'mp3' or 'mp4'.")
    exit()

# Download the video
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
