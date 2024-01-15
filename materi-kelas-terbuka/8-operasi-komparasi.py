# Operasi komparasi -> untuk membandingkan nilai
# Hasilnya boolean -> true false
# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2
c = 3
d = 4
# Lebih besar dari
 
# >, <, >=, <=
print("a = ",a, " b = ",b, " dan ","c = ",c)
result  = a > c
print (a,"> c adalah ", result)
result  = a < c
print (a,"< c adalah ", result)
result  = b >= c
print (b,">= c adalah ", result)
result  = b <= c
print (b,"<= c adalah ", result)

# == &  != (== harus dua kalo = aja nnti jadi assignment/isi variabel)
result  = a == d
print (a,"= ",d, "adalah ", result)
result  = a == d
print (a,"!= ",d, "adalah ", result)

# Komparasi diatas bekerja pada syntax literal kek a > 4 nah yg literal itu yg 4 (gak  makan memori), tpi bisa juga ngebandingin dua variabel 
# Kalo is dan is not itu ngebandingin 2 variabel, ga bisa literal kek a > 4 tdi, 4nya harus masuk ke variabel b dulu

# IS sebagai komparasi object identity
x = 5
y = 5
print('nilai x = ', x,"id = ", hex(id(x)))
print('nilai y = ', y,"id = ", hex(id(y)))
# Klo tipe data valuenya sama, di python akan masukkan ke memori yg sama jadi efisien, gak kayak c c++ dll
result = x is y
print ("x is 5 adalah", result )

# ternyata jalan tapi ada tulisan kek "did u mean != ?"
result = x is not y
print ("x is not 5 adalah", result )

# fungsi is sama kek  ==, dan is not kek != bedanya yg is dan is not buat object/variabel