import re
from dotenv import load_dotenv
import os
with open('NAV.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    f.close()
load_dotenv()
arr=[]
for line in lines[:]:
    if line.strip():
        # print(line, end="")
        arr.append(line)

currentAssetName = ''

myAssetList = set(os.environ.get("MY_ASSET").split(';'))


arr2 = []

for asset in arr[:]:
    assetComponent = re.split(';', asset)
    assetComponent = [component.replace('  ', ' ').replace('\n', '').upper() for component in assetComponent]
    if not(re.match("^\d+$", assetComponent[0])) and assetComponent[0] in myAssetList:
            currentAssetName = assetComponent[0]
    elif currentAssetName and assetComponent[0].isnumeric():
        arr2.append(assetComponent)
    else:
        currentAssetName=''

for a in arr2:
    print(a)
print(len(arr2))