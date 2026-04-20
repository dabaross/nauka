def eko_asystent(func):
    def wrapper(self, wartosc):
        if wartosc > 22:
            print("EKO: Zużywasz za dużo energii")
        return func(self, wartosc)
        # 1. Tu sprawdź: jeśli wartosc > 22, wypisz "EKO: Zużywasz dużo energii!"
        # 2. Niezależnie od wyniku powyżej, wywołaj oryginalną funkcję (func)
    

class Termostat:
    def __init__(self):
        self._temperatura = 20 # Temperatura początkowa

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    @eko_asystent # Naklejamy naszą dodatkową funkcję
    def temperatura(self, wartosc):
        if 5 <= wartosc <= 30:
            self._temperatura = wartosc
            print(f"Ustawiono temperaturę na {wartosc}°C")
        else:
            print("BŁĄD: Temperatura poza zakresem bezpieczeństwa (5-30)!")

# --- TEST ---
dom = Termostat()

print("--- Test 1: 18 stopni ---")
dom.temperatura = 18

print("\n--- Test 2: 25 stopni ---")
dom.temperatura = 25 # Tu powinien zadziałać Eko-Asystent i Setter

print("\n--- Test 3: 40 stopni ---")
dom.temperatura = 40 # Tu Setter powinien wywalić błąd