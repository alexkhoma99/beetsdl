from typing import List, Dict

from youtube_search import YoutubeSearch
from beetsdl.video import Video


class SearchResults:
    """
    Object for getting/storing video search results.
    """
    def __init__(self, results):
        """Don't use directly - call VideoResults.search to init"""
        self.raw_results = results
        self.videos = [Video(
                             v['title'],
                             v['channel'],
                             v['duration'],
                             v['views'],
                             'https://youtube.com' + v['url_suffix']
                            )
                       for v in results]

    @classmethod
    def search(cls, term: str):
        return cls(YoutubeSearch(term, max_results=5).to_dict())

