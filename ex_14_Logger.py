class LoggerArgumentow:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print(f"Pozycyjne: {args}, Nazwane: {kwargs}")
        return self.func(*args, **kwargs)





@LoggerArgumentow
def ustaw_temperature(temp, jednostka):
    print(f"Ustawiono: {temp}{jednostka}\n")

@LoggerArgumentow
def konfiguruj_wifi(ssid, haslo, statyczne_ip=False):
    print(f"Łączenie z {ssid}...\n")

# --- TESTY ---
# Tu nie zmieniasz nic, po prostu uruchom.

ustaw_temperature(22.5, "C") # Tylko pozycyjne
ustaw_temperature(75, jednostka="F") # Mieszane
konfiguruj_wifi("MojaSiec", "Tajne123", statyczne_ip=True) # Pozycyjne + nazwane