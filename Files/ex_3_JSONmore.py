import json

imie = "Damian"
dokument = "dane.json"

try:
   with open(dokument, "r") as plik:
         lista_imion = json.load(plik)
except (FileNotFoundError, json.JSONDecodeError):
     lista_imion = []
finally: print("Operacja zakończona")


lista_imion.append(imie)

with open(dokument, "w") as plik:
      json.dump(lista_imion, plik, indent=4)
