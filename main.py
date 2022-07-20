from pytube import YouTube
import os

def audioDownloader(url, download_folder=None):
    try:
        youtube = YouTube(url)
        title = youtube.title

        print(f"\nNow downloading (Audio Only), {title}")

        audio = youtube.streams.filter(only_audio=True).first()

        print(f"File Size: {round(audio.filesize/(1024*1024))} MB")

        if download_folder == None:
            output = audio.download()

        else:
            try:
                output = audio.download(download_folder)
            except:
                print("\nSomething went wrong please check your download folder path.")

        print(f"Download Complete, {title}")

        if download_folder == None:
            print("\nSaved to current folder\n")

            name, ext = os.path.splitext(output)
            mp3_name = name + ".mp3"
            os.rename(output, mp3_name)

        else:
            try:
                print(f"\nSaved to {os.path.abspath(download_folder)}\n")

                name, ext = os.path.splitext(output)
                mp3_name = name + ".mp3"
                os.rename(output, mp3_name)
            except:
                print("Something went wrong please check your download folder path.")
    except:
        print("\nSomething went wrong please try again.")

def videoDownloader(url, download_folder=None):
    try:
        youtube = YouTube(url)
        title = youtube.title

        print(f"\nNow downloading, {title}")

        video = youtube.streams.filter(progressive=True, file_extension="mp4").first()

        print(f"File Size: {round(video.filesize/(1024*1024))} MB")

        if download_folder == None:
            video.download()

        else:
            try:
                video.download(download_folder)

                print(f"Download Complete, {title}")

                if download_folder == None:
                    print("\nSaved to current folder\n")

                else:
                    print(f"\nSaved to {os.path.abspath(download_folder)}\n")
            except:
                print("Something went wrong please check your download folder path.")
    except:
        print("\nSomething went wrong please try again.")

if __name__ == "__main__":
    try:
        while True:
            format = int(input("Mp4 (1) or Mp3 (2): "))
            url = input("Insert a youtube url/link: ")
            downloadFolder = input("Insert a download folder path (Optional): ")

            if format == 1:
                if downloadFolder == "":
                    videoDownloader(url)
                else:
                    videoDownloader(url, downloadFolder)
            elif format == 2:
                if downloadFolder == "":
                    audioDownloader(url) 
                else:
                    audioDownloader(url, downloadFolder)
            else:
                print("Invalid option please try again")
    except KeyboardInterrupt:
        print("The program has stopped.")