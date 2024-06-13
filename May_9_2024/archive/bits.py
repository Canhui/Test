import math

decimal_number = 54696545758787

# calculate the number of bits for the decimal number
bit_length = math.ceil(math.log2(decimal_number + 1))

print("the number of bits:", bit_length)
