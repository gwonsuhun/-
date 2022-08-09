import numbers


car = int(input())


for _ in range(car):
    carprice = int(input())
    option = int(input())
    carresult = 0

    for i in range(option):
        number,price = map(int,input().split())
        result = number * price
        carresult += result
    print(carresult+carprice)







