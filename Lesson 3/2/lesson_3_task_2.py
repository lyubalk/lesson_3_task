from smartphone import Smartphone

smartphone_1 = Smartphone("Samsung", "S40", "+71234566777")
smartphone_2 = Smartphone("apple", "XR", "+79080875643")
smartphone_3 = Smartphone("xiaomi", "A45", "+78653453467")
smartphone_4 = Smartphone("asus", "HY75", "+72345680978")
smartphone_5 = Smartphone("honor", "45", "+78905643454")

#  print(smartphone_1.model)

catalog = [
    smartphone_1,
    smartphone_2,
    smartphone_3,
    smartphone_4,
    smartphone_5
]
print(catalog)

for smartphone in catalog:
    print(f"<марка> - ", smartphone.stamp,
          "<модель> - ", smartphone.model,
          "<номер телефона> - ", smartphone.number)
