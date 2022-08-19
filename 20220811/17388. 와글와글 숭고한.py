soongsil , korea , hanyang = map(int,input().split())


if sum((soongsil,korea,hanyang)) >= 100:
    print("OK")

  
if sum((soongsil,korea,hanyang)) < 100:
    if soongsil < korea and soongsil < hanyang:
        print("Soongsil")
    if korea < soongsil and korea < hanyang:
        print("Korea")
    if hanyang < soongsil and hanyang < korea:
        print("Hanyang")
