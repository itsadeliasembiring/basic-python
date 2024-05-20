#Algoritma Mencari Nilai K Dari N (Mean) Yang Di Input Oleh User
#Input rata-rata bilangan (n) 
n = int(input("Masukkan Angka N minimal 7! "))

#Total bilangan seharusnya
totalBilangan = 4 * n

#Mengecek input agar n tidak boleh negatif (n<0) dan k tidak boleh negatif (n<6+9+11)
while n < 0 or totalBilangan < 26: 
    n = int(input("Masukkan Angka N minimal 7!"))
    totalBilangan = 4 * n

#Total sementara
bilangan = 6 + 9 + 11

#k = total seharusnya - total sementara
k = totalBilangan - bilangan
print("Nilai K adalah : ", k)