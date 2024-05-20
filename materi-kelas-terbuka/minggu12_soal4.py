fibonacci = [0]*10
       
# Input angka       
i=0
while i<2 :
    fibonacci[i] = int(input("Masukkan angka ke- "+str(i+1)+"! "))
    while fibonacci[i] < 0 :
        fibonacci[i] = int(input("Masukkan angka ke- "+str(i+1)+" (Tidak boleh negatif!) "))
    i+=1
       
# Menentukan angka fibonacci kemudian hasilnya di assign ke dalam array fibonacci
i=2
while i<10 :
    fibonacci[i]=fibonacci[i-2]+fibonacci[i-1]
    i+=1
 
# Menampilkan sebanyak 2 bilangan fibonacci setiap barisnya
i = 0
j = 1
spasi = " "

# Output fibonacci
print("Bilangan Fibonacci")
while i<10 :
    if j==2 :
        print("  "+str(fibonacci[i]))
        j=1
        spasi=spasi+"  "
        if i!=9 :  
            print(spasi, end="")
    else :
        print(end="  "+str(fibonacci[i]))
        j+=1
    i+=1