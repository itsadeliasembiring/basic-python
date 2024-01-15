"""
Variable => Wadah yg nampung value/nilai/data (Tempat nyimpen data)
di python ga ada deklarasi kek int a 

Penamaan Variable:
- Ga boleh spasi dan pake (-) => bolehnyaa pake (_) =>nilai_x
- Depannya ga bole ada angka =? boleh taro belakang aja aku123
- misal huruf depan kecil dan kata nextnya kapital gapapa kek => nilaiX

"""
#penamaan & pemanggilan part 1
a = 100
nilai_x =  5
print("Nilai a adalah",a)
# Ternyata bisa gini
print("nilai",a,"tambah",nilai_x,"adalah",a+nilai_x)

#pemanggilan part 2
print("nilai",a)
a = 8
print("nilai terbaru",a)
# assignment indirect (variable yg valuenya dari variable sebelumnya)
b = a
print("nilai b adalah",b)
  