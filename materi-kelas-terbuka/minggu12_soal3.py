#  Deklarasi variabel & array, sumDeret
angka = [0] * 20
sumDeret = [0] * 20
deret = [""] * 20

# User menginput 20 digit angka
i=0
while i<20 :
    angka[i] = int(input("Masukkan bilangan ke- "+str(i+1)+"! "))
    i+=1

# Meng-assign setiap nilai array
i=0
while i<20 :
    deret[i] = ""
    sumDeret[i] = 0
    i+=1

# Menentukan setiap bilangan yang berderet secara ascending
i=0
k=0
while i<19 :
    if angka[i]<=angka[i+1] :
        # Mengassign setiap deret ke array deret di index yang sama
        deret[k]=deret[k]+str(angka[i])  
        # Menjumlah setiap deret ke dalam array deret di index yang sama
        sumDeret[k]=sumDeret[k]+angka[i]
    else :
        # Mengassign deret terakhir ke index yang sama Semisal 8895 maka 88 di asign di true, dan 9 deret terakhir di assign di false
        deret[k]=deret[k]+str(angka[i])  
        # Menjumlah setiap deret ke dalam array deret di index yang sama
        sumDeret[k]=sumDeret[k]+angka[i]

        # Membuat index baru untuk mengassign deret yang baru
        k+=1
    i+=1

        
# Menentukan jumlah deret terbesar
i=0
maximum=0
while i<(k+1) :
    if maximum < sumDeret[i] :
        maximum=sumDeret[i]
    i+=1

# Menampilkan angka deret yang jumlah deretnya terbesar
i=0
print("[ ")
while i<k+1 :
    if maximum == sumDeret[i] :
        print(f"{deret[i]} karena {int(deret[i][0])} + {int(deret[i][1])} + {int(deret[i][2])} = {maximum}")
        print(f"{maximum} adalah jumlah angka berurutan terbesar")
    i+=1
