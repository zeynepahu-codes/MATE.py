def harf_notu_hesapla(vize, final):
    ortalama = vize * 0.4 + final * 0.6

    if ortalama >= 90:
        harf = "AA"
    elif ortalama >= 85:
        harf = "BA"
    elif ortalama >= 80:
        harf = "BB"
    elif ortalama >= 75:
        harf = "CB"
    elif ortalama >= 70:
        harf = "CC"
    elif ortalama >= 60:
        harf = "DC"
    elif ortalama >= 50:
        harf = "DD"
    else:
        harf = "FF"

    return ortalama, harf


vize = float(input("Vize notu: "))
final = float(input("Final notu: "))

ortalama, harf = harf_notu_hesapla(vize, final)

print(f"Ortalama: {ortalama:.2f}")
print(f"Harf notu: {harf}")