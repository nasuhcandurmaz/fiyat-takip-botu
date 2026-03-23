urun_adi = 'iPhone 15'
fiyat = 50000
stok = True
indirim = 10
indirimli_fiyat = fiyat - (fiyat * indirim / 100)

urunler = ["iPhone 15", "Samsung S24", "Xiaomi 14"]
fiyatlar = [50000, 40000, 25000]
esik = 35000



print(urun_adi)
print(fiyat)
print(stok)


print("Normal fiyat:", fiyat)
print("İndirimli fiyat:", indirimli_fiyat)


print("İlk ürün:", urunler[0])
print("İlk fiyat:", fiyatlar[0])


#for i in range(len(urunler)):
    #print(urunler[i], "-", fiyatlar[i], "TL")#

for i in range(len(urunler)):
    if fiyatlar[i] < esik:
        print("UYARI - Ucuz ürün bulundu:", urunler[i], "-", fiyatlar[i], "TL")
    else:
        print(urunler[i], "normal fiyatta:", fiyatlar[i], "TL")    