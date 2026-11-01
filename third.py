dogum_yili = int(input("Doğum yılınız: "))
yas = 2026 - dogum_yili

if yas < 0:
    print("Geçersiz doğum yılı.")
elif yas >= 18:
    print(f"Yaşınız {yas}. Ehliyet alabilirsiniz.")
else:
    print(f"Yaşınız {yas}. Henüz ehliyet alamazsınız.")