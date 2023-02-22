'''
1.6 문자열 압축
반복되는 문자의 개수를 세는 방식의 기본적인 문자열 압축 메서드를 작성하라.
예를 들어 문자열 aabccccaaa를 압축하면 a2b1c5a3이 된다.
만약 '압축된' 문자열의 길이가 기존 문자열의 길이보다 길다면 기존 문자열을 반환해야 한다.
문자열은 대소문자 알파벳(a~z)으로만 이루어져 있다.
'''


def compress_string(str):
    key = str[0]
    cnt = 0
    temp = []
    for i in range(len(str)):
        if(str[i] == key):
            cnt += 1
        else:
            temp.append((key, cnt))
            key = str[i]
            cnt = 1
    temp.append((key, cnt))

    if(len(temp) * 2 > len(str)):
        return str
    else:
        for i in range(len(temp)):
            print(temp[i][0], temp[i][1], sep='', end='')
        print()


compress_string('aabcccccaaa')
