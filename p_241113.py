word = input()

if word == word[::-1]:
    print('회문')

else:
    print('아님')

#########################################

T = input()
for _ in range(T):
    idx, word = input().split()
    idx = int(idx)-1

    # print(word[:idx] + word[idx+1])
    word = list(word)
    word.pop(idx)

    print(''.join(word))


##########################################

# 내 버전
T = input()

for _ in range(T):
    case_list = list(input())

    result, sum_num = 0, 0
    for i in range(len(case_list)):
        if case_list[i] == 'O':
            sum_num += 1
        else:
            result += sum_num
            sum_num = 0
    
    print(result)


### 해시 : 순서X, 검색빠름 o(1), 중복X



## 수 찾기

N = int(input())
A = set(map(int, input().split()))

M = int(input)
B = list(map(int, input().split()))

# B를 순회하면서
for _ in B:
    # A애 있다면 1출력
    if _ in A: print(1)
    # 없다면? 0 출력
    else: print(0)