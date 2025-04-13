# 질문: "Python is awesome"에서 모음(a, e, i, o, u)의 개수를 세세요.

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

text = 'Python is awesome'
print("모음 개수 :",count_vowels(text))