bombr = [[1, 2, -1, -2], [0, 1, 0, -1], [1, 1, -1, -1]]
bombc = [[0, 0, 0, 0], [1, 0, -1, 0], [1, -1, -1, 1]]
bpath = [] # 설치한 폭탄들 좌표
def go(L):
    global ans
    if len(bpath) == L:
        ret = bomb(bpath)
        if ans < ret:
            ans = ret
        return
    for i in range(3):
        bpath.append(i)
        go(L)
        bpath.pop()

def bomb(bombs):    # bombs로 각 폭탄 자리별 무슨 폭탄 놓을지 리스트가 들어옴
    global ans
    hap = 0
    temp = [[0]*n for _ in range(n)]
    for i in range(len(bombs)):
        nr = plant[i][0]
        nc = plant[i][1]
        if not temp[nr][nc]:
            temp[nr][nc] = 1
            hap += 1
        for w in range(4):
            if (0<=nr+bombr[bombs[i]][w]<n) and (0<=nc+bombc[bombs[i]][w]<n):    
                if not temp[nr+bombr[bombs[i]][w]][nc+bombc[bombs[i]][w]]:
                    temp[nr+bombr[bombs[i]][w]][nc+bombc[bombs[i]][w]] = 1
                    hap += 1
    return hap


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
plant = []
ans = 0
for r in range(n):
    for c in range(n):
        if grid[r][c]:
            plant.append((r, c))
go(len(plant))
print(ans)




"""
강력한 폭발

0, 1로 구성된 N x N 크기의 격자판이 주어집니다.

1은 해당 위치가 폭탄이 놓인 칸임을 의미합니다.

폭탄이 놓인 각 칸마다 다음 3가지 중 정확히 하나의 폭탄을 선택하여, 초토화되는 칸들의 합집합의 크기를 최대화하려고 합니다. 여러 폭탄에 의해 동시에 초토화된 칸은 한 번만 셉니다.

각 폭탄은 폭탄 위치를 포함하여 파란색으로 표시된 영역을 초토화시키게 됩니다. 세 폭탄의 모양은 다음과 같습니다.

세로 폭탄: 폭탄 위치와 그 위·아래 방향으로 각각 2칸씩, 세로로 연속된 5칸을 초토화합니다.
십자 폭탄: 폭탄 위치와 상·하·좌·우로 인접한 4칸, 총 5칸을 초토화합니다.
X자 폭탄: 폭탄 위치와 네 대각선 방향으로 인접한 4칸, 총 5칸을 초토화합니다.
초토화 범위가 격자 밖으로 나가는 경우 그 부분은 무시하며, 격자 안에 걸치는 칸만 초토화됩니다.

걍 순열만들고 최종검사만 하는게 나을듯

각 자리별 뭔폭탄 놓을지 결정한 중복순열 리스트
리스트 순회하면서 i번 자리에 b의 폭탄 발파
b의 폭탄이 발파하는 범위는 
for w in range(4):
    temp[plant[i][0]+bombr[b][w]][plant[i][1]+bombc[b][w]]

"""