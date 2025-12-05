import json
from .data.constants import JSON_ENCODING , USER_PATH , STATS_EXTENSION
from .cardcreation import _deck_name_to_path

def stats_name(name: str) -> str:
    return USER_PATH + "stats_" + name + STATS_EXTENSION

