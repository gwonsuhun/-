count = int(input())
result = 0
for i in range(1,count+1):
    a,b = map(int,input().split())
    result = a + b
    print(f"Case #{i}: {a} + {b} = {result}")  