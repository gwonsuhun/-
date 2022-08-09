player = int(input())
scores = []
for _ in range(player):
    score = list(map(int,input().split()))
    scores.append(score)

for i in range(player):
    s = 0
    for j in range(3):
        t = scores[i][j]
        ok = 1
        for k in range(player):
            if k == i:
                continue
            if scores[k][j] == t:
                ok = 0; break
        if ok == 1:
            s += t
    print(s)

