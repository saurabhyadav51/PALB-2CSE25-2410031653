def factorial(n):
    result = [1]

    for i in range(2, n + 1):
        carry = 0
        for j in range(len(result)):
            temp = result[j] * i + carry
            result[j] = temp % 10
            carry = temp // 10

        while carry > 0:
            result.append(carry % 10)
            carry //= 10

    result.reverse()
    return result


print(factorial(5))
print(factorial(10))
print(factorial(1))