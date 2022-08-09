
from itertools import count
from pprint import pprint

num = int(input())

lists = []

for x in range(num):
    y = list(input())
    lists.append(y)

width = 5 # 가로로 누울수있는 리스트의 총횟수

for i in range(num):   #행의횟수
    count_1 = 0
    for j in range(num):  #열의횟수
        lists[i][j]
        if "X" in lists[i][1] : 
            count_1 = count_1 + 1
        if "X" in lists[i][3]:
            count_1 = count_1 + 1
        if count_1 == 2:
           width = width - 1
           break


length = 5 # 세로로 누울수있는 리스트의 총횟수

for I in range(num):   #행의횟수
    count_1 = 0
    for J in range(num):  #열의횟수
        lists[i][j]
        if "X" in lists[1][I] : 
            count_1 = count_1 + 1
        if "X" in lists[3][J]:
            count_1 = count_1 + 1
        if count_1 == 2:
           length = length - 1
           break

print(width,length)
import sys

sys.stdin = open('input.txt')
n = int(input())

mine = [list(input()) for _ in range(n)] # 지뢰의 위치가 있는 2차원 리스트
sweeper = [list(input()) for _ in range(n)] # 열어본 위치가 있는 2차원 리스트
minecount = [['.']*n for _ in range(n)] # 최종 결과를 표시할 2차원 리스트

def minefind(mine, x, y) : # 선택한 칸 주변 지뢰의 개수를 탐색하는 함수를 설정했다.
    ans = 0
    open = 0
    if mine[x-1][y-1] == '*' and x > 0 and y > 0:
        ans += 1
    if mine[x-1][y] == '*' and x > 0:
        ans += 1
    if y < len(mine)-1 :
        if mine[x-1][y+1] =='*' and x > 0 :
            ans += 1
        if mine[x][y+1] =='*' :
            ans += 1
    if x < len(mine) -1 : 
        if mine[x+1][y-1] == '*' and y > 0:
            ans += 1
        if mine[x+1][y] == '*' :
            ans += 1
    if mine[x][y-1] == '*' and y > 0:
        ans += 1
    if mine[x][y] == '*' :
        open += 1
    if x < len(mine)-1 and y < len(mine)-1 :
        if mine[x+1][y+1] == '*' :
            ans += 1
# 내가 선택한 칸을 포함한 주변의 9개의 칸을 탐색하였다. 인덱스 초과를 방지하는 조건들을 달아주었다.
# 또한 내가 선택한 칸이 지뢰일시 open 변수에 1을 반환해주었다.
    return ans, open
open = 0
for i in range(n) :
    for j in range(n) :
        if sweeper[i][j] == 'x' :
            ans, ans2 = minefind(mine, i, j)
            open += ans2
            minecount[i][j] = ans # 위의 함수를 사용해 모든 칸을 탐색하여 지뢰의 개수를 표시해주었다.
if open > 0 : # 탐색 도중 open이 1이라도 있을시, 즉 지뢰를 한 번이라도 열었을 시 모든 지뢰를 결과에 표시해주었다.
    for i in range(n) : 
        for j in range(n) :
            if mine[i][j] == '*' :
                minecount[i][j] = '*'
for i in range(n) :
    print(*minecount[i], sep = '')