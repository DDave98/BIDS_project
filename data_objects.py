from enum import StrEnum

#enum containing all datasets present in DB
class Dataset(StrEnum):
    STOCKS = "stocks"
    FOREX = "forex"
    COMMODITIES = "commodities"

#enum containing all tables in DB
class Table(StrEnum):
    STOCK_DATA_LIVE = "stock_data_live"