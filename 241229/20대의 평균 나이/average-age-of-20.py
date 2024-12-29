sum = 0
cnt = 0
while 1:
    age = int(input())
    if age >= 30:
        break
    sum += age
    cnt += 1
print(f"{sum/cnt:.2f}")