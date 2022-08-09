number = [] # 5개의 자연수의 평균과 중앙값을구해야한다.

for i in range(5): #다섯개의자연수를 입력받는다
    a = int(input())
    number.append(a) #리스트에 넣어준다

result = 0 # 점수의합을 계산

for i in number:
    result = result + i #점수의 합을 더해준다

number.sort() # 오름차순으로정리
print(round(result/5),number[2]) # 총점수를 5을나누고 소수점없애기  넘버의 중앙값 출력
