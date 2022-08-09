num = int(input())


list = []
for _ in range(num):
    m = int(input())
    list.append(m)  

list.sort()
print(*list, sep='\n')