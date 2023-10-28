# len가 M이상인 문자에 대해서만 dict에 넣는데,
# 해당 문자가 dict에 존재하면 value += 1
# 해당 문자가 dict에 없으면 value = 1
# 이후 정렬을 3번 진행하는데, 순서는
# 그냥sort, len로 sort, value로 sort

n, m = map(int, input().split())
my_dict = {}

for _ in range(n):
    index = input()
    if(len(index) >= m):
        if(index not in my_dict):
            my_dict[index] = 1
        else:
            my_dict[index] += 1

my_dict = sorted(my_dict.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))
# x[0] = 단어, x[1] = 단어 빈도수
# -x[1] = 자주 나오는 단어 앞에 배치
# -len(x[0]) = 단어 길이 길수록 앞에 배치
# x[0] = 단어 사전 순 정렬

for i in my_dict:
    print(i[0])