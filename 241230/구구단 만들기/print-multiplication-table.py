n = input().split()
a, b = int(n[0]), int(n[1])

for i in range(1, 10):
	for j in range(b, a-1, -1):
		if j % 2 == 0:
			print(f"{j} * {i} = {i * j}", end="")
			if j != a:
				print(" / ", end="");
	print()