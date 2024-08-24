# YouTube Playlist Downloader

This script downloads all videos from a YouTube playlist to the local machine. It uses the `pytube` library to handle the downloading process and includes several features to ensure a smooth and efficient operation.

## Features

- **Download All Videos**: Automatically fetches and downloads all videos in the specified YouTube playlist.
- **Safe File Names**: The script sanitizes video titles to create filenames that are safe for your filesystem.
- **Optimized Resolution**: Downloads videos in 720p resolution when available, with a fallback to the highest available resolution.
- **Error Logging**: Any errors during the download process are logged to `errorlog.txt`.
- **Duplicate Prevention**: A JSON file (`downloaded_videos.json`) keeps track of downloaded videos, preventing duplicates.

## Prerequisites

- Python 3.x
- `pytube` library

You can install `pytube` using pip:
```
pip install pytube
```

## Usage
1. **Set Playlist URL:** Modify the playlist_url variable in the script to point to your desired YouTube playlist.

2. **Set Download Directory:** Specify the download directory by modifying the download_dir variable. Make sure the directory exists and you have write permissions.

3. **Run the Script:** Execute the script:
```
python download_playlist.py
```
4. **Monitor Progress:** The script will display the progress of each video being processed and downloaded.
5. **Error Handling:** Any errors encountered during the process will be logged in errorlog.txt.

## Customization
- File Name Sanitization: The sanitize_filename function can be modified if you want to implement a different naming convention.
- Resolution Selection: The script currently defaults to 720p resolution. If you need a different default, you can modify the resolution filter in the code.

## Troubleshooting
- **Connection Issues:** Ensure that your internet connection is stable.
- **Permission Errors:** Verify that the download directory has the appropriate permissions.
- **Pytube Issues:** Ensure that you have the latest version of pytube.
