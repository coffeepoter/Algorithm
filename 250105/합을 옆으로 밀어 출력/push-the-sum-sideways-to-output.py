n = int(input())
sum_val = 0
for _ in range(n):
    sum_val += int(input())
s = str(sum_val)
s = s[1:] + s[0]
print(s)