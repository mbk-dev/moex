import requests

import apimoex
import pandas as pd

with requests.Session() as session:
    data = apimoex.requests.get_index_history(session=session, index="RUABITR")
    df = pd.DataFrame(data)

print(df)
