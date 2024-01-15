"""
casting type data => merubah tipe data dari 1 tipe ke tipe lain
Kek dari int ke string

tipe data => int, str, float, bool

caranya 
tipedata(nama_variable)

conver float (koma) to int (bulet) bakal dibuletin ke bawah kek 8.9 jadi 8
tiap conver perilakunya beda-beda
"""

## INT ##
this_int = 3
print("data = ", this_int, "type = ", type(this_int))
# To float
int_to_float = float(this_int)
print("data ",int_to_float,"tipe ", type(int_to_float))
# To String
int_to_str = str(this_int)
print("data ",int_to_str,"tipe ", type(int_to_str))
# To bool
int_to_bool = bool(this_int) #false kalo value nya 0, diluar 0 true
print("data ",int_to_bool,"tipe ", type(int_to_bool))

## FLOAT ##
this_float = 3.1
# To Int
float_to_int = int(this_float) # dibuletin ke bawah
print("value ", float_to_int, type(float_to_int))
# To Bool
float_to_bool = bool(this_float) # >0 valuenya true
print("value ", float_to_bool, type(float_to_bool))
# To String
float_to_str = str(this_float)
print("data ",float_to_str,"tipe ", type(float_to_str))

## boolean ##
this_bool = False
# To Int
bool_to_int = int(this_bool)
print("value ", bool_to_int, type(bool_to_int))
# To Float
bool_to_float = float(this_bool)
print("value ", bool_to_float, type(bool_to_float))
# To String
bool_to_str = str(this_bool)
print("data ",bool_to_str,"tipe ", type(bool_to_str))

## String
this_str = ""
# To Int (Ga bisa kalo valuenya huruf)
str_to_int = int(this_str)
print("value ", str_to_int, type(str_to_int))
# To Float (Ga bisa kalo valuenya huruf)
str_to_float = float(this_str)
print("value ", str_to_float, type(str_to_float))
# To Bool (false kalo string kosong)
str_to_bool = bool(this_str)
print("data ",str_to_bool,"tipe ", type(str_to_bool))