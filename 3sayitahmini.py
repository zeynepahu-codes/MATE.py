import random
 
hedef = random.randint(1, 100)
tahmin_sayisi = 0
 
print("1 ile 100 arasında bir sayı tuttum, bulabilir misin?")
 
while True:
    try:
        tahmin = int(input("Tahmininiz: "))
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz")
        continue
 
    tahmin_sayisi += 1
 
    if tahmin < hedef:
        print("Yukarı çık")
    elif tahmin > hedef:
        print("Aşağı in")
    else:
        print(f"Tebrikler! {tahmin_sayisi} tahminde buldun.")
        break
 