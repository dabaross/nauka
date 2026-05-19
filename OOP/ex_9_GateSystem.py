def weryfikacja_czasu(fun):
    def wrapper(self, osoba, czas):
        self.osoba = osoba
        self.czas = czas

        if czas > 120:
            osoba = f"ALARM: {osoba}"
        return fun(self, osoba, czas)
    return wrapper

class Brama:
    logi =[]
    def __init__(self):
        pass

    @weryfikacja_czasu
    def rejestruj_wjazd(self, osoba, czas):
        wpis = f"Wjechał {osoba}, Czas: {czas}"
        self.logi.append(wpis)
        return  wpis
 

b = Brama()

print(b.rejestruj_wjazd("Damian", 50))
print(b.rejestruj_wjazd("Nieznajomy", 200))