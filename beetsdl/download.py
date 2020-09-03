from youtube_dl import YoutubeDL
from tempfile import TemporaryDirectory


class Downloader:
    """Download a song"""
    def __init__(self):
        self.temp_path = TemporaryDirectory()
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl': self.temp_path.name + '/%(title)s.%(ext)s',
        }
        self.ydl = YoutubeDL(ydl_opts)

    def download(self, url: str):
        self.ydl.download([url])

    def __del__(self):
        self.temp_path.cleanup()
