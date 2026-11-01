def indirim_hesapla(tutar, yuzde):
    indirim_tutari = tutar * yuzde / 100
    son_fiyat = tutar - indirim_tutari
    return indirim_tutari, son_fiyat


tutar = float(input("Fiyatsız tutar (TL): "))
yuzde = float(input("İndirim yüzdesi: "))

indirim, son = indirim_hesapla(tutar, yuzde)

print(f"İndirim tutarı: {indirim:.2f} TL")
print(f"Son fiyat: {son:.2f} TL")