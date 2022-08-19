import sys
sys.stdin = open("14467.txt","r")

num = int(input())

cowrod = []

for i in range(num):
    cow = list(map(int,input().split()))
    cowrod.append(cow)
print(cowrod)