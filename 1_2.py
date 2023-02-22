'''
1.2 순열 확인
문자열 두 개가 주어졌을 때 이 둘이 서로 순열관계에 있는지 확인하는 메서드를 작성하라.
'''
# 순열관계에 있는 두 문자열 a,b
a = 'ABABCDCDE'
b = 'DDCCBAEBA'
c = 'ABCDE'

# 각 문자 리스트화 후 정렬, 리스트 비교


def check_permutation(str1, str2):
    temp1 = list(str1)
    temp2 = list(str2)
    temp1.sort()
    temp2.sort()

    # s1 = ''.join(temp1)
    # s2 = ''.join(temp2)
    if(temp1 == temp2):
        print("두 문자열은 순열 관계입니다.")

    else:
        print("두 문자열은 순열 관계가 아닙니다.")


check_permutation(a, b)
check_permutation(a, c)
