import os
import json
from dotenv import load_dotenv

class Zarzadca:
    def __init__(self, nazwa_pliku):
        self.nazwa_pliku = nazwa_pliku

    def __enter__(self):
        print(f"Otwarto połączenie z {self.nazwa_pliku}")
        return self
    
    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            print(f"Error {exc_type}")
        return False
    

def uruchom_rejestrator():
    # Wczytujemy dane z .env
    load_dotenv()
    sensor = os.getenv("SENSOR_NAME")
    
    # Używamy naszego menedżera
    with Zarzadca("dane.json") as zarzadca:
        print(f"Logowanie danych dla sensora: {sensor}")
        
        # Tutaj mogłaby być Twoja logika JSON (Read-Update-Write)
        dane = {"sensor": sensor, "status": "online"}
        print(f"Zapisuję: {dane}")

# 3. STRAŻNIK (Główny włącznik)
if __name__ == "__main__":
    uruchom_rejestrator()
