import csv
import datetime


with open("Menu.txt", "w") as menu_file:
    menu_file.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n1: Klasik\n2: Margarita\n3: TürkPizza\n4: Sade Pizza\n* ve seçeceğiniz sos:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n* Teşekkür ederiz!")

# Pizza sınıfı
class Pizza:
    def __init__(self):
        self.description = "Pizza"
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return 0

# KlasikPizza sınıfı
class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik Pizza"
    
    def get_cost(self):
        return 20

# MargheritaPizza sınıfı
class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"
    
    def get_cost(self):
        return 25

# TurkPizza sınıfı
class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Türk Pizza"
    
    def get_cost(self):
        return 30

# SadePizza sınıfı
class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Sade Pizza"
    
    def get_cost(self):
        return 15

# Decorator sınıfı
class Decorator(Pizza):
    def __init__(self, component):
        super().__init__()
        self.component = component
    
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    
    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

# Zeytin sosu sınıfı
class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Zeytin Soslu"

    def get_cost(self):
        return self.component.get_cost() + 5

# Mantar sosu sınıfı
class Mantarlar(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mantarlı Soslu"

    def get_cost(self):
        return self.component.get_cost() + 6

# Keçi peyniri sosu sınıfı
class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Keçi Peynirli Soslu"

    def get_cost(self):
        return self.component.get_cost() + 8

# Et sosu sınıfı
class Et(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Etli Soslu"

    def get_cost(self):
        return self.component.get_cost() + 10

# Soğan sosu sınıfı
class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Soğanlı Soslu"

    def get_cost(self):
        return self.component.get_cost() + 4

# Mısır sosu sınıfı
class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mısır Soslu"

    def get_cost(self):
        return self.component.get_cost() + 3

# main fonksiyonu
def main():
    # Menüyü yazdır
    with open("Menu.txt", "r") as menu:
        print(menu)


if __name__ == '__main__':
    pizza = None

    while not pizza:
        try:
            base_choice = int(input(
                "Lütfen bir pizza tabanı seçiniz: (1-Klasik, 2-Margarita, 3-TürkPizza, 4-Sade Pizza) "))
            if base_choice == 1:
                pizza = KlasikPizza()
            elif base_choice == 2:
                pizza = MargheritaPizza()
            elif base_choice == 3:
                pizza = TurkPizza()
            elif base_choice == 4:
                pizza = SadePizza()
            else:
                print("Lütfen geçerli bir seçim yapınız.")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

    while True:
        try:
            sos_choice = int(input(
                "Lütfen bir sos seçiniz: (11-Zeytin, 12-Mantarlar, 13-Keçi Peyniri, 14-Et, 15-Soğan, 16-Mısır) "))
            if sos_choice == 11:
                pizza = Zeytin(pizza)
            elif sos_choice == 12:
                pizza = Mantarlar(pizza)
            elif sos_choice == 13:
                pizza = KeciPeyniri(pizza)
            elif sos_choice == 14:
                pizza = Et(pizza)
            elif sos_choice == 15:
                pizza = Sogan(pizza)
            elif sos_choice == 16:
                pizza = Misir(pizza)
            else:
                print("Lütfen geçerli bir seçim yapınız.")
            break
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

    aciklama = input("Açıklama: ")
      # Sipariş zamanını kaydetme
    order_time = datetime.datetime.now()
    
    print("------------------------")
    print("Siparişiniz hazır!")
    print("Sipariş tarihi:", order_time.strftime("%d-%m-%Y %H:%M"))
    print("Sipariş detayı:", pizza.get_description())
    print("Toplam fiyat:", pizza.get_cost(), "TL")
    print("Açıklama: ", aciklama)
    print("------------------------")
    print()
    # Kullanıcı bilgileri alınır
    print("------ÖDEME ALANI------")
    name = input("İsim: ")
    tc_no = input("TC Kimlik Numarası: ")
    while len(tc_no) != 11:
        print("Geçersiz TC Kimlik Numarası!")
        tc_no = input("TC Kimlik Numarası: ")
    cc_no = input("Kredi Kartı Numarası: ")
    cc_password = input("Kredi Kartı Şifresi: ")
    while len(cc_password) != 4:
        print("Geçersiz kredi kartı şifresi! Lütfen 4 haneli şifre giriniz!")
        cc_password = input("Kredi Kartı Şifresi: ")
    print("------------------------")
    print()
    print("Merhaba " + name + " siparişiniz oluşturulmuştur. ")
    print()

# Veritabanına ekleme yapılır
    with open("Orders_Database.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, tc_no, cc_no, pizza.get_description(), order_time.strftime("%d-%m-%Y %H:%M"), cc_password])
