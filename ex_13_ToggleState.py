class Bezpiecznik:
    def __init__(self, func):
        self.uzbrojony = False
        self.pompa = func
    def __call__(self):
        if self.uzbrojony == False:
            self.uzbrojony = True
            print("pompa uzbrojona, nastepne wywolanie ja uruchomi")
        elif self.uzbrojony == True:
            print("Uruchamiam pompe")
            self.uzbrojony = False
            self.pompa()

@Bezpiecznik
def uruchom_pompe():
    print("pompa dziala")
        

uruchom_pompe()
uruchom_pompe()
uruchom_pompe()