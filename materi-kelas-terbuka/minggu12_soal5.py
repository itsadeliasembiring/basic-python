# Algoritma menampilkan p angka segitiga dan menentukan apakah sebuah bilangan yang di input user merupakan angka segitiga atau bukan
        
# Input jumlah deret (p)
p=int(input("Masukkan jumlah deret (p) : "))

# Input angka yang ingin di cek
cekAngka=int(input("Masukkan angka yang ingin di cek dalam pola segitiga : "))

# Membuat deret segitiga
angkaDeret = [0]*p
i=0
deret=1
while i<p :
    angkaDeret[i]=int(deret*(deret+1)/2)
    deret+=1
    i+=1

# Menampilkan deret segitiga
i=0
print(p,"angka segitiga pertama adalah: ",end="")
while i<p :
    if i!=p-1 :
        print(angkaDeret[i],end=",")
    else:
        print(angkaDeret[i])
    i+=1
        
# Mengecek apakah angka yang ingin di cek oleh user merupakan angka segitiga atau bukan
i=0
jmlTrue=0
while i<p :
    if cekAngka==angkaDeret[i] :
        print(cekAngka,"adalah angka segitiga")
        jmlTrue=1
    elif i == p-1 and jmlTrue == 0 :
        print(cekAngka,"bukan angka segitiga")
    i+=1