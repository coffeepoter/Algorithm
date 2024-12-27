n = input().split()
h, w = int(n[0]), int(n[1])
b = int((10000*w) / (h*h))
print(b)
if b >= 25:
    print("Obesity")