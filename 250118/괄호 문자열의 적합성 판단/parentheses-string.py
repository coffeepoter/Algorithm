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

def sol(s, arr):
    for i in range(len(arr)):
        if arr[i] == '(':
            s.push('(')
        elif arr[i] == ')':
            if s.empty():
                return False
            else:
                s.pop()
    if s.empty():
        return True
    else:
        return False

s = Stack()
arr = input()
if sol(s,arr):
    print("Yes")
else:
    print("No")