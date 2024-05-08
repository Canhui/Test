def log2(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    result = 0
    while n > 1:
        n //= 2
        result += 1

    return result

n = int(input("Please input a postive integer n："))
result = log2(n)
print("log2({}) = {}".format(n, result))
