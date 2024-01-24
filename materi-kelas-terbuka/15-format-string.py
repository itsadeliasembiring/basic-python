# format string

# contoh generic
name = "adelew"
str = "hellow " + name
print(str)
# versi format f"isi {variable}"
format_str = f"hello {name}"
print(format_str)

# Number
angka = 2020.2
format_str = f"angka = {angka}" #auto jadi str
print(format_str)
# Versi bilangan bulat
angka1 = 20
format_str = f"angka = {angka1:d}" #error kalo float/ada koma
print(format_str)

# Bilangan ribuan,jutaan,dll (kasi :, biar jadi 2,000,000)
angka = 200000
format_str = f"ribuan = {angka:,}"
print(format_str)

# Bilangan desimal {variable:.ambilBrpAngkaSehabisTitik-f}
angka = 2005.17373737
format_str = f"desimal = {angka:.2f}"
print(format_str)

# Menampilkan leading zero (depannya) 2005.173=8
angka = 2005.17373737
format_str = f"desimal = {angka:7.2f}" #7nya di itung dari dpn
print(format_str)
format_str = f"desimal = {angka:8.2f}" #kalo lewat, nnti depannya muncul space kosong
print(format_str)
format_str = f"desimal = {angka:08.2f}" #depan kasi 0 biar space kosongnya diganti 0
print(format_str)

# boolean
bool = False
format_str = f"boolean = {bool}" 
print(format_str)

# menampilkan tanda +  :+d
plusNumber = 10.12344
format_plus = f"plus = {plusNumber:+}" #auto muncul tanda +
print(format_plus)
format_plus = f"plus = {plusNumber:+.2f}"  #bisa kasi enih juga
print(format_plus)
# menampilkan tanda - :-d
minusNumber = -10
format_minus = f"minus = {minusNumber:-d}"
print(format_minus)

# Memformat persen
persentase = 0.011
format_persen = f"persen = {persentase:%}"
print(format_persen)
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika dalam placeholder/kurung
harga = 10000
jumlah = 5
format_str = f"harga total = Rp. {harga*jumlah:,}"
print(format_str)

# format angka lain (binary, octal, hexadecimal)
number = 255
format_binary = f"binary = {bin(number)}" #method bin
print(format_binary)
format_octal = f"octal = {oct(number)}" #method oct
print(format_octal)
format_hexa = f"hexa = {hex(number)}" #method hex
print(format_hexa)

