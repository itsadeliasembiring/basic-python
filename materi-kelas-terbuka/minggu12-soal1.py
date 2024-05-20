# Algoritma menggabungkan data array x dan y ke dalam array baru berukuran 11 data dengan ketentuan nilai-nilai array kedua disisipkan ke array pertama
#  Declare array
x = [0] * 6
y = [0] * 5
z = [0] * 11

# Input array x
i=0
while i<6 :
    x[i] = int(input("Masukkan array X digit "+str(i+1)+"! "))
    i += 1

    
# Input array y
i=0
while i<5 :
    y[i] = int(input("Masukkan array Y digit "+str(i+1)+"! "))
    i += 1


# Menggabungkan array X dan Y ke dalam array Z
i=0
dx=0
dy=0
while i<11 :
    if i%2==0 :
        z[i] = x[dx]
        dx=dx+1
    else:
        z[i] = y[dy]
        dy=dy+1
    i += 1

# Output array gabungan        
i=0
print("Array gabungan Z = [ ", end="")
while i<11 :
    print(z[i], end=" ")
    i += 1
print("]")