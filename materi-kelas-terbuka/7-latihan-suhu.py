print("\n Kalkulator Konversi Suhu\n")

# Celcius
celcius =  float(input("Masukkan suhu dalam celcius : "))
print("Suhu dalam Celcius adalah ", celcius,"C")
# Reamur => 4/5 C  kasi kurunk biar 4/5 duluan yg diitung
c_to_reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah ", c_to_reamur, "R")
# Fahrenheit
c_to_fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah ", c_to_fahrenheit, "F")
# Kelvin
c_to_kelvin = celcius + 273
print("Suhu dalam Kelvin adalah ", c_to_kelvin, "K")

# Reamur
reamur =  float(input("Masukkan suhu dalam reamur : "))
print("Suhu dalam Reamur adalah ", reamur,"R")
# Celcius
r_to_celcius = (5/4) * reamur
print("Suhu dalam Celcius adalah ", r_to_celcius, "C")
# Fahrenheit
r_to_fahrenheit = ((9/4) * reamur) + 32
print("Suhu dalam Fahrenheit adalah ", r_to_fahrenheit, "F")
# Kelvin
r_to_kelvin = ((5/4) * reamur) + 273
print("Suhu dalam Kelvin adalah ", r_to_kelvin, "K")

# Fahrenheit
fahrenheit =  float(input("Masukkan suhu dalam fahrenheit : "))
print("Suhu dalam fahrenheit adalah ", fahrenheit,"F")
# Celcius
f_to_celcius = (5/9) * (fahrenheit - 32)
print("Suhu dalam Celcius adalah ", f_to_celcius, "C")
# Reamur
f_to_reamur = (4/9) * (fahrenheit - 32)
print("Suhu dalam Fahrenheit adalah ", f_to_reamur, "R")
# Kelvin
f_to_kelvin = ((5/9) * (fahrenheit - 32)) + 273
print("Suhu dalam Kelvin adalah ", f_to_kelvin, "K")

# Kelvin
kelvin =  float(input("Masukkan suhu dalam kelvin : "))
print("Suhu dalam kelvin adalah ", kelvin,"F")
# Celcius
k_to_celcius = kelvin - 273
print("Suhu dalam Celcius adalah ", k_to_celcius, "C")
# Reamur
k_to_reamur = (4/5) * (kelvin - 273)
print("Suhu dalam kelvin adalah ", k_to_reamur, "R")
# fahrenheit
k_to_fahrenheit = ((9/5) * (kelvin - 273)) + 32
print("Suhu dalam Kelvin adalah ", k_to_fahrenheit, "F")