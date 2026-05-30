#Gra Symulator farmy – klasy Crop, Animal, Barn, Farm, Weather; sadzenie/zbiór roślin, 
# karmienie zwierząt, zmienna pogoda wpływająca na plony.
import random


class Crop:
#Stan wzrotu, nazwa, pora zbiorów, numer pola, zbiory, sadzenie
    def __init__(self, plant_name, harvest_time, planting_time):
        self.plant_name = plant_name
        self.harvest_time = harvest_time
        self.planting_time = planting_time
        self.is_occupied = False
        self.growth = 0

    def harvest(self, weather):
        #Sprawdzenie czy pora roku i pogoda pozwala na zebranie i zbiory
        if not self.is_occupied:
            print("On the field is nothing grow")
            return 0
        
        if weather.getMonth() not in self.harvest_time:
            print(f"You can't harvest {self.plant_name} in {weather.getSeason()}")
            return 0
        
        if self.growth < 10:
            print(f"{self.plant_name} is not ready yet")
            return 0
        
        print(f"Harvested {self.plant_name}!")
        self.is_occupied = False
        return 10

    def planting(self, weather):
        #Sprawdzenie czy na polu coś rośnie i czy jest pora roku i pogoda na zasadzenie
        if(weather.getMonth() in self.planting_time):
            self.is_occupied = True
            self.growth = 0
            print(f"You plant {self.plant_name}")
        else:
            print(f"You can't plant {self.plant_name} in {weather.getSeason()}")

class Animal:
#Rodzaj, pokarm, zbiory
    def __init__(self, animal_name, what_eating, is_hungry):
        pass

class Barn:
#Zapasy, magazyn, sprzedaż, kasa
    def __init__(self):
        self.field = Field()
        self.crop = Crop()
        self.field_list = []
        self.crop_list = ["Wheat", "Oat", "Corn"]
        self.money = 0
        self.silo = 0

    def whatFieldIHave(self):
        print("Fields that you have: ")
        for i in self.field_list:
            print(self.field_list[i], ", ")

    def howMuchMoneyYouHave(self):
        return self.money
    
    def harvestToSilo(self):
        

class Field:
    #Numer pola, czy jest nasze, ile m3 zbiorów
    def __init__(self, field_number):
        self.field_number = field_number
        self.barn = Barn()
    
    def fieldBuy():
        pass

    def isItYourField(self):
        if(self.field_number in self.barn.field_list):
            return True
        else:
            return False


class Weather:
#Dzień, miesiąc, pora roku, pogoda
    def __init__(self, month, season):
        self.month = month
        self.season = season
        self.what_weather = "sunny"
        self.month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.current_month = 0

    def weather_change(self):
        self.what_weather = random.choice(["sunny", "rainy", "windy", "stormy"])

    def sleep(self):
        self.current_month = (self.current_month + 1) % 12
        self.what_weather = random.choice(["sunny", "rainy", "windy", "stormy"])
    
    def getMonth(self):
        return self.month_list[self.current_month]
    
    def getSeason(self):
        month = self.getMonth()

        winter = ["December", "January", "February"]
        spring = ["March", "April", "May"]
        summer = ["June", "July", "August"]
        autumn = ["September", "October", "November"]

        if month in winter:
            return "Winter"
        if month in spring:
            return "Spring"
        if month in summer:
            return "Summer"
        if month in autumn:
            return "Autumn"
    
    

class Farm:
    #Śpij dzień zmiana miesiąca i pogody, śpij 6h zmiana pogody, zboża
    pass