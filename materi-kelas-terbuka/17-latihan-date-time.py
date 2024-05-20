# Date and Time (Latihan)
# Masukkan tanggal lahir nanti keliatan umur nya berapa

# import
import datetime as dt

# Today
hari_ini = dt.date.today()
print(hari_ini)\
# Isi Data
tanggal = dt.date(2005,1,23)
print(tanggal)
# Cara tau hari ini hari apa pake %A
print(f"Hari ini adalah hari = {hari_ini:%A}")

# Deteksi Umur
print("Masukkan tanggal, bulan, dan tahun lahir anda! //maksa")
# Inputan user di casting jadi int
tanggal = int(input("Tanggal \t:"))
bulan   = int(input("Bulan \t\t:"))
tahun   = int(input("Tahun \t\t:"))
# Masukkan jadi 1 variable
tanggal_lahir_user = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir mu adalah : {tanggal_lahir_user}")
print(f"Kamu lahir pada hari : {tanggal_lahir_user:%A}")
# Hitung Umur => Hari ini - tanggal lahir
hari_ini = dt.date.today()
print(f"Hari ini tanggal = {hari_ini}, dan hari {hari_ini:%A}")
umur_hari = hari_ini - tanggal_lahir_user
umur_tahun = umur_hari.days // 365 #// biar bulet
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"""
Umur anda adalah        : {umur_tahun} tahun
Kamu telah hidup selama : {umur_hari.days} hari, {umur_bulan_sisa} bulan
""")