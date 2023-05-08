"""
https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_B
"""
n,q=map(int,input().split())
d={}
time=0
queue=[]
for i in range(n):
        a,b=input().split()
        d[a]=int(b)
        queue.append(a)
while queue:
    val=d[queue[0]]
    if val>int(q):
        temp=queue.pop(0)
        queue.append(temp)
        d[temp]=val-q
        time+=q
    else:
        time+=val
        name=queue[0]
        queue.pop(0)
        print(name,time)


if __name__ == "__main__":
  q = 100
  n = 5
  p = {
    'p1': 180,
    'p2': 80,
    'p3': 200,
    'p4': 350,
    'p5': 20
  }
  queue = ['p1', 'p2', 'p3', 'p4', 'p5']
  queue(n, q, p)