from enum import StrEnum

#enum containing all datasets present in DB
class Dataset(StrEnum):
    STOCKS = "stocks"
    FOREX = "forex"
    COMMODITIES = "commodities"
    NEWS = "news"

#enum containing all tables in DB
class Table(StrEnum):
    STOCK_DATA_LIVE = "stock_data_live"
    FOREX_DATA_LIVE = "forex_data_live"
    COMMODITIES_DATA_LIVE = "commodities_data_live"
    NEWS = "news"