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
            print(f"You can't harvest {self.plant_name} in {weather.getMonth()}")
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
            print(f"You can't plant {self.plant_name} in {weather.getMonth()}")

    def grow(self, weather):
        if self.is_occupied:
            if weather.getWeather() == "sunny":
                self.growth += 2
            elif weather.getWeather() == "rainy":
                self.growth += 3
            else:
                self.growth += 1



class Barn:
#Zapasy, magazyn, sprzedaż, kasa
    def __init__(self):
        self.money = 0
        self.silo = 0

    # def whatFieldIHave(self):
    #     print("Fields that you have: ")
    #     for i in self.field_list:
    #         print(self.field_list[i], ", ")

    def howMuchMoneyYouHave(self):
        return self.money
    
    def addToSilo(self, amount):
        self.silo += amount
        print(f"Silo now contains: {self.silo}")

    def sell(self):
        earned = self.silo*5
        self.money += earned
        print(f"Sold crops for {earned}$")
        self.silo = 0

class Field:
    #Numer pola, czy jest nasze, ile m3 zbiorów
    def __init__(self, field_number):
        self.field_number = field_number
        self.crop = None
    
    # def fieldBuy():
    #     pass

    # def isItYourField(self):
    #     if(self.field_number in self.barn.field_list):
    #         return True
    #     else:
    #         return False

    def plantCrop(self, crop, weather):
        if self.crop and self.crop.is_occupied:
            print("Field is already planted")
            return
        
        self.crop = crop
        crop.planting(weather)

    def harvestCrop(self, weather):
        if not self.crop:
            print("Nothing planted here")
            return 0
        
        return self.crop.harvest(weather)
    
    def update(self, weather):
        if self.crop:
            self.crop.grow(weather)


class Weather:
#Dzień, miesiąc, pora roku, pogoda
    def __init__(self):
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
    
    def getWeather(self):
        return self.what_weather
    
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
    
# class Animal:
# #Rodzaj, pokarm, zbiory
#     def __init__(self, animal_name, what_eating, is_hungry):
#         pass    

class Farm:
    #Śpij dzień zmiana miesiąca i pogody, śpij 6h zmiana pogody, zboża
    def __init__(self):
        self.weather = Weather()
        self.barn = Barn()
        self.fields = [Field(1), Field(2)]

    def nextDay(self):
        print("----------------------New Day----------------------")
        self.weather.sleep()

        for field in self.fields:
            field.update(self.weather)

        print(f"Month: {self.weather.getMonth()}, Weather: {self.weather.getWeather()}")

    def plant(self, field_number, crop):
        field = self.fields[field_number - 1]
        field.plantCrop(crop, self.weather)

    def harvest(self, field_number):
        field = self.fields[field_number - 1]
        amount = field.harvestCrop(self.weather)
        self.barn.addToSilo(amount)


farm = Farm()

farm.nextDay()
farm.nextDay()

wheat = Crop("Wheat", ["August", "September"], ["March", "April"])

farm.plant(1, wheat)

for i in range(5):
    farm.nextDay()

farm.harvest(1)
farm.barn.sell()
