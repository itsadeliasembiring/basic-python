# Algoritma Menentukan Tarif Perjalanan MyJeg

# Input Jarak Tempuh
jarakTempuh = float(input("Masukkan Jarak Tempuh: "))

# Input Waktu Tempuh
waktuTempuh = float(input("Masukkan Waktu Tempuh: "))

# Input Keadaan Cuaca
keadaanCuaca = str(input("Masukkan keadaan cuaca! (Terang/Hujan) : "))
keadaanCuaca = keadaanCuaca.lower()

# Tarif minimal  
tarifMinimal = 10000
        
# Tarif Jarak Tambahan
tarifJarakTambahan = 50
        
# Tarif Waktu Tambahan
tarifWaktuTambahan = 1000
       
# Standar Waktu
standarWaktu = jarakTempuh*2.5
        
# Menentukan Tarif jarak tempuh
if jarakTempuh > 3 :
    totalTarif = tarifMinimal+2000
    #Apabila > 3km maka km pertama dikenakan tarif Rp.2000,- (4km)
    if jarakTempuh > 4 :
        # Tarif km selanjutnya Rp.50,-/km => (selisih*50)+totalTarif
        totalTarif = (int)((jarakTempuh - 4) * tarifJarakTambahan) + totalTarif
else : #Apabila 0 hingga 3km maka tarifnya Rp.10.000,-
    totalTarif = tarifMinimal

        
# Menentukan Tarif Waktu
if waktuTempuh > standarWaktu :
    # Apabila dalam perjalanan melebihi waktu standar dikenakan biaya jam sibuk dengan ketentuan tarif Rp. 1.000,- per menit dari kelebihan waktunya 
    # (selisih*1000)+totalTarif
    totalTarif = ((waktuTempuh - standarWaktu) * tarifWaktuTambahan) + totalTarif

# Tarif keadaaan cuaca
if keadaanCuaca == "hujan" :
    totalTarif = totalTarif+(totalTarif*0.15)

totalTarif = int(totalTarif)

# Output Total Tarif        
print("Total Tarif yaitu : Rp. ",totalTarif,",-")   