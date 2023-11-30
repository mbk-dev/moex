import requests

import apimoex
import pandas as pd


with requests.Session() as session:
    data = apimoex.requests.get_indexes_info(
        session=session,
        columns=("SECID", "LATNAME"),
    )
    df = pd.DataFrame(data)

print(df)
