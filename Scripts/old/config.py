from enum import StrEnum

#enum containing all datasets present in DB
class EventDataUrl(StrEnum):
    BBC = "gpreda/bbc-news/"
    MNH = "therohk/million-headlines"

class FinanceDataDownloadParams:
    types = ["MSFT", "AAPL", "AMZN", "JNJ"]
    start = "1990-01-01"
    end = "2000-01-01"

class EventDataDownloadParams:
    types = [member.value for member in EventDataUrl]
    names = [member.name for member in EventDataUrl]
    fileNames = ["bbc_news", "abcnews-date-text"]