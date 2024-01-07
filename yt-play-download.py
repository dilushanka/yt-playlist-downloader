from pytube import Playlist

def get_validated_url():
    while True:
        try:
            playlist_url = input("Enter the YouTube playlist URL: ")
            playlist = Playlist(playlist_url)
            return playlist
        except Exception as e:
            print(f"Invalid URL or an error occurred: {e}")

def display_resolution_options(playlist):
    print("\nAvailable Resolutions:")
    unique_resolutions = set()

    for video in playlist.videos:
        for stream in video.streams.filter(file_extension="mp4"):
            if stream.resolution:
                unique_resolutions.add(stream.resolution)

    for i, resolution in enumerate(sorted(unique_resolutions), start=1):
        print(f"{i}. {resolution}")

def get_user_resolution_choice():
    while True:
        try:
            choice = int(input("Enter the number corresponding to your preferred resolution: "))
            return choice
        except ValueError:
            print("Invalid choice. Please enter a valid number.")

def download_playlist(playlist, resolution_choice):
    print(f"\nDownloading all videos in the playlist: '{playlist.title}'\n")

    for video in playlist.videos:
        stream = video.streams.filter(file_extension="mp4", resolution=resolution_choice).first()
        if stream:
            print(f"Downloading: {video.title} ({resolution_choice})")
            stream.download()

    print("\nDownload completed for the entire playlist.")

def main():
    playlist = get_validated_url()
    display_resolution_options(playlist)
    resolution_choice = get_user_resolution_choice()

    download_playlist(playlist, resolution_choice)

if __name__ == "__main__":
    main()
