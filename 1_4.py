'''
1.4 회문 순열
주어진 문자열이 회문(palindrome)의 순열인지 아닌지 확인하는 함수를 작성하라.
회문이란 앞으로 읽으나 뒤로 읽으나 같은 단어 혹은 구절을 의미하며, 순열이란 문자열을 재배치 하는 것을 뜻한다.
회문이 꼭 사전에 등장하는 단어로 제한될 필요는 없다.
'''

# 파이썬 딕셔너리를 이용해 등장 횟수 세기
# 회문순열인 경우 같은 문자의 개수가 전부 짝수 이거나 단 한 개만 홀수여야 한다.

str = input()
str = str.replace(' ', '')
str = str.lower()

cnt = 0

# 딕셔너리 생성
dic = {}
for i in range(len(str)):
    if(str[i] in dic):
        dic[str[i]] += 1
    else:
        dic.setdefault(str[i], 1)

result = list(dic.values())

# 문자열 길이가 홀수인 경우는 회문의 가운데에 중복 개수가 홀수인 문자 존재
if(len(str) % 2 == 0):
    cnt = 0
else:
    cnt = 1

# 딕셔너리의 values를 순차검색 후, 중복개수가 홀수인 경우 cnt를 깎음
for i in range(len(result)):
    if(cnt < 0):
        print(False)
        break
    if(result[i] % 2 == 1):
        cnt -= 1

if(cnt == 0):
    print(True)


'''
입력: Tact Coa
출력: True (순열: "taco cat", "atco cta" 등)

예제
1. A BC SDEEG FSA - False
2. Tact Coa - True
'''
