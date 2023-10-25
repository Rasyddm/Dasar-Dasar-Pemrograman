kendaraan= ["beat,motor,150cc,merah,dua"]
print (kendaraan)
kendaraan.append("19jt,matic")
print (kendaraan)
kendaraan.insert(3,"honda")
print (kendaraan)

print()

menghitung= input("menghitung bangun datar")
match menghitung:
    case "1":
        sisi= int(input("masukan nilai sisi"))
        luas= sisi*sisi
        print(luas)
    case "2":
         jari_jari= int(input("masukan niali jari-jari:"))
         luas= 3.14*jari_jari*jari_jari
         print(luas)
    case "3":
        alas= int(input("masukan nilai alas:"))
        tinggi= int(input("masukan nilai tinggi:"))
        luas= 0.5*alas*tinggi
        print(luas)
    case _:
         print("salah pilih")


