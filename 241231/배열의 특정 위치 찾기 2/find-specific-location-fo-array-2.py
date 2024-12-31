arr = list(map(int, input().split()))
sum_odd, sum_even = 0, 0

for i in range(0, len(arr)):
    if i % 2 == 1:
        sum_odd += arr[i]
    else:
        sum_even += arr[i]

if sum_odd >= sum_even:
    print(sum_odd - sum_even)
else:
    print(sum_even - sum_odd)