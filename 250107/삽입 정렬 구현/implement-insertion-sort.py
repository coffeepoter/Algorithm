def insert_sort(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    
    return arr

n = int(input())
arr = list(map(int, input().split()))
insert_sort(n, arr)
for e in arr:
    print(e, end=' ')