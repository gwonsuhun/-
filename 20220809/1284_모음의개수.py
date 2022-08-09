





while True: # 마지막 문장이 #이나와야 끝이나니까 !
    letter = input()
    count = 0 # 다시 0으로 초기화 
    if letter == "#":
        break
    for i in letter: # 입력받은 문장에 모음이있으면 카운트 +1 
        if i in 'a' or i in 'e' or i in 'i' or i in 'o' or i in 'u':
            count +=1
        if i in 'A' or i in 'E' or i in 'I' or i in 'O' or i in 'U':
            count +=1
    print(count) # 한문장을 검사하면 프린트
