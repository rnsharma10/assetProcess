import re
import pandas as pd
with open('NAV.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    f.close()

# collect the data
arr=[]
for line in lines[:]:
    if line.strip():
        # print(line, end="")
        arr.append(line)

arr2 = []


# clean the data
for asset in arr[:]:
    assetComponent = re.split(';', asset)
    assetComponent = [component.replace('  ', ' ').replace('\n', '').upper() for component in assetComponent]
    arr2.append(assetComponent)


df = pd.DataFrame(arr2)
df.to_excel(excel_writer = "asset.xlsx")
