a, b = map(int, input().split())
lists = []

for _ in range(a):
    lists.append(input())#여기까지 입력

result1, result2 = 0, 0

for l in lists:
    if "X" not in l:
        result1 += 1#한 행씩 검사

for i in range(b):#한 열씩 검사하기 위해 for
    if "X" not in [lists[j][i] for j in range(a)]:
        result2 +=1

print(max(result1, result2))