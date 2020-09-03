"""
Basic CLI wrapper for youtube-dl and beets. Search YouTube for songs and select a source, \
then use youtube-dl to download the audio and beets to import it to your library (fixing \
the name, metadata, etc. in the process).
"""


import argparse
import os

from colorama import Fore
from typing import List

from beetsdl.video import Video
from beetsdl.search import SearchResults
from beetsdl.download import Downloader


class Session:
    ARROW = Fore.LIGHTYELLOW_EX + "==> " + Fore.RESET

    def __init__(self, term: str, videos: List[Video]):
        """
        Not to be called directly - this object should be initialized with Session.search().
        :param term: query term
        :param videos: list of video objects (defined by beetsdl.video, supplied by beetsdl.search)
        """
        self.term = term
        self.videos = videos
        self.vid = None
        self.downloader = None

    @staticmethod
    def intro(term: str):
        """
        Print the 'searching' notification.
        :param term: query term
        :return: None
        """
        print(Session.ARROW + Fore.LIGHTMAGENTA_EX + f"Searching for {term} ..." + Fore.RESET)

    @staticmethod
    def error(string):
        """
        Print an error message in red.
        :param string: error string
        :return: None
        """
        print(Fore.RED + string + Fore.RESET + '\n')

    @classmethod
    def search(cls, term: str):
        """
        Search for the given query term and return a Session object
        :param term: string to query YouTube for.
        :return: Session object, which is the top-level object for the program.
        """
        Session.intro(term)
        results = SearchResults.search(term)
        return cls(term, results.videos)

    @staticmethod
    def display_video(pos: int, vid: Video):
        """
        Neatly display each video result
        :param pos: integer position (1 to 5)
        :param vid: Video object (defined in beetsdl.video)
        :return: None
        """
        print(Fore.CYAN +
              '[' + str(pos) + '] ' + Fore.RESET +
              Fore.YELLOW + 'Title: ' + Fore.GREEN + vid.title + '\n' +
              Fore.YELLOW + '    Channel: ' + Fore.GREEN + vid.channel + '\n' +
              Fore.YELLOW + '    Duration: ' + Fore.GREEN + vid.duration + '\n' +
              Fore.YELLOW + '    Views: ' + Fore.GREEN + vid.views + Fore.RESET + '\n')

    def prompt_choice(self):
        """
        Get the user's choice (1 to 5) for audio source.
        :return: None
        """
        while not self.vid:
            vid_index_str = input(Session.ARROW + Fore.CYAN + 'Enter choice (default 1): ' + Fore.RESET)

            try:
                vid_index = int(vid_index_str)
                if vid_index < 1 or vid_index > 5:
                    raise ValueError
                else:
                    self.vid = self.videos[vid_index - 1]
            except ValueError:
                Session.error("Choice must be an integer between 1 and 5")

    def display_videos(self):
        """
        Neatly display each video result.
        :return: None
        """
        for i, v in enumerate(self.videos):
            Session.display_video(i+1, v)

    def download(self):
        """
        Create a Downloader object for the session and call youtube-dl's download function.
        :return: None
        """
        self.downloader = Downloader()
        self.downloader.download(self.vid.url)

    def import_into_beets(self):
        """
        Call the beet CLI program and import the downloaded file.
        :return: None
        """
        # TODO: Rework this and properly call the beets API.
        os.system(f'beet import {self.downloader.temp_path.name}')


def main():
    """
    Entry point for CLI.
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "Search",
        metavar="term",
        type=str,
        help="search term to query YouTube"
    )
    args = parser.parse_args()
    term = args.Search

    # Run the search/download/import process from start to finish.
    session = Session.search(term)
    session.display_videos()
    session.prompt_choice()
    session.download()
    session.import_into_beets()


if __name__ == '__main__':
    main()

