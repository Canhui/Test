def find_primitive_roots(n):
    c, p = phi(n)
    pr = []
    for a in c:
        s = set([a**i % n for i in range(1, p+1)])
        if len(s) == p:
            pr.append(a)
    return pr

def phi(n): # Euler Totient
    congruence_class = [i for i in range(1, n) if gcd(i, n) == 1]
    print("hi phi")
    return congruence_class, len(congruence_class)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
n = 14
# φ(n) = 6, (Z/14Z)X = {1, 3, 5, 9, 11, 13}

#print(find_primitive_roots(n))
#  a  a^2  a^3  a^4 a^5 a^6     (mod n)
#[ 1,   1,   1,   1,  1,  1]
#[ 3,   9,  13,  11,  5,  1]
#[ 5,  11,  13,   9,  3,  1]
#[ 9,  11,   1,   9, 11,  1]
#[11,   9,   1,  11,  9,  1]
#[13,   1,  13,   1, 13,  1]

#[3, 5] # since a = 3, 5 generates (Z/14Z)X

# ------------------------------------------------------

def find_discrete_log(a, n, y):
    _, p = phi(n)
    # first check existence
    if a in find_primitive_roots(n):
        print("a=", a)
        for b in range(1, p):
            print("b=", b)
            if a**b % n == y:
                return b
    return None

# print(find_discrete_log(2, 11, 9)) # 2^6 mod 11 = 9, find_discrete_log(2, 11, 9) => 6
# 6  # 2 is a primitive root of 11 
     # and 9 ≡ 2^6 (mod 11) =>
     # dlog_{2, 11} 9 = 6

print(find_discrete_log(100001, 70606432933607, 67385023448517)) # find b => 54696545758787
# a = 100001
# b = 54696545758787
# p = 70606432933607
# a^b mod p = 67385023448517
