import requests

import moex
import pandas as pd


with requests.Session() as session:
    data = moex.requests.get_indexes_info(
        session=session,
        columns=("SECID", "LATNAME"),
    )
    df = pd.DataFrame(data)

print(df)
