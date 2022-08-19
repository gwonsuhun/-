# import sys
# sys.stdin = open("25304.txt")

total = int(input())

num =  int(input())

results = 0

for i in range(num):
    item , number = map(int,input().split())
    result = item * number
    results += result 

if results == total:
    print("Yes")
else:
    print("No")