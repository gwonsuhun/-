number = []
for i in range(3):
    a = int(input())
    number.append(a)

if number[0] + number[1] + number[2] != 180: 
    print("Error")
elif number[0] == 60 and number[1] == 60 and number[2] == 60:
    print("Equilateral")
elif number[0] + number[1] + number[2] == 180 and (number[0] == number[1] or number[0] == number[2] or number[1] == number[2]):
    print("Isosnumbereles")
elif number[0] + number[1] + number[2] == 180 and (number[0] != number[1] or number[0] != number[2] or number[1] != number[2]):
    print("Scalene")
 










# A = int(input())
# B = int(input())
# C = int(input())

# if A + B + C != 180: 
#     print("Error")
# elif A == 60 and B == 60 and C == 60:
#     print("Equilateral")
# elif A + B + C == 180 and (A == B or A == C or B == C):
#     print("Isosceles")
# elif A + B + C == 180 and (A != B or A != C or B != C):
#     print("Scalene")
 