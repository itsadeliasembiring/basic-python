# Algoritma Menentukan Waktu Kedatangan Bus
# Deklarasi variabel

# Input waktu jam keberangkatan
jam1 = int(input("Masukkan Jam Keberangkatan Bus!"))
while jam1 < 0 or jam1 > 23 :
    jam1 = int(input("Masukkan Jam Keberangkatan Bus!"))

# Input waktu menit keberangkatan
menit1 = int(input("Masukkan Menit Keberangkatan Bus!"))
while menit1 < 0 or menit1 > 59:
    menit1 = int(input("Masukkan Menit Keberangkatan Bus!"))

# Input jarak
s = int(input("Masukkan Jarak Lokasi!"))

# Input kecepatan
v = int(input("Masukkan Kecepatan Bus!"))

# Waktu istirahat   
istirahat = 45

# Waktu tempuh 
t2 = (s/v) * 60 + istirahat
jam2 = t2 / 60
menit2 = t2 % 60

# Menghitung waktu kedatangan bus  
waktuJam = jam1 + jam2
waktuMenit = menit1 + menit2
if waktuMenit > 60 :
    waktuJam = waktuJam + 1
    waktuMenit = waktuMenit - 60

print("Bus Tiba Pada Pukul ", waktuJam, ".", waktuMenit);
