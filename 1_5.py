'''
1.5 하나 빼기
문자열을 편집하는 방법에는 세 가지 종류가 있다. 문자 삽입, 문자 삭제, 문자교체.
문자열 두 개가 주어졌을 때, 문자열을 같게 만들기 위한 편집 횟수가 1회 이내인지 확인하는 함수를 작성하라.
'''

# 문자 삽입, 삭제는 같은 비교방법이다.
# 문자열 슬라이싱을 이용한다.

str1 = input()
str2 = input()


def validate(a, b):
    length = min(len(a), len(b))
    cnt = 0
    diff = abs(len(a) - len(b))

    if(diff > 1):
        return False

    for i in range(length):
        if(a[i] != b[i]):
            cnt += 1

    if(cnt + diff > 1):
        return False

    return True


print(validate(str1, str2))

# pale
# ple
