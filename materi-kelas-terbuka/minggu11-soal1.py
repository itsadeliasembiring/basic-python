# Algoritma untuk menghitung berat masing-masing 3 bebek yang hilang, serta standar deviasi dari populasi bebek Pak Budi
import math

# Declare array beratBebek
beratBebek = [0] * 10

#  Input Rata-rata berat bebek
meanBebek = float(input("Masukkan Rata-rata berat bebek! "))

#  total seharusnya berat bebek
totalSeharusnya = meanBebek*10
totalSementara = 0
        
#  Input berat 7 bebek
for i in range(0,6):
    beratBebek[i] = float(input("Masukkan Berat Bebek "+str(i + 1)+"! "))
    totalSementara = totalSementara+beratBebek[i]

        
# Mencari total berat 3 bebek
beratBebekHilang = totalSeharusnya-totalSementara
        
# Mencari masing-masing berat 3 bebek
beratBebek[7] = (1/3.75)*beratBebekHilang   
beratBebek[8] = (1.25/3.75)*beratBebekHilang
beratBebek[9] = (1.50/3.75)*beratBebekHilang
        
# Menghitung Varians
totalSimpangan = 0
for i in range(10):
    simpangan = pow((beratBebek[i]-meanBebek), 2)
    totalSimpangan = totalSimpangan+simpangan

varians = totalSimpangan/10
        
# Menghitung standar deviasi
standarDeviasi = math.sqrt(varians)
        
# Menampilkan berat bebek dan standar deviasi
print("Berat Bebek 1 : ",beratBebek[7]," Kg")
print("Berat Bebek 2 : ",beratBebek[8]," Kg")
print("Berat Bebek 3 : ",beratBebek[9]," Kg")
        
print("Standar Deviasi : ",standarDeviasi," Kg")