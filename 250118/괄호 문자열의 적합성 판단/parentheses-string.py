class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        return not self.items
    
    def size(self):
        return len(self.items)

    def pop(self):
        self.items.pop()
    
    def top(self):
        print(self.items[-1])

s = Stack()
arr = input()

for i in range(len(arr)):
    if arr[i] == '(':
        s.push('(')
    elif arr[i] == ')':
        if s.empty():
            print("No")
            continue
        else:
            s.pop()
if s.empty():
    print("Yes")
else:
    print("No")