class FuelTank:
    def __init__(self, level, capacity):
        self.capacity = capacity
        self.level_wewn = level

    @property
    def level_wewn(self):
        return self._level
    
    @level_wewn.setter
    def level_wewn(self, wartosc):
        if wartosc > self.capacity:
            self._level = self.capacity
            print(f"Zbiornik nie zmiesci wiecej niz:{self.capacity}")
        
        elif wartosc < 0:
            self._level = 0
        
        else: self._level = wartosc

    def drive(self, distance):
        self.level_wewn = self.level_wewn - (distance * 0.5)
    
    @property
    def range(self):
        pozostalo = self._level * 2
        return f"Zasieg {pozostalo}km"
    

zbiornik1 = FuelTank(70, 100)
print(zbiornik1.range)
zbiornik1.drive(20)
print(zbiornik1.range)
zbiornik1.level_wewn = 120


    
