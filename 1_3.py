'''
1.3 URL화
문자열에 들어 있는 모든 공백을 '%20' 으로 바꿔주는 메서드를 작성하라.
최종적으로 모든 문자를 다 담을 수 있을 만큼 충분한 공간이 확보되어 있으며 문자열의 최종 길이가 함께 주어진다고 가정해도 된다.
(자바로 구현한다면 배열 안에서 작업할 수 있도록 문자배열(character array)을 이용하기 바란다.)
'''
# join 메서드를 이용한 구현
str = input()
length = int(input())

temp = list(str.split())
result = '%20'.join(temp)

print(result)


'''
입력: "Mr John Smith", 13
출력: "Mr%20John%20Smith"
'''
