class Smartfon:
    def __init__(self, marka, poziom_baterii):
        self.marka = marka
        self.poziom_baterii_set = poziom_baterii

    @property
    def poziom_baterii_set(self):
        return f" Poziom baterii {self.marka}: {self._poziom_baterii_wewn}%"
        
    @poziom_baterii_set.setter
    def poziom_baterii_set(self, wartosc):
        if wartosc > 100:
            self._poziom_baterii_wewn = 100
            
        elif wartosc < 0:
            self._poziom_baterii_wewn = 0
        else:
            self._poziom_baterii_wewn = wartosc



tel1 = Smartfon("iPhone", 80)
print(tel1.poziom_baterii_set)
tel1.poziom_baterii_set = 120
print(tel1.poziom_baterii_set)

tel2 = Smartfon("Samsung", 120)
print(tel2.poziom_baterii_set)