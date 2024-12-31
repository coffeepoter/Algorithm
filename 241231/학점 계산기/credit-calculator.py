n = int(input())
m = list(map(float, input().split()))

sum_val = sum(m)
avg = sum_val / len(m)
print(f"{avg:.1f}")
if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")