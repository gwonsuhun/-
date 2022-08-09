


N,M = map(int,input().split())
counts = 0

for i in range(N,M+1):
    if i%10 == 0:
        counts +=1
