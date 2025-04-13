# 질문 : 입력된 이메일 주소가 유효한지 검사하세요. (조건: @와 . 포함)
#         (형식: "1990년 12월 12일")

def valid_email(email_address):
    # 조건: '@'와 '.'이 모두 포함되어야 한다
    if "@" in email_address and "." in email_address:
        # '@'는 맨 앞이나 맨 뒤에 오면 안됨
        at_index = email_address.find("@")
        dot_index = email_address.rfind(".")

        if 0 < at_index < dot_index < len(email_address) - 1:
            return True
    return False

# 예시
email = input(" 이메일 주소:")

if valid_email(email):
    print("유효함")
else:
    print("유효하지 않음")