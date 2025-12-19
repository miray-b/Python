import random

while True:
    secret_number = random.randint(1,100)
    #print(secret_number)
    guess = 0
    lives = 5

    print("\n" + "*"*30)
    print("""Merhaba! 
      Sayı Tahmin Oyununa Hoş Geldiniz. 
      Bu oyunda sizden tuttuğum 1 ve 100 arasındaki sayıyı tahmin etmeniz bekleniyor. 
      5 deneme hakkınız var. 
      Başarılar! """)
    while guess != secret_number:
        try: 
            user_input = input("Tahmininiz nedir?")
            guess = int(user_input)
        except ValueError:
            print("Sayı girmediniz. Oyun bitti.")
            break

        if guess < secret_number:
            print("Tahmin yanlış! Daha büyük bir sayı deneyin.")
            lives = lives - 1
            print(f"Kalan deneme hakkınız: {lives}")
        elif guess > secret_number:
            print("Tahmin yanlış! Daha küçük bir sayı söyleyin.")
            lives = lives -1
            print(f"Kalan deneme hakkınız: {lives}")
        else:
            print("Tahmin doğru! Tebrikler.")
        if lives == 0:
            print("Deneme hakkınız bitti. Oyunu kaybettiniz.")
            break
    again = input("\n Tekrar oynamak ister misiniz? (E/H): ").lower()
    if again == "h":
        print("Oyun kapatılıyor. Tekrar görüşmek üzere!")
        break