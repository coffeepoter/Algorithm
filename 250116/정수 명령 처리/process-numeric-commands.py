class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        print((not self.items)*1)
    
    def size(self):
        print(len(self.items))

    def pop(self):
        print(self.items[-1])
        self.items.pop()
    
    def top(self):
        print(self.items[-1])

s = Stack()
n = int(input())

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        s.push(cmd[1])
    elif cmd[0] == "pop":
        s.pop()
    elif cmd[0] == "size":
        s.size()
    elif cmd[0] == "empty":
        s.empty()
    elif cmd[0] == "top":
        s.top()
