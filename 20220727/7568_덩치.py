
# 비교할 인원만큼 반복할 변수를 만든다!
human = int(input())
# 몸무게와 키를 저장할 리스트를 만든다!
result = []

# 몸무게와 키를 각자 입력받고 리스트에 저장한다.
for i in range(human):
    weight, height = map(int, input().split())
    result.append((weight, height))

# 하나씩 비교해보고싶어서 이중 for 문을해봤다.
# 조건은 result[0] result[1] 번의 위치한 몸무게와 키를 반복문을돌면서
# 기준점인 j 몸무게가 k의 몸무게보다 작거나 j 키가 k의 키보다 작으면 rank에 +1 
# 키와 몸무게가 모두 크면 rank의 +1을 하기위해 and를썼다
for j in result:
    rank = 1
    for k in result:
        if j[0] < k[0] and j[1] < k[1]:
                rank += 1
    print(rank,end=" ")
        




