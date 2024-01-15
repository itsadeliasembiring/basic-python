"""
Operasi Aritmatika :
+ - * /
"""
a = 2
b = 2
result = a+b
print (a, "+", b, "=", result)

result = a-b
print (a, "-", b, "=", result)

result = a*b
print (a, "*", b, "=", result)

result = b/a
print (b, "/", a, "=", result)

# Pangkat **
result = b**a
print (b, "pangkat", a, "=", result)

# Modulus => sisa bagi (%)
# Misal 10/3 = 9-10=sisa 1
a=3
b=10
result = b%a
print (b, "dan", a, "modulusnya", result)

#floor division (kek modulus tpi dibuletin kebawah) //
result = b//a
print (b, "dan", a, "floor divisonnya", result)

# Prioritas Operasi
""" 
(kurunk) -> pangkat/eksponent -> perkalian/pembagian -> modulus/floor -> Pertambahan/Pengurangan

"""

