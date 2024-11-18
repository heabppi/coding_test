import sys
input = sys.stdin.readline
from itertools import permutations

T = int(input())
for _ in range(T):
    k = int(input)
    words = [input().rstrip for _ in range(k)]

    flag = False
    for i in range(k):
        for j in range(k):
            if i == j:
                continue

            p = words[i] + words[j]
            if p == p[::-1]:
                print(p)
                flag = True
                break
        
        if flag:
            break
    
    if not flag:
        print(0)

###############################################################
    # for w1, w2 in permutations(words, 2):
    #     p = w1 + w2
    #     if p == p[::-1]:
    #         print(p)
    #         break
    
    # else:
    #     print(0)

###############################################################

T = int(input())
for _ in range(T):
    k = int(input)
    words = [input().rstrip for _ in range(k)]

    flag = False
    for i in range(k):
        for j in range(k):
            if i == j:
                continue

            p = words[i] + words[j]
            if p == p[::-1]:
                print(p)
                exit(0)
        
    print(0)

#######################################################

# 3. 함수 처리하기

def find_palindrome():
    for i in range(k):
        for j in range(k):
            if i == j:
                continue

            p = words[i] + words[j]
            if p == p[::-1]:
                print(p)
                return
    
    print(0)

T = int(input())       
for _ in range(T):
    k = int(input)
    words = [input().rstrip for _ in range(k)]

    find_palindrome(words)