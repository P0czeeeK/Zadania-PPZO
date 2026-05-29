#Gra Symulator farmy – klasy Crop, Animal, Barn, Farm, Weather; sadzenie/zbiór roślin, 
# karmienie zwierząt, zmienna pogoda wpływająca na plony.
import random

class Crop:
#Stan wzrotu, nazwa, pora zbiorów, numer pola, zbiory, sadzenie
    def __init__(self, plant_name):
        self.plant_name = plant_name,
        self.harvest_time = [],
        self.planting_time = [],
        self.is_occupied = False

    def harvest(self, field_number, is_harvest_time, is_weather, silo_number, is_occupied):
        #Sprawdzenie czy pora roku i pogoda pozwala na zebranie i zbiory
        pass

    def planting(self, field_number, is_harvest_time, is_weather, is_occupied):
        #Sprawdzenie czy na polu coś rośnie i czy jest pora roku i pogoda na zasadzenie
        pass


class Animal:
#Rodzaj, pokarm, zbiory
    def __init__(self, animal_name, what_eating, is_hungry):
        pass

class Barn:
#Zapasy, magazyn, sprzedaż
    pass

class Weather:
#Dzień, miesiąc, pora roku, pogoda
    def __init__(self, mounth, season):
        self.mounth = mounth,
        self.season = season,
        self.what_weather = "sunny"

    def weather_change(self):
        self.what_weather = random.choice(["sunny", "rainy", "windy", "stormy"])

    
    

class Farm:
    pass