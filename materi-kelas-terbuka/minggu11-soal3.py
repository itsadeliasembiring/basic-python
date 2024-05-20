#Algoritma untuk menentukan jumlah bilangan yang meningkat dari besar ke kecil secara berurutan(decrease) terpanjang 
#  Assign value array
bilangan = [0] * 20
panjangUrutan = [0] * 20
urutanBilangan = [""] * 20
# Assign value variabel
j = 0
panjangBilangan = 0
        
# User menginput bilangan
for i in range(20):
    bilangan[i] = int(input("Masukkan bilangan ke-"+str(i+1)+"! "))
   
# Mengecek bilangan yang berurut dari terbesar ke terkecil (Decrease)
# Membatasi hingga index 18, agar saat i = 19 tidak mengecek dengan i=20 yang melebihi panjang array
for i in range(19):
    if bilangan[i]>bilangan[i+1] :
        panjangUrutan[j] = panjangUrutan[j]+1
        urutanBilangan[j] = urutanBilangan[j]+str(bilangan[i])
    else :
        urutanBilangan[j] = urutanBilangan[j]+str(bilangan[i])
        j = j+1

# Menentukan urutan angka terpanjang
for i in range(j+1):
    if panjangBilangan < panjangUrutan[i] :
        panjangBilangan = panjangUrutan[i]
        
# Menampilkan angka yang berurutan terpanjang
for i in range(j+1):
    if panjangBilangan == panjangUrutan[i] :
        print(urutanBilangan[i], "(", len(urutanBilangan[i]), ")")
