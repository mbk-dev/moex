import requests
import pprint

import apimoex

with requests.Session() as session:
    securitycollections = apimoex.requests.get_reference(session=session, placeholder="securitycollections")


pprint.pp(securitycollections)