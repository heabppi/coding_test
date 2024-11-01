# 콜라츠 추측
def solution(num):
    n = 0

    while num != 1:
        if n >= 500:
            return -1
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        n += 1

    return n

# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):

    answer = []
    for ar in arr:
        if ar % divisor == 0:
            answer.append(ar)

    if answer:
        answer.sort()

    else:
        answer = [-1]
    return answer

# 음양 더하기
def solution(absolutes, signs):
    cal = 0
    for num, sign in zip(absolutes, signs):
        if sign:
            cal += num
        else:
            cal -= num
    return cal

# 없는 숫자 더하기
def solution(numbers):
    all_num = [1,2,3,4,5,6,7,8,9,0]

    all_num, numbers = set(all_num), set(numbers)

    missing_num = all_num - numbers

    answer = sum(missing_num)
    return answer

def solution(numbers):
    all_num = [1,2,3,4,5,6,7,8,9,0]
    
    answer = sum(all_num) - sum(numbers)
    return answer

# 제일 작은 수 제거하기(remove, min)
def solution(arr):
    least_num = min(arr)
    arr.remove(least_num)

    if not arr:
        return [-1]

    return arr

# 핸드폰 번호 가리기
def solution(phone_number):

    return '*' * (len(phone_number) - 4) + phone_number[-4:]