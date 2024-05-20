# Kalkulator Sederhana


print(10*"~")
print("Kalkulator Sederhana")
print(10*"~" + "\n")
angka1 = float(input("Masukkan angka 1 = "))
operator = input("Pilih operator (+, -, x, /) : ")
angka2 = float(input("Masukkan angka 2! = "))

# Percabangan
if operator == "+" :
    result = angka1 + angka2
    print(f"Hasilnya adalah {result}")
elif operator == "-" :
     result = angka1 - angka2
     print(f"Hasilnya adalah {result}")
elif operator == "*" or operator == "x":
    result = angka1 * angka2
    print(f"Hasilnya adalah {result}")
elif operator == "/" :
    result = angka1 / angka2
    print(f"Hasilnya adalah {result}")
else :
    print("Operator yang anda masukkan di luar nurul!")