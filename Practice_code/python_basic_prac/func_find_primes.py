# 시작값, 끝값을 인자로 받아 그 사이의 소수를 리스트로 반환하는 find_primes 함수를 작성하세요.

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # 제곱근까지만 검사
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

result = find_primes(1, 20)
print("소수:",result)