import json # 1. Musimy to zaimportować

class SensorWifi:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.odczyty = []

    def dodaj_odczyt(self, rssi):
        # Tu by był Twój dekorator z poprzedniego zadania
        self.odczyty.append(rssi)

    def zapisz_do_json(self):
        nazwa_pliku = f"{self.nazwa}_dane.json"
        dane_do_zapisu = {"sensor": self.nazwa, "pomiary": self.odczyty}
        
        # 2. Otwieramy plik w trybie "w" (write - zapis)
        with open(nazwa_pliku, "w") as plik:
            # 3. Zamieniamy listę na JSON i wrzucamy do pliku
            json.dump(dane_do_zapisu, plik) 
        
        return f"Dane zapisane w pliku: {nazwa_pliku}"

# --- TEST ---
sensor = SensorWifi("Kuchnia")
sensor.dodaj_odczyt(-50)
sensor.dodaj_odczyt(-65)
sensor.dodaj_odczyt(-40)

print(sensor.zapisz_do_json())