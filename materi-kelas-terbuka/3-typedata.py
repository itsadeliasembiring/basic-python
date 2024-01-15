"""
tipe data = > jenis data dari valuenya yg kita masukin ke variable
"""

# Dia langsung, ga kek bahasa lain yg harus deklarasi tipe data kek char nama_variable
# Cara cek tipe datanya => type(nama_variabel)

# integer (angka bulet)
this_integer = 90
print("data : ", this_integer)
print("tipenya", type(this_integer))\

# float (angka pake koma)
this_float = 1.1
print("data : ", this_float)
print("tipe: ", type(this_float))

# string (karakter or huruf)
this_string = "adele cancik 123"
print("isinya : ", this_string)
print("tipe: ", type(this_string))

#boolean (true or false) biner 0 and 1
this_boolean = True
print("isinya : ", this_boolean)
print("tipe: ", type(this_boolean))


#tipe data khusus
#bilangan kompleks (imajiner)
thisComplex = complex(5,6)
print("isinya : ", thisComplex)
print("tipe: ", type(thisComplex))

#tipe data bahasa C  kek double, long, dll
from ctypes import c_double
data_c_double = c_double(1111)
print("data : ", data_c_double)
print("tipenya : ", type(data_c_double))