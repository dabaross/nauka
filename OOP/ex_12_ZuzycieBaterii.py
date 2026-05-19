class ZuzycieBaterii:
    def __init__(self, func):
        # Twoj kod tutaj (zapisz func i ustaw baterie na 30)
        self.func = func
        self.poziom_baterii = 30
        pass

    def __call__(self): # Celowo bez args i kwargs!
        # Twoj kod tutaj (logika zuzycia i wywolania)
        if self.poziom_baterii > 0:
            self.poziom_baterii -= 10
            print(f"Bateria: {self.poziom_baterii}")
            return self.func()
        else:
            print("Bateria rozładowana")

        pass

# --- UŻYCIE ---

@ZuzycieBaterii
def wyslij_ping():
    print("  -> Sygnał z czujnika wysłany poprawnie!\n")

# --- TESTY ---
# Wywołujemy funkcję 4 razy.
# Za pierwszym, drugim i trzecim razem powinna zadziałać.
# Za czwartym razem bateria powinna być pusta (odrzucone).

wyslij_ping()
wyslij_ping()
wyslij_ping()
wyslij_ping()