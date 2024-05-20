# Algoritma Menghitung Persentase Kenaikan Harga Jual Minyak Goreng

# Input persentase ongkos kirim
persentaseOngkir = int(input("Masukkan persentase ongkos kirim : "))

# Harga beli minyak
hargaBeli=15000
# Keuntungan   
keuntungan=2500

# Menghitung ongkos kirim   
ongkosKirim=int((persentaseOngkir/100)*hargaBeli)

# Menghitung harga jual dengan mengambil keuntungan Rp 2500
hargaJual= ongkosKirim + hargaBeli + keuntungan

# Menghitung persentase kenaikan harga jual 
persentaseKenaikan=((hargaJual - hargaBeli) / hargaBeli) * 100
print("Kenaikan Harga Jual Minyak dari Harga Beli sebanyak ",persentaseKenaikan," %");