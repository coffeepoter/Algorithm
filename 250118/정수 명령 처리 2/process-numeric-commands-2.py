from collections import deque

class Queue:
    def __init__(self):          
        self.dq = deque()
                
    def push(self, item):       
        self.dq.append(item)
                
    def empty(self):             
        return not self.dq
                
    def size(self):              
        return len(self.dq)
        
    def pop(self):               
        return self.dq.popleft()
                
    def front(self):            
        return self.dq[0]


q = Queue()            
n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        q.push(cmd[1])
    elif cmd[0] == "pop":
        print(q.front())
        q.pop()
    elif cmd[0] == "size":
        print(q.size())
    elif cmd[0] == "empty":
        print(q.empty() * 1)
    elif cmd[0] == "front":
        print(q.front())
