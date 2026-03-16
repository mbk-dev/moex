import pprint

import requests

import moex
import pandas as pd

from moex import get_board_history, get_dividends

# index values
# with requests.Session() as session:
#     data = moex.requests.get_index_history(
#         session=session,
#         index="RGBITR",  # RUABITR,  IRDIVTR  RUHYRAIF  RUGBINFTR RUCBTRNS
#         start="2024-01-01",
#         # end="2015-01-01",
#         columns=("TRADEDATE", "CLOSE")
#     )
#     df_index_values = pd.DataFrame(data)
#     pprint.pp(list(df_index_values.columns))
#     print(df_index_values)


# # MOEX securities tickers
# with requests.Session() as session:
#     data = moex.requests.get_board_securities(
#         session=session,
#         table="securities",
#         engine="stock",
#         market="shares",
#         board="TQBR",  # TQTF - список ETF, TQIF - ЗПИФ
#         columns=("SECID", "SHORTNAME", "NAME", "LATNAME", "CURRENCYID"),
#     )
#     df = pd.DataFrame(data)
# print(df)

# Close Values
# with requests.Session() as session:
#     data = get_board_history(
#         session,
#         'SBERP',
#         # start="2013-01-01",
#         # end="2013-03-03",
#         # columns=("TRADEDATE", "CLOSE")
#     )
#     df = pd.DataFrame(data)
#     df.set_index('TRADEDATE', inplace=True)
#     print(df.head(), '\n')
#     print(df.tail(), '\n')

# Dividends
with requests.Session() as session:
    data = get_dividends(
        session,
        'SBERP',
        # start="2013-01-01",
        # end="2013-03-03",
        # columns=("TRADEDATE", "CLOSE")
    )
    df = pd.DataFrame(data)
    # df.set_index('TRADEDATE', inplace=True)
    print(df.head(), '\n')
    print(df.tail(), '\n')


