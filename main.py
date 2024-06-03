import openpyxl
import kelime_düzenleme

kelime_listesi=set(kelime_düzenleme.yenilenmis_kelimeler)


harf_listeleri = {
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: []
}

for kelime in kelime_listesi:
    if isinstance(kelime, str):
        kelime_uzunlugu = len(kelime)
        if kelime_uzunlugu in harf_listeleri:
            harf_listeleri[kelime_uzunlugu].append(kelime)




tahmin_listesi=[]
harf_sayisi=input("Lütfen harf sayısını giriniz: ")



diger_harfler=input("Yeri belli olmayan diğer harfleri aralarında bir boşluk olucak şekilde yazın: ")
diger_harfler_liste=diger_harfler.split()

for kelime in harf_listeleri[int(harf_sayisi)]:
    degisken=0
    for i in range(len(diger_harfler_liste)):
        if diger_harfler_liste[i] in kelime:
            degisken+=1
            if degisken==len(diger_harfler_liste):
                tahmin_listesi.append(kelime)
            else:
                continue
        else:
            break



harf_siralamasi = {}
for i in range(1,int(harf_sayisi)+1):
    harf_nedir=input(f"{i}. harfi girin: ")


    if harf_nedir=="":
        continue
    else:
        harf_siralamasi[i]=harf_nedir

harf_numaraları=list(harf_siralamasi.keys())
harf_degerleri=list(harf_siralamasi.values())
bilinen_harf_sayisi = len(harf_siralamasi)

son_tahmin_listesi=[]
for kelime in tahmin_listesi:
    deger = 0
    for i in range(bilinen_harf_sayisi):
        if kelime[int(harf_numaraları[i])-1]==harf_degerleri[i]:
            deger=deger+1
            if deger == int(bilinen_harf_sayisi):
                son_tahmin_listesi.append(kelime)
            else:
                continue
        else:
            break



if len(son_tahmin_listesi)>1:
    print(son_tahmin_listesi)
else:
    print(tahmin_listesi)

"""
for kelime in harf_listeleri[harf_sayisi]:
    bilinen_harf_sayisi=len(harf_siralamasi)
    for i in range(0,bilinen_harf_sayisi):
        bilinen_harf_numarası=list(harf_siralamasi.keys())[i]
        if kelime[bilinen_harf_numarası]==list(harf_siralamasi.values())[i]:
            tahmin_listesi.append(kelime)
        else:
            continue

"""





