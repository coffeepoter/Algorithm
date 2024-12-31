arr = ['L', 'E', 'B', "R", 'O', 'S']
ch = input()
idx = -1
for i in range(len(arr)):
    if arr[i] == ch:
        idx = i
if idx == -1:
    print("None")
else:
    print(idx)