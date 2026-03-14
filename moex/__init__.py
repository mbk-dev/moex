"""Реализовано несколько функций-запросов информации о торгуемых акциях и их исторических котировках, результаты которых
напрямую конвертируются в pandas.DataFrame.

Работа функций базируется на универсальном клиенте, позволяющем осуществлять произвольные запросы к MOEX ISS, поэтому
перечень доступных функций-запросов может быть легко расширен.
"""
from .client import ISSClient
from .requests import *

__all__ = [
    "ISSClient",
    "get_reference",
    "find_securities",
    "find_security_description",
    "get_market_candle_borders",
    "get_board_candle_borders",
    "get_market_candles",
    "get_board_candles",
    "get_board_dates",
    "get_board_securities",
    "get_market_history",
    "get_board_history",
    "get_index_tickers",
    "get_index_history",
    "get_indexes_info",
    "get_dividends",
]

__version__ = "1.3.0"
