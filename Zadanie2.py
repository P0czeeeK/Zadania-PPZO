#Gra Symulator farmy – klasy Crop, Animal, Barn, Farm, Weather; sadzenie/zbiór roślin, 
# karmienie zwierząt, zmienna pogoda wpływająca na plony.
import random


class Crop:
#Stan wzrotu, nazwa, pora zbiorów, numer pola, zbiory, sadzenie
    def __init__(self, plant_name):
        self.plant_name = plant_name,
        self.harvest_time = [],
        self.planting_time = [],
        self.is_occupied = False,
        self.weather = Weather(),
        self.barn = Barn()

    def harvest(self, field_number, is_harvest_time, is_weather, silo_number, is_occupied):
        #Sprawdzenie czy pora roku i pogoda pozwala na zebranie i zbiory
        if(self.weather.getMonth in self.harvest_time):
            pass
        else:
            print(f"You can't harvest in {self.weather.getSeason}")

    def planting(self, field_number, is_harvest_time, is_weather, is_occupied):
        #Sprawdzenie czy na polu coś rośnie i czy jest pora roku i pogoda na zasadzenie
        if(self.weather.getMonth in self.planting_time):
            pass
        else:
            print(f"You can't plant in {self.weather.getSeason}")

class Animal:
#Rodzaj, pokarm, zbiory
    def __init__(self, animal_name, what_eating, is_hungry):
        pass

class Barn:
#Zapasy, magazyn, sprzedaż, kasa
    def __init__(self):
        self.field = Field()
        self.field_list = []
        self.money = 50000

    def whatFieldIHave(self):
        print("Fields that you have: ")
        for i in self.field_list:
            print(self.field_list[i], ", ")

    def HowMuchMoneyYouHave(self):
        return self.money

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
        self.month = month,
        self.season = season,
        self.what_weather = "sunny"
        self.month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        self.current_month = 0

    def weather_change(self):
        self.what_weather = random.choice(["sunny", "rainy", "windy", "stormy"])

    def sleep(self):
        self.current_month = (self.current_month + 1) % 12
    
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
    pass