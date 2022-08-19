#입력은 20 행으로 구성된다. 1 번째 줄부터 10 번째 줄에는 W 대학의 각 참가자의 점수를 나타내는 
# 정수가 11 번째 줄부터 20 번째 줄에는 
# K 대학의 각 참가자의 점수를 나타내는 정수가 적혀있다. 이 정수는 모두 0 이상 100 이하이다.
import sys
sys.stdin = open("5576.txt","r")

w_school =[] #w 학교 점수를 모을 리스트
k_school = [] #k 대학교 점수를


for _ in range(10):  # w 대학교 점수를 입력받고 리스트에넣기
    a = int(input())
    w_school.append(a)


for _ in range(10):  # k 대학교 점수를 입력받고 리스트에넣기 
    b = int(input())
    k_school.append(b)

w_school.sort() #솔트로 오름차순 정리
k_school.sort()


w_result = w_school[9] + w_school[8] + w_school[7] # 뒤에 3명더하기
k_result = k_school[9] + k_school[8] + k_school[7]


print(w_result,k_result)