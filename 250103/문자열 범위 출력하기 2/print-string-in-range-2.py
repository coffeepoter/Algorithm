str1 = input()
n = int(input())
if n < len(str1):
    for i in range(len(str1)-1 , len(str1)-1-n, -1):
        print(str1[i], end="")
else:
    for i in range(len(str1)-1, -1, -1):
        print(str1[i], end="")