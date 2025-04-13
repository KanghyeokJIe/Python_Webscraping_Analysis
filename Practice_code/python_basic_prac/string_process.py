# 질문: "Hello"와 "World"를 연결하여 "Hello World"를 출력하세요.
#              대문자로 변환하세요.
#             "Hello World"에서 "World"만 슬라이싱하여 출력하세요.
#              "Python is fun"에서 공백을 기준으로 문자열을 분리하세요.
#              "abcdef"에서 짝수 인덱스(0, 2, 4)의 문자들만 출력하세요.
#             "Hello"를 3번 반복하여 출력하세요.


a = 'Hello'
b = 'World'
c = a + b
d = 'Python is fun'
e = 'abcdef'

print (a + ' ' + b)
print(a.upper()+' '+b.upper())
print(c[5:10])
print(d.split(' '))
print(e[::2])
print(a*3)