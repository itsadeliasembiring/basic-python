""" why casting di perlukan?
syntax => input("....")
contoh nama_varible = input("Masukkan nama mu : ")


"""

# nama = input("Input namamu : ")
# print("isinya = ",nama, "bertipe ", type(nama))
# Datanya alayways string typenya
# Kalo mau diubah, pake castin data materi sebelumnya
# umur = int(input("Umur ?")) #bisa float juga, klo dimasukin huruf auto eror
# print ("Umurnya : ", umur, "bertipe ",type(umur))

# Kalo bool harus di int dulu
biner = bool(int(input("Masukkan bool ")))
print ("Bool bernilai ", biner, "bertipe ", type(biner))