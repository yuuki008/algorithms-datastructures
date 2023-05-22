from heapq import heappush, heappop
import sys

que = []
ans = []
for line in sys.stdin.readlines():
    cmd, *v = line.split()
    if cmd == 'insert':
        heappush(que, -int(v[0]))
    elif cmd == 'extract':
        ans.append("%d\n" % -heappop(que))
sys.stdout.writelines(ans)