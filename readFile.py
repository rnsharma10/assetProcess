import re
with open('NAV.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    f.close()

arr=[]
for line in lines[:]:
    if line.strip():
        # print(line, end="")
        arr.append(line)
