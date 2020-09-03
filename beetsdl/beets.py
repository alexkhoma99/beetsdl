import os


def import_into_beets(path: str):
    """
    Very primitive way of calling beets, this whole thing should be done as a beets plugin.
    :param path:
    :return: None
    """
    os.system(f'beet import {path}')
