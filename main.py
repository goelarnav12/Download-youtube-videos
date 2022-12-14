from pytube import YouTube

VIDEO_SAVE_DIRECTORY = "./video"
AUDIO_SAVE_DIRECTORY = "./audio"

def download(video_url):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()

    try:
        video.download(VIDEO_SAVE_DIRECTORY)
    except:
        print("Failed to download video")

    print("video was downloaded successfully")

def download_audio(video_url):
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio = True).first()

    try:
        audio.download(AUDIO_SAVE_DIRECTORY)
    except:
        print("Failed to download audio")

    print("audio was downloaded successfully")

if __name__ == "__main__":
    url=input("Type url of youtube video: ")
    cmd=input("Do you want only Audio downloaded....if Yes then type '1' else type '2':\n")
    if cmd=='1':
        download_audio(url)
    else:
        download(url)

