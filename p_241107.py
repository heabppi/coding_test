# 직사각형 별찍기
a, b = map(int, input().strip().split(' '))
print('\n'.join(['*' * a] * b))

# 같은 숫자는 싫어
def solution(arr):

    answer = []
    before_num = None
    for num in arr:
        if before_num != num:
            answer.append(num)
            before_num = num

    return answer

# 최대공약수와 최소공배수
def solution(n, m):
    answer = []
    # 둘 중 더 큰 숫자
    max_num = n
    if m > max_num: max_num = m

    # 최대공약수(gcd)
    for a in range(1, max_num + 1):
        if (n % a == 0) and (m % a == 0):
            gcd = a
    answer.append(gcd)

    # 최소공배수(lcm)
    lcm = abs(n * m) // gcd
    answer.append(lcm)

    return answer

# 크기가 작은 부분 문자열
def solution(t, p):
    a = len(t)  # t의 길이
    b = len(p)  # p의 길이
    count = 0

    # t에서 p와 같은 길이의 부분 문자열을 모두 확인
    for i in range(a - b + 1):  # 마지막 인덱스는 a - b
        if t[i:i + b] <= p:  # 부분 문자열이 p보다 작거나 같은지 비교
            count += 1

    return count