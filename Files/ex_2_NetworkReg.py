import json

class BlednaJakoscSygnalu(Exception):
    pass

def sprawdz_sygnal(fun):
    def wrapper(self, ssid, moc):
        if moc < 0 or moc > 100:
            raise BlednaJakoscSygnalu("Błędna jakość sygnału")
        return fun(self, ssid, moc)
    return wrapper

class RejestratorWiFi:

    
    def __init__(self, nazwa_pliku):
        self.nazwa_pliku = nazwa_pliku
        self.znalezione_sieci=[]
    @sprawdz_sygnal
    def dodaj_siec(self, ssid, moc):
        self.pomiary = {"ssid": ssid, "moc": moc}
        self.znalezione_sieci.append(self.pomiary)

    def archiwizuj(self):
        with open(self.nazwa_pliku, "w") as plik:
            json.dump(self.znalezione_sieci, plik)
        return f"Dane zapisane w pliku: {self.nazwa_pliku}"

    def przywroc_dane(self):
        try:
            with open(self.nazwa_pliku, "r") as plik:
                self.znalezione_sieci = json.load(plik)
        except FileNotFoundError: 
            print("Nie znaleziono pliku, tworzę nową bazę.")

rejestrator = RejestratorWiFi("skan.json")

try:
    rejestrator.dodaj_siec("Dom_WiFi", 80)
    print("Dodano Dom_WiFi")
    rejestrator.dodaj_siec("Sasiad_Wifi", 120) # To rzuci błąd
except BlednaJakoscSygnalu as e:
    print(f"Złapano błąd: {e}")

rejestrator.archiwizuj()

# Test recovery
recovery = RejestratorWiFi("skan.json")
recovery.przywroc_dane()
print(f"Dane w nowym obiekcie: {recovery.znalezione_sieci}")