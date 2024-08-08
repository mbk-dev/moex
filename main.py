import pprint

import requests

import moex
import pandas as pd

# index values
with requests.Session() as session:
    data = moex.requests.get_index_history(
        session=session,
        index="RGBITR",  # RUABITR,  IRDIVTR  RUHYRAIF  RUGBINFTR RUCBTRNS
        start="2024-01-01",
        # end="2015-01-01",
        columns=("TRADEDATE", "CLOSE")
    )
    df_index_values = pd.DataFrame(data)
    pprint.pp(list(df_index_values.columns))
    print(df_index_values)


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




