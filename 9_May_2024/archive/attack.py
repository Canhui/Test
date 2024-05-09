def discrete_log(a, p, c):
    b = 1
    base = a % p

    while base != c:
        base = (base * a) % p
        b += 1
        print("Trying b = ", b)

        if b > p:
            return None  # cannot find solution b

    return b

a = 100001 # 2  
p = 70606432933607 # 11
c = 67385023448517 # 9

result = discrete_log(a, p, c)

if result is None:
    print("cannot find solution b")
else:
    print("Find solution b:", result)

# a^b mod p = c
# 2^6 mod 11 = 9
# 100001 ^ 54696545758787 (mod 70606432933607) = 67385023448517
