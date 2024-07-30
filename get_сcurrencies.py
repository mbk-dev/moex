import requests

import moex
import pandas as pd

# get names
with requests.Session() as session:
    data = moex.requests.get_board_securities(
        session=session,
        engine="currency",
        market="selt",
        board="CETS",
        columns=("SECID", "SHORTNAME", "NAME", "LATNAME", "CURRENCYID"),
    )
    df = pd.DataFrame(data)

# get history
with requests.Session() as session:
    data = moex.requests.get_board_history(
        session=session,
        security="GLDRUB_TOM",
        engine="currency",
        market="selt",
        board="CETS",
        start="2024-01-01",
        end="2024-02-01"
        # columns=("SECID", "LATNAME", "CURRENCYID", "FREQUENCY", "TYPE", "TYPENAME", "IS_TRADED", "CONSTITUENTS"),
    )
    df1 = pd.DataFrame(data)

print(df[df["SECID"].str.contains("pltrub_tom", case=False)])

print(df1)
