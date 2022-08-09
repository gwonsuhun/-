

num = int(input())


guest = list(map(int,input().split()))

pc = [0]*101

result = 0

for i in guest:
    if pc[i] == 0:
        pc[i] = 1
    else:
        result += 1 

print(result)
