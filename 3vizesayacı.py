
from datetime import datetime
 
while True:
    metin = input("Sınav tarihi ve saati (GG.AA.YYYY SS:DD): ")
    try:
        sinav = datetime.strptime(metin, "%d.%m.%Y %H:%M")
        break
    except ValueError:
        print("Format hatalı. Örnek: 14.11.2026 10:00")
 
fark = sinav - datetime.now()
 
if fark.total_seconds() <= 0:
    print("Bu tarih geçmiş.")
else:
    gun = fark.days
    saat = fark.seconds // 3600
    print(f"Sınava {gun} gün {saat} saat kaldı.")
 