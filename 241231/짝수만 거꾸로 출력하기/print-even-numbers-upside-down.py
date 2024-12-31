n = int(input())
arr = list(map(int, input().split()))

arr = [ele for ele in arr if ele % 2 == 0]
arr.reverse()

for ele in arr:
    print(ele, end=" ")