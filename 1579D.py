import heapq        
 
from queue import PriorityQueue as PQ
 
 
n=int(input())
for i in range(n):
    pq=PQ()
    ans=0
    length=int(input())
    data=list(map(int,input().split()))
    for j in range(length):
        if data[j]!=0:
            pq.put((-data[j],j+1))
    ans=[]
    count=0
    while pq.qsize()>1:
        a=pq.get()
        b=pq.get()
        count+=1
        ans.append((a[1],b[1]))
        if b[0]!=-1:
            pq.put((b[0]+1,b[1]))
        if a[0]!=-1:
            pq.put((a[0]+1,a[1]))
    print(count)
    for i in ans:
        print(i[0],i[1])
