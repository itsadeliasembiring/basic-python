# Algoritma untuk menentukan apakah suatu tanggal yang di-input oleh user POLINDROME atau bukan
#  Deklarasi variabel & array      
bulanAngka = ""
fullDate = [0]*8
# Data 12 nama bulan ke array namaBulan
namaBulan = [
    "januari",
    "februari",
    "maret",
    "april",
    "mei",
    "juni",
    "juli",
    "agustus",
    "september",
    "oktober",
    "november",
    "desember"
]
        
# Input tanggal
date = str(input("Masukkan Tanggal : "))
dateInt = int(date)

while dateInt>31 :
    print("Masukkan Tanggal : (Tidak boleh lebih dari 31!) ")
    date = str(input("Masukkan Tanggal : "))
    dateInt = int(date)
        
# Input bulan
month = str(input("Masukkan Bulan (Contoh: januari) : ")).lower()
        
# Input tahun
year = str(input("Masukkan Tahun : "))
       
# Mengubah nama bulan yang di input user menjadi bulan numerik
for i in range (12) :
    if namaBulan[i]==month :
        if i<9 :
            bulanAngka = "0"+str(i+1)
        else :
            bulanAngka = ""+str(i+1)

print("adalah", bulanAngka)
# Memasukkan satu persatu nilai tanggal, bulan dan tahun ke array fullDate (8 digit)
for i in range (2) :
    fullDate[i] =  int(date[i])

for i in range (2) :
    fullDate[i+2] =  int(bulanAngka[i])

for i in range (4) :
    fullDate[i+4] =  int(year[i])

# Mengecek apakah array full date polindrome atau tidak
digitTrue=0
i2=7
for i in range(8) :
# Membandingkan index depan dan belakang, apabila nilai sama maka digit true bertambah 1
    if fullDate[i]==fullDate[i2] :
        digitTrue = digitTrue+1
    i2=i2-1

# Jika jumlah true = 8 maka polindrome
if digitTrue==8 :
    print("Tanggal ",date,"-",bulanAngka,"-",year," merupakan angka POLINDROME")
else :
    print("Tanggal ",date,"-",bulanAngka,"-",year," BUKAN angka POLINDROME")