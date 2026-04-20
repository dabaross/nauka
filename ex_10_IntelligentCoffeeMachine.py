def dodaj_bonus(fun):
    def wrapper(self, rodzaj_kawy, cukier):
        if rodzaj_kawy == "Premium":
            rodzaj_kawy = "Królewska Premium"
        return fun(self, rodzaj_kawy, cukier)
    return wrapper

class Ekspres:
    def __init__(self, model):
        self.model = model
    
    @dodaj_bonus
    def parz_kawe(self, rodzaj_kawy, cukier):
        return f"Parze {rodzaj_kawy} z {cukier} lyzeczkami cukru"

    def czysc_maszyne(self):
        pass



ekspres = Ekspres("delonghi")
print(ekspres.parz_kawe("Premium", 10))
print(ekspres.parz_kawe("Zajebista", 1))