 
def podwojne_punkty(func):
    def wrapper(self, ilosc_punktow):
        ilosc_punktow += ilosc_punktow
        return func(self, ilosc_punktow)
    return wrapper

class KartaKlienta:
    def __init__(self, ilosc_punktow):
        self.ilosc_punktow = ilosc_punktow

    @podwojne_punkty
    def dodaj_punkty(self, wartosc):
        self.ilosc_punktow += wartosc
        print(f"Ilosc pkt = {self.ilosc_punktow}")
    

karta = KartaKlienta(10)
karta.dodaj_punkty(50)