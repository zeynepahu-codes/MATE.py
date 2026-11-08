while True:
    try:
        sayi = int(input("Bir sayı girin: "))
        break
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz")
 
print(f"Girdiğiniz sayı: {sayi}")
 