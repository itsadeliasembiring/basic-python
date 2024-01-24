# String

# Single quote
data = 'Iki single quote'
print(data)
# Double quote
data = "iki string double quote"
print(data)

# Gabungan
print('"Halowww afah kabar broooo"')
print("'Baiqqq', skrg hari jum'at yah?")

# character khusus : \ (Backslash)
print('hari jumat waktunya sholat  jum\'at')
print('g\'day, isn\'t it?')
# misal mau print backslashnyaa, kasi backslash lagi
print("C:\\users\\jennie")
# ver 2 pakai raw string : semuwa dianggep string
print(r'C:\new folder \n')

# tab => \t
print("Jennie \t ldr \t ama \t adele")

# backspace => \b 
print("Adel \byj")
print("Adel\byj")
print("Adel yj")
# !kesimpulan : dia apus karakter sebelumnya\

# New line =>\n (enter)
print("fist baris. \nseken baris.")#LF->line feed->linux,mac os (Unix)
print("fist baris. \rseken baris.") #CR->carriage return->yg lama kek commodore, acorn,lisp
print("fist baris. \r\nseken baris.") #CRLF->line feed carriage return->windows

# multiline literal string
print("""
Nama : adele maniez
Pacar  : Yeonjunieeee
""")
#  pake rawwww string (rawwrrr)
print(r"""
Nama : adele maniez
Pacar  : Yeonjunieeee /mangeakkk
""")

