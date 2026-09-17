def sel(L):
    if len(path) == N:
        print(*path)
        return
    for i in range(1, L+1):
        path.append(i)
        sel(L)
        path.pop()

K, N = map(int, input().split())

path = []
sel(K)

"""
K개 중에 1개를 N번 뽑기

1이상 K이하의 정수를 하나 고르는 행위를 N번 반복하여 나올 수 있는 모든 서로 다른 수열을 구해주는 프로그램을 작성해보세요.
"""