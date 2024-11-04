# 내적
def solution(a, b):
    return sum(a_ * b_ for a_, b_ in zip(a,b))

# 가운데 글자 가져오기
def solution(s):
    if len(s) % 2 == 0:
        center = len(s) // 2
        return s[center-1:center+1]
    else:
        center = len(s) // 2
        return s[center]
    
# 좋았다고 생각되는 코드
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2+1]

# 수박수박수박수박수박수?
def solution(n):
    if n % 2 == 1:
        str = (n // 2) * '수박' + '수'
    else:
        str = (n // 2) * '수박'
    return str

# 좋았다고 생각되는 코드
def solution(n):
    return '수박' * (n//2) + '수' * (n%2)

# 약수의 개수와 덧셈
def solution(left, right):
    answer = 0
    plus, minus = 0, 0
    for num in range(left, right+1):
        list = [i for i in range(1, num+1) if num % i == 0]
        if len(list) % 2 == 0:
            plus += num
        else:
            minus += num
    answer = plus - minus
    return answer

# 문자열 내림차순으로 배치하기
def solution(s):
    return ''.join(sorted(s, reverse=True))

# 부족한 금액 계산하기
def solution(price, money, count):
    sum_money = sum([price * c for c in range(1, count+1)])
    if sum_money - money > 0:
        return sum_money - money
    else: return 0

# 문자열 다루기 기본
def solution(s):
    # 길이가 4 또는 6이고, 숫자로만 구성되어 있는지 확인
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False
    
# 행렬의 덧셈
def solution(arr1, arr2):
    result = []

    for i in range(len(arr1)):
        row_sum = []
        for j in range(len(arr1[i])):
            row_sum.append(arr1[i][j] + arr2[i][j])
        result.append(row_sum)
        
    return result

# 다른 사람의 풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))

