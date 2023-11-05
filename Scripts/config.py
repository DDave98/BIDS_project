from enum import StrEnum

#enum containing all datasets present in DB
class EventDataUrl(StrEnum):
    BBC = "gpreda/bbc-news/"
    MNH = "therohk/million-headlines"