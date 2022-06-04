
with open('NAV.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    f.close()

arr=[]
max_length=0
max_index=0
for line in lines[:]:
    if line.strip():
        # print(line, end="")
        arr.append(line.split(";"))

# print(arr)

# check the largest nav number
""" for i in range(1,len(arr)):

    if len(arr[i])>4:
        if len(arr[i][4].split('.')[0]) > max_length:
            max_length = len(arr[i][4].split('.')[0])
            max_index = i
print(max_length)
print(arr[max_index]) """

