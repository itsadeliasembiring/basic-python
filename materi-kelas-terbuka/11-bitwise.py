# bit wise -> operasi masing masing bit/biner
# int 1=>0 0 0 0 0 0 0 1= 2^0 = 1
# kalo biasa pake or, di bitwise |
# Agak gak paham

# Bit wise OR (|)
a = 9
b = 5
c = a | b
print("nilai : ", a, " , binary :", format(a,"08b"))
print("nilai : ", b, " , binary :", format(b,"08b"))
print("nilai BIT WISE : ", c, " , binary :", format(c,"08b"))

# Bit wise AND (&)
c = a & b
print("nilai : ", a, " , binary :", format(a,"08b"))
print("nilai : ", b, " , binary :", format(b,"08b"))
print("nilai BIT WISE : ", c, " , binary :", format(c,"08b"))

# Bit wise XOR (^)
c = a ^ b
print("nilai : ", a, " , binary :", format(a,"08b"))
print("nilai : ", b, " , binary :", format(b,"08b"))
print("nilai BIT WISE : ", c, " , binary :", format(c,"08b"))

# Bit wise NOT (~)
# Misal nilai a 9 di mirror jadi -10
c = ~ a 
print("nilai : ", a, " , binary :", format(a,"08b"))
print("nilai BIT WISE : ", c, " , binary :", format(c,"08b"))
#  mirror lagi pake xor
d = 0b0000001001
e = 0b1111111111
print("Nilai : ", e^d, ', binary : ', format(e^d,"08b"))

# shifting
# shift right (>>) Geser kanan
c = a >> 2
print("nilai : ", a, " , binary :", format(a,"08b"))
print("nilai BIT WISE : ", c, " , binary :", format(c,"08b"))

# shift left (<<) Geser kiri
c = a << 2
print("nilai : ", a, " , binary :", format(a,"08b"))
print("nilai BIT WISE : ", c, " , binary :", format(c,"08b"))