n = int(input())
arr = []
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push_back":
        a, b = cmd[0], int(cmd[1])
        arr.append(b)
    elif cmd[0] == "pop_back":
        arr.pop()
    elif cmd[0] == "size":
        print(len(arr))
    elif cmd[0] == "get":
        a, b = cmd[0], int(cmd[1])
        print(arr[b-1])