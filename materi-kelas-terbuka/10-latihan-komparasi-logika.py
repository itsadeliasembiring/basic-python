# Membuat gabungan area rentang dari angka

inputUser = float(input("Masukin angka < 3 atau > 10 : "))

# Check afakah the number <3
isKurangDari = (inputUser < 3)
print("Angka < 3 adalah ",isKurangDari)

# Check afakah the number >10
isLebihDari = (inputUser > 10)
print("Angka > 10 adalah ",isLebihDari)

# ornya hrus kecik
isCorrect = isKurangDari or isLebihDari 
print("Apakah angka tersebut memenuhi syarat ?", isCorrect)

print("\n", 10*"=","\n")
# Kasus irisan 3 sampe 10 ======3+++++10=======
inputUser = float(input("Masukin angka > 3 atau < 10 : "))
# Check afakah the number >3 ===3+++++
isLebihDari = (inputUser > 3)
print("Angka > 3 adalah ",isLebihDari)

# Check afakah the number < 10 +++10====
isKurangDari = (inputUser < 10)
print("Angka < 10 adalah ",isKurangDari)

# Checking
isCorrect = isLebihDari and isKurangDari
print("Apakah angka tersebut memenuhi syarat ?", isCorrect)

print("\n", 10*"=","\n")

# PR : Buat program yg  --0++5--8++11-- dan ++0--5++8--11++
# >0, <5, >8, <11
# <0, >5, <8,>11

inputUser = float(input("Masukin angka>=0, <=5, >8, <11 : "))
# Soal 1
Result1 = (inputUser >=0) and (inputUser <=5)
print ("Apakah >= 0 & <=5 ? ", Result1)
Result2 = (inputUser >=8) and (inputUser <=11)
print ("Apakah >= 8 & <=11 ? ", Result2)
# Checking
ResultAll = Result1 or Result2
print("Apakah memenuhi syarat? ", ResultAll)

# Soal 2
Result3 = (inputUser <= 0) or (inputUser >=5)
print ("Apakah <= 0 atau >= 5 ? ", Result3)
Result4 = (inputUser <= 8) or (inputUser >=11)
print ("Apakah <= 8 atau >= 11 ? ", Result4)
# Checking
ResultAll = Result2 or Result3
print("Apakah memenuhi syarat? ", ResultAll)
