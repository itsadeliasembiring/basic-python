# Algoritma Menentukan Koordinat Titik Potong Grafik 
import math   
#Input y1   
print("Input y1")
a = float(input("ax^2 = "))
b = float(input("bx = "))
c = float(input("c = "))

#Input y2
print("Input y2")
d = float(input("ax^2 = "))
e = float(input("bx = "))
f = float(input("c = "))
        

print("y1 = ",a,"x^2 + ",b,"x + ",c)
print("y2 = ",d,"x^2 + ",e,"x + ",f)
        
# Persamaan Kuadrat y1-y2=0
nilaiA = a-d
nilaiB = b-e
nilaiC = c-f
        
# Mencari Diskriminan
diskriminan = pow(nilaiB, 2)-(4*(nilaiA*nilaiC))

# Persamaan Kuadrat
print("Persamaan Kuadrat = ",int(nilaiA),"x^2 + ",int(nilaiB),"x ","+",int(nilaiC))
        
# Menentukan titik potong berdasarkan diskriminan
if diskriminan>0 :
    # Menggunakan rumus ABC untuk menentukan 2 titik potong
    x1 = (-nilaiB + math.sqrt(diskriminan)) / (2*nilaiA)
    x2 = (-nilaiB + math.sqrt(diskriminan)) / (2*nilaiA)
    y1 = d*pow(x1, 2)+(e*x1)+f
    y2 = d*pow(x2, 2)+(e*x2)+f
    print("Kedua grafik tersebut saling memotong di titik (",int(x1),",",int(y1)," dan (",int(x2),",",int(y2)+")")
elif diskriminan == 0 :
    # Menentukan 1 titik potong
    x1 =  -nilaiB/(2*a)
    y1 =  pow(a*x1, 2) + (b*x1) + c
            
    # Menampilkan koordinat
    print("Kedua grafik tersebut saling bersinggungan di titik ", "(", int(x1), ",", int(y1), ")")
else :
    print("Kedua grafik tersebut saling lepas!")
