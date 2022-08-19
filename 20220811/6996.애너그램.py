from turtle import back


num = int(input())

for _ in range(num):
    a_word , b_word = map(str,input().split())
    count = 0
    for i in a_word:
        for j in b_word:
            if i == j:
                count += 1
    if count == len(a_word) and count == len(b_word) :
        print(f"{a_word} & {b_word} are anagrams.")
        break
    else:
        print(f"{a_word} & {b_word} are not anagrams.")


