from dotenv import load_dotenv
import os
load_dotenv()

# expect 15000 lines of data
nav_link = os.getenv("NAV_LINK")

import requests as req
response = req.get(nav_link)
# fundlist = response.text.split('\n')[:10]
# for i in range(10):
#     print(fundlist[i])
with open('NAV.txt', 'w', encoding="utf-8") as f:
    f.write(response.text)
    f.close()
