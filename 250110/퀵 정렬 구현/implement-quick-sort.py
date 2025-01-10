def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    
    left = [x for x in arr[1:] if x <= pivot] 
    right = [x for x in arr[1:] if x > pivot] 
    
    return quick_sort(left) + [pivot] + quick_sort(right)

n = int(input())
arr = list(map(int, input().split()))
sorted_arr = quick_sort(arr)
for e in sorted_arr:
    print(e, end=" ")
