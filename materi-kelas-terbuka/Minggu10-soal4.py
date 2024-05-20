# Algoritma Menghitung Sudut Terbesar (satuan radian) Jam
# Input Jam
jam = int(input("Input jam = "))

# Input Menit
menit = int(input("Input menit = "))

# Menghitung Sudut Jam
sudutJam = (jam*30)+(menit*0.5)

# Menghitung Sudut Menit
sudutMenit = menit*6

# Sudut total
sudutTotal = abs(sudutJam-sudutMenit)

# Menghitung sudut terbesar dan sudut terkecil       
if sudutTotal > 180 :
    sudutTerkecil = 360-sudutTotal
    sudutTerbesar = sudutTotal
    print("Sudut Terkecil ", sudutTerkecil)
    print("Sudut Terbesar ", sudutTerbesar)
else :
    sudutTerkecil = sudutTotal
    sudutTerbesar = 360-sudutTotal
    print("Sudut Terkecil ", sudutTerkecil)
    print("Sudut Terbesar ", sudutTerbesar)

#  Konversi ke dalam Radian
radian = sudutTerbesar/180
print("Sebesar ", radian, " radian")