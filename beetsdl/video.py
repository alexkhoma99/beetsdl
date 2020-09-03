from typing import NamedTuple


class Video(NamedTuple):
    """
    Video result (only keeping relevant info)
    """
    title: str
    channel: str
    duration: str
    views: str
    url: str

