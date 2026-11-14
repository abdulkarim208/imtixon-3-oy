mahsulotlar = {"non": 4000, "sut": 12000, "olma": 8000}

nom = input("mahsulot nomi: ")
narx = int(input("yangi narx: "))

if nom in mahsulotlar:
    mahsulotlar[nom] = narx
    print("narx yangilandi.")
else:
    print("mahsulot topilmadi.")

print(mahsulotlar)