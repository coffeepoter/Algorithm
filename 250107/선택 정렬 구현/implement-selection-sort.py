def selected_sort(arr):
    for i in range(n):
        min_val = i
        for j in range(i+1, n):
            if arr[j] < arr[min_val]:
                min_val = j
        tmp = arr[i]
        arr[i] = arr[min_val]
        arr[min_val] = tmp
        
n = int(input())
arr = list(map(int, input().split()))
selected_sort(arr)

for e in arr:
    print(e, end=" ")
