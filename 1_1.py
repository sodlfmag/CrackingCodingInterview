'''
1.1 중복이 없는가?
문자열이 주어졌을 때, 이 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘을 작성하라.
자료구조를 추가로 사용하지 않고 풀 수 있는 알고리즘 또한 고민하라.
'''

str = 'ABAACEDEDCE'
str = 'ABCDE'
# 내장 메서드 사용
# --> 개별 문자열 분리 - 리스트 저장 후 set으로 중복 삭제 -> 길이 비교
temp = set(list(str))
if(len(str) != len(temp)):
    print("중복된 문자가 있습니다.")

# 순차비교를 통한 중복 찾기
temp = []
for chr in str:
    if(chr in temp):
        print("중복된 문자가 있습니다.")
        break
    temp.append(chr)
