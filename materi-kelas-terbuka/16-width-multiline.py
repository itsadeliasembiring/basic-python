# Width and Multiline
data_name = "adele"
data_umur = 19
data_tinggi = 200

# string standard
data_string = f"nama = {data_name}, umur = {data_umur}, tinggi = {data_tinggi}"
print(5*"="+"String Standard"+5*"=")
print(data_string)

# string multiline (pakai enter/newline, \n)
data_string = f"nama = {data_name} \numur = {data_umur} \ntinggi = {data_tinggi}"
print("\n"+5*"="+"String Multiline with \\n"+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama = {data_name}, tinggi = {data_tinggi}

 
umur = {data_umur}
"""
# bakal tampil sesuai yg kita codingin (ga perlu \n lagi)
print("\n"+5*"="+'String Multiline with """'+5*"=")
print(data_string)

# string multiline (rata) pake :>mawbrp
data_string = f"""
nama   = {data_name:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
"""
# bakal tampil sesuai yg kita codingin (ga perlu \n lagi)
print("\n"+5*"="+'String Multiline Atur Lebar'+5*"=")
print(data_string)