class SygnalPozaZakresemError(Exception):
    pass

def waliduj_rssi(func):
    def wrapper(self, rssi):
        if rssi > 0:
            raise SygnalPozaZakresemError("Sygnał nie moze byc dodatni!")
        return func(self, rssi)
    return wrapper

class SensorWifi():
    odczyty = []
    def __init__(self):
        pass    

    @waliduj_rssi
    def zapisz_odczyt(self, rssi):
        odczyt = rssi
        self.odczyty.append(odczyt)



    
try:
    sensor = SensorWifi()
    sensor.zapisz_odczyt(10)
except SygnalPozaZakresemError as e:
    print(f"Błąd {e}")
