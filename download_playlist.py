from pytube import Playlist
from pytube.exceptions import PytubeError
import urllib.error
import os
import logging
import re
import json

# Setup logging
logging.basicConfig(filename='errorlog.txt', level=logging.ERROR, format='%(asctime)s - %(message)s')
# Set the desired resolution
resolution = '720p'
# Define the playlist URL ( will be like https://youtube.com/playlist?list= ... )
playlist_url = ' Define the playlist URL '
# Define the download directory (change to a valid directory path where you have write permissions)
download_dir = ' Define the download directory '
# Define a file to store the mapping of original titles to sanitized filenames
mapping_file = 'downloaded_videos.json'

# Function to sanitize file names
def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "_", filename)

# Load existing mappings if they exist
if os.path.exists(mapping_file):
    with open(mapping_file, 'r') as file:
        downloaded_videos = json.load(file)
else:
    downloaded_videos = {}

i = 0
try:
    # Create a Playlist object
    playlist = Playlist(playlist_url)

    print(f'Downloading videos from playlist: {playlist.title}')
    
    # Loop through all the videos in the playlist
    for video in playlist.videos:
        i += 1
        video_title = video.title
        try:
            print(f'{i} Processing: {video_title}')
            
            # Check if the video has already been downloaded
            if video_title in downloaded_videos:
                print(f'{i} Skipping: {video_title} (already exists)')
                continue
            
            # Define the sanitized file name
            sanitized_title = sanitize_filename(video_title)
            file_name = os.path.join(download_dir, f"{sanitized_title}.mp4")
            
            print(f'{i} Downloading: {video_title}')
            # Get the desired resolution stream
            stream = video.streams.filter(res=resolution, progressive=True).first()
            if stream:
                stream.download(output_path=download_dir, filename=f"{sanitized_title}.mp4")
            else:
                print(f'720p resolution not available for: {video_title}, downloading highest resolution available.')
                stream = video.streams.get_highest_resolution()
                stream.download(output_path=download_dir, filename=f"{sanitized_title}.mp4")
            
            # Update the mapping
            downloaded_videos[video_title] = sanitized_title
            with open(mapping_file, 'w') as file:
                json.dump(downloaded_videos, file)
        
        except Exception as e:
            # Log the error and continue with the next video
            error_message = f'Error processing {video_title}: {str(e)}'
            print(error_message)
            logging.error(error_message)
    
    print(f'{i} Download complete!')

except urllib.error.URLError as e:
    error_message = f'URL Error: {e.reason}'
    print(error_message)
    logging.error(error_message)
except PytubeError as e:
    error_message = f'Pytube Error: {str(e)}'
    print(error_message)
    logging.error(error_message)
except Exception as e:
    error_message = f'An unexpected error occurred: {str(e)}'
    print(error_message)
    logging.error(error_message)
