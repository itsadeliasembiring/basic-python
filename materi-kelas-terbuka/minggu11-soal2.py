# Algoritma untuk menghitung jumlah mahasiswa yang masuk setiap kategori, bila nilai angka dari mahasiswa di-input-kan oleh user
# Declare & init array
nilaiMahasiswa = [0] * 15
# init variabel
a = ab = b = bc = c = d = e = 0
        
# Input nilai 15 mahasiswa   
for i in range(15):
    nilaiMahasiswa[i] = float(input("Masukkan nilai mahasiswa "+str(i+1)+"! "))
        
# Menentukan kategori nilai mahasiswa
for i in range(15):
    if nilaiMahasiswa[i]>=86 and nilaiMahasiswa[i]<=100 :
        a=a+1
    elif nilaiMahasiswa[i]>=78 and nilaiMahasiswa[i]<=85.9 :
        ab=ab+1
    elif nilaiMahasiswa[i]>=70 and nilaiMahasiswa[i]<=77.9 :
        b=b+1
    elif nilaiMahasiswa[i]>=62 and nilaiMahasiswa[i]<=69.9 :
        bc=bc+1
    elif nilaiMahasiswa[i]>=54 and nilaiMahasiswa[i]<=61.9 :
        c=c+1
    elif nilaiMahasiswa[i]>=40 and nilaiMahasiswa[i]<=53.99 :
        d=d+1
    elif nilaiMahasiswa[i]>=0 and nilaiMahasiswa[i]<=39.99 :
        e=e+1

# Menampilkan jumlah mahasiswa setiap kategori nilai 
print("Jumlah Mahasiswa Yang Mendapat Nilai A : ",a)
print("Jumlah Mahasiswa Yang Mendapat Nilai AB : ",ab)
print("Jumlah Mahasiswa Yang Mendapat Nilai B : ",b)
print("Jumlah Mahasiswa Yang Mendapat Nilai BC : ",bc)
print("Jumlah Mahasiswa Yang Mendapat Nilai C : ",c)
print("Jumlah Mahasiswa Yang Mendapat Nilai D : ",d)
print("Jumlah Mahasiswa Yang Mendapat Nilai E : ",e)   