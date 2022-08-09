num =  int(input())

for _ in range(num):
    a = str(input())
    count_1 = 0
    count_2 = 0

    for i in a:       
        if i[0] ==  "(" :
             count_1 = count_1 +1
        elif i[0] == ")" :      
            count_2 = count_2 +1                       
        if count_1 == count_2:
         print("YES")    
        else:
         print("NO")
       