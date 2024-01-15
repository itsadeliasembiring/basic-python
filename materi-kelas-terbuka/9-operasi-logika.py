# Operasi logika/boolean/tabel kebenaran
# not, or, and, xor

# NOT (selalu ke balikan)
a = True
c = not a
print ("LOGIKA NOT (selalu ke balikan)")
print ("data a = ", a)
print ("Dalam logika NOT jadi ", c)

# OR (kalo salah satu ada true auto true)
print ("LOGIKA OR (kalo salah satu ada true auto true)")
a = True
b = False
c = a or b
print (a, 'OR', b, "=", c)
a = True
b = True
c = a or b
print (a, 'OR', b, "=", c)
a = False
b = False
c = a or b
print (a, 'OR', b, "=", c)

# AND (dua duanya harus true)
print ("LOGIKA AND (dua duanya harus true)")
a = True
b = False
c = a and b
print (a, 'AND', b, "=", c)
a = True
b = True
c = a and b
print (a, 'AND', b, "=", c)
a = False
b = False
c = a and b
print (a, 'AND', b, "=", c)

# XOR pake tanda ^ (dua duanya harus true)
# Operator bitwise mempunyai arti operasi matematika dengan mengoperasikan nilai dalam bilangan biner (0 dan 1).
print ("LOGIKA XOR (akan true jika salah satu aja, kalo dua true jadi false)")
a = True
b = False
c = a ^ b
print (a, 'XOR', b, "=", c)
a = True
b = True
c = a ^ b
print (a, 'XOR', b, "=", c)
a = False
b = False
c = a ^ b
print (a, 'XOR', b, "=", c)