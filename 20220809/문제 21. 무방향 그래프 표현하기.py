from pprint import pprint 

x=7
y=6

lists = [[0] * x for _ in range(x)]

for _ in range(y):
    v1, v2 = map(int,input().split())
    lists[v1][v2] = 1
    lists[v2][v1] = 1 
pprint(lists)