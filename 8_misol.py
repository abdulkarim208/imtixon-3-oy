import json

with open("products.json", "r") as f:
    mahsulotlar = json.load(f)

nom = input("mahsulot nomi: ")
miqdor = int(input("yangi miqdor: "))

topildi = False

for mahsulot in mahsulotlar:
    if mahsulot["nom"] == nom:
        mahsulot["miqdor"] = miqdor
        topildi = True

if topildi:
    with open("products.json", "w") as f:
        json.dump(mahsulotlar, f, indent=4)
    print("miqdor yangilandi.")
else:
    print("mahsulot topilmadi.")