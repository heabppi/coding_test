import sys
input = sys.stdin.readline

# N = int(input())


# # 1. 조건문으로 분기하기
# book_sales = dict()
# book_dict = {}
# for i in range(N):
#     book_name = input().rstrip()

#     # 키값이 존재하지 않는 경우
#     if book_name not in book_sales:
#         # 새로 생성
#         book_sales[book_sales] = 1

#     # 키값이 존재하는 경우
#     else:
#         book_sales[book_name] += 1

# # 2. get 메서드 활용하기
# book_sales = dict()
# book_dict = {}
# for i in range(N):
#     book_name = input().rstrip()

#     # 없으면 0 입력 + 1
#     book_sales[book_name] = book_sales.get(book_name, 0) + 1


# # 3. defaultdict() 객체 활용하기
# # 해당하는 value의 값을 정해진 자료형을 자동으로 만들어준다
# from collections import defaultdict     #value값에 dafault가 정해진 dict
# # book_sales = defaultdict(int)         # value 값으로 0
# # book_sales = defaultdict(str)         # value 값으로 ' ' 
# # book_sales = defaultdict(list)        # value 값으로 []

# book_sales = defaultdict(int)
# for _ in range(N):
#     book_name = input().rstrip()
#     book_sales[book_name] += 1

# # 4. Counter() 객체 활용하기
# from collections import Counter
# book_sales = [input().rstrip() for _ in range(N)]
# book_sales = Counter(book_sales)


# # 가장 많이 팔린 책 찾기

# # 1) 선형 탐색
# # 초기값 설정
# max_num = 0
# max_sales_book = ''

# for book, cnt in book_sales.items():
#     if cnt > max_num:
#         max_sales_book = book
#         max_num = cnt

#     # 만약 똑같이 팔렸다면?
#     elif cnt == max_num:
#         # 더 작은 책 제목으로 갱신
#         max_sales_book = min(book, max_sales_book)

# print(max_sales_book)

# # 2) 딕셔너리 정렬                                             #기준1, 기준2
# sorted_sales_info = sorted(book_sales.items(), key=lambda x: (-x[1], x[0]))

# print(sorted_sales_info[0][0])


## 일곱 난장이 찾기
dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

# i -> 0일 때, j -> 1부터
# i -> 1일 때, j -> 2부터
flag = False
for i in range(8):
    for j in (i+1, 9):
        if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
            spy = [i, j]
            flag = True
            break  # 이중 for 반복문이 되면 가장 가까운 for문만 강제종료

        if flag:
            break

for idx in range[9]:
    if idx in spy:
        continue

    print(dwarfs[idx])

###########################################################

# 일곱 난장이 찾기

from itertools import combinations

dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

for spy1, spy2 in combinations(dwarfs, 2):
    if sum(dwarfs) - spy1 - spy2 == 100:
        spy = [spy1, spy2]
        break

for dwarf in dwarfs:
    if dwarf not in spy:
        print(dwarf)