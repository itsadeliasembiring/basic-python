# Operasi yg bisa dilkukan dengan penyingkatan
a = 5 # ini adalah assignment
print("nilai a = ", a)
#  a = a + 1 bisa disingkat jadi a+= 1
a += 1
print("nilai a + 1 = ", a)

a -= 2 # iki maksudnya a = a-2
print("nilai a - 2 = ", a)

a *= 5 
print("nilai a * 2 = ", a)

a /= 2 
print("nilai a / 2 = ", a)

# modulus
b=10
print("Nilai b = ",b )
b %= 3
print("Nilai modulus 3 adalah ", b)

b=10
# Floor division
b //= 3
print("Nilai floor division 2 adalah ", b)

a = 5
print("Nilai a =",a)
# pangkat
a **= 3
print("5 pangkat 3 adalah ",a)

# Operasi bitwise
c = True
print("\n nilai c =",c)
c != False
print("\n nilai c != false, maka c menjadi",c)
c = False
print("\n nilai c =",c)
c != False
print("\n nilai c != false, maka c menjadi",c)

# AND
c = True
print("\n nilai c =",c)
c &= False
print("\n nilai c &= false, maka c menjadi",c)
c = True
print("\n nilai c =",c)
c &= True
print("\n nilai c &= true, maka c menjadi",c)

# XOR
c = True
print("\n nilai c =",c)
c ^= False
print("\n nilai c ^= false, maka c menjadi",c)
c = True
print("\n nilai c =",c)
c ^= True
print("\n nilai c ^= true, maka c menjadi",c)