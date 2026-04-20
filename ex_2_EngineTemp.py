class Silnik:
    def __init__(self, temperatura):
        self.poziom_temp = temperatura
    
    @property
    def poziom_temp(self):
        return f"Temperatura wynosi {self._temperatura}"
    
    @poziom_temp.setter
    def poziom_temp(self, wartosc):
        if wartosc > 120:
            print("Uwaga: Silnik przegrzany, ograniczam do 120")
            self._temperatura = 120
        elif wartosc < -30:
            print("Silnik zamarzł. Ostatni pomiar: -30")
            self._temperatura = -30
        else:
            self._temperatura = wartosc 
    

    def stan_silnika(self):
        if self._temperatura < 40:
            return "Zimny"
        elif 40 <= self._temperatura <= 90:
            return "Optymalny"
        elif self._temperatura > 90:
            return "Przegrzany"
    
s1 = Silnik(125)
print(s1.poziom_temp, s1.stan_silnika())