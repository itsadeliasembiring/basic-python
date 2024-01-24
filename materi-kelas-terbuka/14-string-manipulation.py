# Operasi & Manipulasi String

# Menyambung string (Concatenate)
first_name = "Adele"
middle_name = "Ruby"
last_name = "Jane"
complateName = first_name+" "+middle_name+" "+last_name
print(complateName)

# Hitung panjang string (Len)
panjangNama = len(first_name)
print("Panjangnya sebanyak", str(panjangNama), "chacacter")

# Operasi String
# Mengecek apakah di sebuah string ada komponen char atau string (Kek search huruf gitu)
search = "Z"
result  = search in complateName
print ("huruf"+" "+search+" ada di "+complateName+" = "+str(result))
# Akan false karna di dalam variable complateName tidak ada huruf Z (lower or uppercase ngaruh juga)
# Versi gak ada (kebalikan IN) nanti hasilnya bakal true
search = "Z"
result  = search not in complateName
print ("huruf"+" "+search+" tidak ada di "+complateName+" = "+str(result))

# Mengulang string
print("xi"*100)
print(7*"wk")

# Indexing : Ambil data dari string (Motong) 
# Index mulai dari 0 yh kack
print("index ke-0 adalah : " + complateName[0])
print("index ke-1 adalah : " + complateName[1])
print("index ke-2 adalah : " + complateName[2])
print("index ke-3 adalah : " + complateName[3])
print("index ke-4 adalah : " + complateName[4])
# Kalo - nanti ambil dari belakang (start from -1)
print("index ke -1 dari adele adalah : " + first_name[-1])
# dari 0 sampai .. (: artinya sampai)
print("index ke 0 sampe 3 dari adele adalah : " + first_name[0:4])
# Index ke 3 gak akan di tampilin, program seolah baca ambil index 0 sampai sebelum 3, so buat nampilinnya +1 aja dari index yg mau diambil
print("index ke 2 sampe 4 dari adele adalah : " + first_name[2:5])
# index dengan jeda
print("index ke [0,2,4,6,8,12] dari adele ruby jane adalah : " + complateName[0:8:2]) #Tambahin increment/kelipatan di belakang
# spasi juga kebaca/di itung index
print("index ke-5 adalah : " + complateName[5])

# Item paling kecil (Min)
print("yang paling kecik : " + min(first_name)) 
#spasi kebaca juga anjay soalnya ASCII paling kecik
asciiCode = ord(" ")
print("ASCII code untuk spasi adalah " + str(asciiCode))
data = 117
print("ASCII code untuk a adalah " + chr(data))
# Item paling besar (Max)
print("yang paling besar : " + max(complateName))

# Operator dalam bentuk method
data = "Anjayyyy"
jumlah =  data.count("y") #count itu method
print("Jumlahnya ", str(jumlah))

# Method ubah string jadi upper case
testing = "aDeLe ManiEzZzz"
print("Ori : "+testing)
testing = testing.upper()
print("Upper : ", testing)
# Lowercase
testing = testing.lower()
print("Lower : "+testing)
# Kapital
testing = testing.capitalize()
print("capitalize : "+testing)


# Pengecekan dengan isX method
# contohnya pengecekan lower case
salam = "hi sist"
enihLower = salam.islower() #Enih resultnya bool jadi harus di string
# ga semua tipe data bisa di concat (pake koma bisa, kalo + harus di ubah jadi str duls)
print(salam + " is lower? "+ str(enihLower))
enihUpper = salam.isupper() 
print(salam + " is upper? "+ str(enihUpper)) 

# isalpha() -> buat cek apakah semuwa huruf + gak kosong
data = "hisist"
enihAlpha = data.isalpha() 
print(data + " is alpha (only huruf)? "+ str(enihAlpha))  #kalo ada spasi auto false

# isalnum() -> buat cek apakah semuwa huruf + angka
data = "hisist123"
enihAlnum = data.isalnum() 
print(data + " is alnum? (huruf and angka)?"+ str(enihAlnum))  #kalo salah satu memenuhi syarat auto true

# isdecimal() -> buat cek apakah semuwa angka
data = "3"
enihDecimal = data.isdecimal() 
print(data + " is decimal (only angka)? "+ str(enihDecimal))  #kalo ada spasi auto false

# isspace() -> buat cek string kosong (tab, spasi, newline \n)
data = "\t"
enihSpace = data.isspace() 
print(data + " is space (spasi,tab,\\n, dll)? "+ str(enihSpace)) 
# istitle() -> buat cek apakah semuwa katanya dimulai huruf besar
data = "Ayam Goreng Mak Cik"
enihTitle = data.istitle() 
print(data + " is title (awal kata huruf besar)? "+ str(enihTitle)) #kalo salah satu kata huruf kecik auto false, sama kalo ada ' auto false karna ga sesuai aturan judul

# Mengecek komponen startswith() endswith()
# startswith() buat cek kata pertama (upper lower ngaruh)
cek_start = "Annyeong Oppa".startswith("Annyeong")
print("start = " + str(cek_start))
# endswith() buat cek kata terakhir (upper lower ngaruh)
cek_ends = "Annyeong Oppa".endswith("Oppa")
print("ends = " + str(cek_ends))

# Penggabungan komponen join() split()
pisah = ['aku','orang','batak'] #ini list
print(pisah)
# gabung -> Join()
combine = ','.join(pisah)
print(combine)
combine = ' '.join(pisah) #bisa ganti tanda
print(combine)
#  split ()
gabungan = "akuehmakuehmaku"
print(gabungan.split("aku")) #kata akan hilang dan sisanya jadi list [..,..]

## alokasi karakter rjust(),ljust(),center()
# rata kanan rjust(berapa)
kanan = "right".rjust(10) #10 karakter di itung dari kanan, makin panjang kata makin kureng spasinya
print("'"+kanan+"'")
# rata kanan ljust(berapa)
kiri = "left".ljust(10) #10 karakter di itung dari kiri, makin panjang kata makin kureng spasinya
print("'"+kiri+"'")
# center
tengah = "center".center(10) #10 karakter di itung dari kiri kanan, makin panjang kata makin kureng spasinya
print("'"+tengah+"'")
# bisa diubah ga pake spasi (misal ganti -, +, apagitu)
kanan = "right".rjust(10,"-") 
print("'"+kanan+"'")

# kebalikannya (kalo tadi kan dia nambahin dan enih ngilangin)->strip() 
tengah = tengah.strip() #ngilangin spasi, bisa tengah = tengah.strip(" ")
print("'"+tengah+"'")