n, m = map(int, input().split())
castle = []
for _ in range(n):
    castle.append(input())
print(castle)

n_cnt = 0
for i in range(n):
    if 'X' not in castle[i]:
        n_cnt += 1
print(n_cnt)