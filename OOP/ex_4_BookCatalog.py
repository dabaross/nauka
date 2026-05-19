class Ksiazka:
    def __init__(self, tytul, ilosc_stron):
        self.tytul = tytul
        self.strony = ilosc_stron

    @property
    def strony(self):
        return self._strony
    
    @strony.setter
    def strony (self, wartosc):
        if wartosc <= 0:
            self._strony = 1
        else:
            self._strony = wartosc
        
    def __eq__(self, other):
        if not isinstance(other, Ksiazka):
            return False
        return self._strony == other._strony
    
    def __lt__(self, other):
    # PRZYPADEK 1: Porównujemy Książkę z Książką
        if isinstance(other, Ksiazka):
            return self._strony < other._strony
        
        # PRZYPADEK 2: Porównujemy Książkę z Liczbą (int)
        if isinstance(other, int):
            return self._strony < other
        
        # PRZYPADEK 3: Ktoś podał coś dziwnego (np. napis)
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Ksiazka):
            return self._strony > other._strony
        if isinstance(other, int):
            return self._strony > other
        return NotImplemented

            
k1 = Ksiazka("Mały Książę", 100)
k2 = Ksiazka("Władca Pierścieni", 1200)
k3 = Ksiazka("Inna książka", 100)

print(f"Czy k1 == k3? {k1 == k3}")  
print(f"Czy k1 < k2? {k1 < k2}")    
print(f"Czy k2 > k1? {k2 > 100}")    
print(f"Czy k2 > k2? {k1 > k2}")   