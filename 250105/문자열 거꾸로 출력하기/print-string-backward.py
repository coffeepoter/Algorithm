while True:
    s = input()
    if s == "END":
        break
    else:
        arr = list(s)
        arr.reverse()
        print(''.join(arr))