
# import sys
# sys.stdin = open("FBI.txt")

FBI_member = []
count = 0
for i in range(1,6): #자리수저장
    member = input()
    if "FBI" in member: 
        FBI_member.append(i) # 입력받은문장에 fbi 가있으면 fbi 맴버에 저장
    if "FBI" not in member: # 입력받은문장에 fbi 가없으면  카운트에 1 플러스
        count += 1

if count == 5: # 다섯명중에 fbi 가아닌사람이 다섯명이면
    print("HE GOT AWAY!") #도망갔다 프린트
else:
    print(*FBI_member) # 아니면 저장한 fbi 멤버 출력 
    

