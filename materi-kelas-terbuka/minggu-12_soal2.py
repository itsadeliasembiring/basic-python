# Algoritma menyisipkan data ke-4 di posisi pertama dan data ke-5 di posisi tengah dengan ketentuan data ke-1, ke-2 dan ke-3 tetap terurut!

#  Deklarasi array
x = [0]*5

        
# Menginput angka
i=0
while i<5 :
    x[i] = int(input("Masukkan array X digit "+str(i+1)+"! "))
    i += 1

# Menukar data ke-4 ke data ke-1
awal = x[0]
x[0] = x[3]
x[3] = awal
        
# Menukar data ke-5 ke data ke-3
tengah = x[2]
x[2] = x[4]
x[4] = tengah
        
# Mengurutkan data ke-1,2,dan 3 (Data yang tidak ditukar) secara ascending
i = 1
while i <= 3 :
    if i == 1 or i == 3 or i == 4 :
        j = i + 2
        while j <= 4 :
            if j == 1 or j == 3 or j == 4 :
                if x[i] > x[j] :
                    simpan = x[j]
                    x[j] = x[i]
                    x[i] = simpan
            j += 2
    i += 2

        
# Menampilkan isi array 
i=0
print("Output : X = [ ")
while i<5 :
    print(x[i], end="")
    i += 1
print("]")