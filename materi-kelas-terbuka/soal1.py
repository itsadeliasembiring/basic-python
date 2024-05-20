#Algoritma Menghitung Jumlah Harta Warisan
# Warisan Ibu = 1/6 Warisan
warisanIbu = 1/6

# Warisan Putra = 1/3 (x-warisan ibu) = 1/3 (1-0.25) = 1/3(0.75) = 0.25/putra
warisanPutra = 1/3*(1-warisanIbu)

# Total warisan ibu + putra = 6 miliar
warisanIbuPutra = 6000000000

# Menghitung jumlah warisan
totalWarisan = int(warisanIbuPutra/(warisanIbu+warisanPutra))
print("Total Warisan seluruhnya adalah Rp ", totalWarisan)