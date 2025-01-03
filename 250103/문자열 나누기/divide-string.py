n = int(input())
arr = input()
cnt = 0
for elem in arr:
    if elem == " ":
        continue
    print(elem, end="")
    cnt += 1
    if cnt % 5 == 0:
        print()