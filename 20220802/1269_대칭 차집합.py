

A,B = map(str,input().split()) #리스트를만들려고 str으로받음
for _ in range(1):
    A_number = list(map(int,input().split()))


for i in range(1):
    B_number = list(map(int,input().split()))

C = set(A_number)-set(B_number)  # 리스트를 set으로 만들고 set 과 set에서 - 를사용하면 차집합이나온다 
D = set(B_number)-set(A_number)   # C,D의 넣어주고

result = len(C)+len(D) # C 와 D의 원소의길이를 더해준다
print(result)
