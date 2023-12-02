import requests
import pprint

import moex

with requests.Session() as session:
    securitycollections = moex.requests.get_reference(session=session, placeholder="securitycollections")


pprint.pp(securitycollections)