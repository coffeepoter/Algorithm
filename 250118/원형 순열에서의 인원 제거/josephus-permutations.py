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
arr = []            
n, k = list(map(int, input().split()))
for i in range(1,n+1):
    q.push(i)

while True:
    if q.empty():
        break
    for i in range(k):
        if i == k-1:
            arr.append(q.front())
            q.pop()
            break
        q.push(q.front())
        q.pop()

for e in arr:
    print(e, end=" ")