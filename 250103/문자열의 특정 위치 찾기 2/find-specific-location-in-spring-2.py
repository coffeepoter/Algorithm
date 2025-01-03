str1 = ["apple", "banana", "grape", "blueberry", "orange"]
ch = input()
cnt = 0
for elem in str1:
    if elem[2] == ch or elem[3] == ch:
        print(elem)
        cnt += 1
print(cnt)