import pprint

import requests

import moex
import pandas as pd


with requests.Session() as session:
    data = moex.requests.get_index_history(
        session=session,
        index="RUCBTRNS",  # RUABITR,  IRDIVTR  RUHYRAIF  RUGBINFTR
        start="2000-01-01",
        # end="2015-01-01",
        columns=("TRADEDATE", "CLOSE")
    )
    df = pd.DataFrame(data)
    pprint.pp(list(df.columns))


print(df)


