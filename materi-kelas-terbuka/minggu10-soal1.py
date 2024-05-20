# Algoritma menentukan panjang garis singgung persekutuan luar dari kedua lingkaran
import math   
#  Input x1
x1 = float(input("Masukkan x1 : "))
#  Input y1
y1 = float(input("Masukkan y1 : "))  
#  Input r1
r1 = float(input("Masukkan r1 : "))
        
#  Input x2
x2 = float(input("Masukkan x2 : "))
        
#  Input y2
y2 = float(input("Masukkan y2 : "))
        
#  Input r2
r2 = float(input("Masukkan r2 : "))
        
jarakPusat = abs(math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))
print(jarakPusat)
panjang = pow( jarakPusat, 2) - pow(r1 - r2, 2)
        
if panjang <= 0 :
    print("Kedua lingkaran ini tidak memiliki garis singgung")
else :
    panjang = math.sqrt(panjang)
    print("Panjang garis singgung persekutuan luar : ",panjang)