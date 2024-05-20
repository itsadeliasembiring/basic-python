#Mengurutkan angka dari terbesar-terkecil
from math import fabs
bil = [0] * 20
for i in range(20):
    bil[i] = int(input())
terpanjang = 0
cekPanjang = 0
for i in range(1,20):
    if bil[i] < bil[i - 1]:
        terpanjang += 1
        posisi = i
    else:
        if terpanjang > cekPanjang:
            cekPanjang = terpanjang
            cekPosisi = posisi
        terpanjang = 0
if cekPosisi == 19:
    cekPanjang = terpanjang
    cekPosisi = posisi + 1
posisiAwal = abs(cekPanjang - cekPosisi)
type(posisiAwal)
type(cekPosisi)

for i in range(posisiAwal, cekPosisi + 1):
    print(str(bil[i]) + " ", end='', flush=True)
cekPanjang += 1
print("(" + str(cekPanjang) + ")", end='', flush=True)
