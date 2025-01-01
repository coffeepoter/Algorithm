arr = [
    input().split()
    for _ in range(5)
]

for elem1 in arr:
    for elem2 in elem1:
        elem2 = elem2.upper()
        print(elem2,end=" ")
    print()