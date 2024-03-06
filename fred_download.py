import pytube
import os

def download_youtube_audio(url):
    try:
        youtube = pytube.YouTube(url)
        audio_stream = youtube.streams.filter(only_audio=True).first()
        
        # Download to the current directory
        out_file = audio_stream.download()

        # Rename with original title and .mp3 extension
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print(f"Audio downloaded successfully as: {new_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ")
    download_youtube_audio(youtube_url)