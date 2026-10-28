def go(idx):
    global ans
    if idx >= n:
        if ans < len(path):
            ans = len(path)
        return
    for s, e in path:
        if lines[idx][0] <= e and s <= lines[idx][1]:
            go(idx+1)
            return
    path.append(lines[idx])
    go(idx+1)
    path.pop()
    go(idx+1)

n = int(input())
lines = []
path = []
for _ in range(n):
    a, b = map(int, input().split())
    temp = (a, b)
    lines.append(temp)
ans = 0
go(0)
print(ans)
# Please write your code here.


"""
고르냐/안고르냐

인데 고르는 경우 겹치는 조건 검사하면됨
인자로 넘겨줄건 몇번째 선분 고르는지
골랐는데 겹치는거면 return

겹치는거 판단은 

a,b랑 c,d있다고 하면

a<=c<=b거나
a<=d<=b거나


5
1 2
3 7
3 4
4 6
7 9
"""