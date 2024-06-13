import math 

# Function
# Ref: https://stackoverflow.com/questions/1832617/calculate-discrete-logarithm
def baby_steps_giant_steps(a,b,p,N = None):
    if not N: N = 1 + int(math.sqrt(p))

    #initialize baby_steps table
    baby_steps = {}
    baby_step = 1
    for r in range(N+1):
        baby_steps[baby_step] = r
        baby_step = baby_step * a % p

    #now take the giant steps
    giant_stride = pow(a,(p-2)*N,p)
    giant_step = b
    for q in range(N+1):
        if giant_step in baby_steps:
            return q*N + baby_steps[giant_step]
        else:
            giant_step = giant_step * giant_stride % p
    return "No Match"

p = 70606432933607
a = 100001
b = 54696545758787

print(baby_steps_giant_steps(a,67385023448517,p))
