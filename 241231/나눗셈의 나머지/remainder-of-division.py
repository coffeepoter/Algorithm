a, b = map(int, input().split())

remainder_counts = {}

while a > 1:
    remainder = a % b 
    if remainder in remainder_counts:
        remainder_counts[remainder] += 1 
    else:
        remainder_counts[remainder] = 1 
    a //= b  

result = sum(count ** 2 for count in remainder_counts.values())

print(result)