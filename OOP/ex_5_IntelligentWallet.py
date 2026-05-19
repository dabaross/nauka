class Portfel:
    def __init__(self, balans = 0):
        
        self.history_this = []
        self.balans_this = balans

    @property
    def balans_this(self):
        return self._balans 
    
    @balans_this.setter
    def balans_this(self, wartosc):
        if wartosc < 0:
            print(f"Za małe saldo: {self._balans}")
    
        else: self._balans = wartosc

    def wydaj(self, kwota):
        self.balans_this = self.balans_this - kwota
        self.history_this.append(f"- {kwota}")
    
    def wplac(self, kwota):
        self.balans_this = self.balans_this + kwota
        self.history_this.append(f" {kwota}")
    
    def __eq__(self, other):
        if not isinstance(other, Portfel):
            return False
        return self._balans == other._balans
    
    def __lt__(self, other):
        return self._balans < other._balans
    
    def __len__(self):
        return len(self.history_this)
    
    def __getitem__(self, key):
        return self.history_this[key]
    
p = Portfel()
p.wplac(200)
p.wydaj(50)
p.wplac(100)

print(f"Stan konta: {p.balans_this}")      # Powinno być 250
print(f"Liczba operacji: {len(p)}")   # Powinno być 3
print(f"Druga operacja: {p[1]}")      # Powinno być -50

