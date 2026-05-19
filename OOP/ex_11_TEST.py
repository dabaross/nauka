import json

class TemperaturaPozaSkalaError(Exception):
    pass

def sprawdz_zakres(func):
    def wrapper(self, wartosc):
        if wartosc > -50 and wartosc < 100:
            print(f"Zapisano wartosc {wartosc}")
            return func(self, wartosc) 
        else:
            raise TemperaturaPozaSkalaError("Temperatura poza skala")
    return wrapper

class Termometr:
    def __init__(self):
        self.historia = []
    
    @sprawdz_zakres
    def zaloguj_temperature(self, wartosc):
        self.historia.append(wartosc)
    
    def export_json(self):
        nazwa_pliku = "dane.json"
        dane_do_zapsu = self.historia

        with open(nazwa_pliku, "w") as plik:
            json.dump(dane_do_zapsu, plik)
        
        return f"Dane zapisano w pliku {nazwa_pliku}"

try:
    termo = Termometr()
    termo.zaloguj_temperature(25)
    termo.export_json()
    print(termo.historia)

    termo.zaloguj_temperature(150)
except TemperaturaPozaSkalaError as e:
    print(e)