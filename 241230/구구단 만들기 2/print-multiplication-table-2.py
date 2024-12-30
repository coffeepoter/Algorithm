n = input().split()
a, b = int(n[0]), int(n[1])

for i in range(2, 9, 2):
	for j in range(b, a-1, -1):
			print(f"{j} * {i} = {i * j}", end="")
			if j != a:
				print(" / ", end="");
	print()