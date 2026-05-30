using System;
using System.Collections.Generic;

class Crop
{
    public string PlantName { get; set; }
    public List<string> HarvestTime { get; set; }
    public List<string> PlantingTime { get; set; }
    public bool IsOccupied { get; set; }
    public int Growth { get; set; }

    public Crop(string plantName, List<string> harvestTime, List<string> plantingTime)
    {
        PlantName = plantName;
        HarvestTime = harvestTime;
        PlantingTime = plantingTime;
        IsOccupied = false;
        Growth = 0;
    }

    public int Harvest(Weather weather)
    {
        if (!IsOccupied)
        {
            Console.WriteLine("On the field is nothing grow");
            return 0;
        }

        if (!HarvestTime.Contains(weather.GetMonth()))
        {
            Console.WriteLine($"You can't harvest {PlantName} in {weather.GetMonth()}");
            return 0;
        }

        if (Growth < 10)
        {
            Console.WriteLine($"{PlantName} is not ready yet");
            return 0;
        }

        Console.WriteLine($"Harvested {PlantName}!");
        IsOccupied = false;
        return 10;
    }

    public void Planting(Weather weather)
    {
        if (PlantingTime.Contains(weather.GetMonth()))
        {
            IsOccupied = true;
            Growth = 0;
            Console.WriteLine($"You plant {PlantName}");
        }
        else
        {
            Console.WriteLine($"You can't plant {PlantName} in {weather.GetMonth()}");
        }
    }

    public void Grow(Weather weather)
    {
        if (IsOccupied)
        {
            string w = weather.GetWeather();
            if (w == "sunny") Growth += 2;
            else if (w == "rainy") Growth += 3;
            else Growth += 1;
        }
    }
}

class Barn
{
    public int Money { get; set; }
    public int Silo { get; set; }

    public Barn()
    {
        Money = 0;
        Silo = 0;
    }

    public void AddToSilo(int amount)
    {
        Silo += amount;
        Console.WriteLine($"Silo now contains: {Silo}");
    }

    public void Sell()
    {
        int earned = Silo * 5;
        Money += earned;
        Console.WriteLine($"Sold crops for {earned}$");
        Silo = 0;
    }
}

class Field
{
    public int FieldNumber { get; set; }
    public Crop Crop { get; set; }

    public Field(int fieldNumber)
    {
        FieldNumber = fieldNumber;
        Crop = null;
    }

    public void PlantCrop(Crop crop, Weather weather)
    {
        if (Crop != null && Crop.IsOccupied)
        {
            Console.WriteLine("Field is already planted");
            return;
        }

        if (crop.PlantingTime.Contains(weather.GetMonth()))
        {
            crop.Planting(weather);
            Crop = crop;
        }
        else
        {
            Console.WriteLine("Wrong month for planting");
        }
    }

    public int HarvestCrop(Weather weather)
    {
        if (Crop == null)
        {
            Console.WriteLine("Nothing planted here");
            return 0;
        }

        return Crop.Harvest(weather);
    }

    public void Update(Weather weather)
    {
        Crop?.Grow(weather);
    }
}

class Weather
{
    private string currentWeather;
    private string[] monthList =
    {
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    };

    private int currentMonth;

    public Weather()
    {
        currentWeather = "sunny";
        currentMonth = 0;
    }

    public void Sleep()
    {
        currentMonth = (currentMonth + 1) % 12;
        WeatherChange();
    }

    public void WeatherChange()
    {
        string[] options = { "sunny", "rainy", "windy", "stormy" };
        Random r = new Random();
        currentWeather = options[r.Next(options.Length)];
    }

    public string GetMonth()
    {
        return monthList[currentMonth];
    }

    public string GetWeather()
    {
        return currentWeather;
    }
}

class Animal
{
    public string AnimalName { get; set; }
    public bool IsHungry { get; set; }

    public Animal(string name)
    {
        AnimalName = name;
        IsHungry = false;
    }

    public void Feed(Barn barn)
    {
        if (barn.Silo > 0)
        {
            barn.Silo -= 1;
            IsHungry = false;
            Console.WriteLine($"You feeded your {AnimalName}");
        }
        else
        {
            Console.WriteLine("No food in silo");
        }
    }
}

class Farm
{
    public Weather Weather { get; set; }
    public Barn Barn { get; set; }
    public Animal Animal { get; set; }
    public List<Field> Fields { get; set; }

    public Farm()
    {
        Weather = new Weather();
        Barn = new Barn();
        Animal = new Animal("Cows");
        Fields = new List<Field> { new Field(1), new Field(2) };
    }

    public void NextDay()
    {
        Console.WriteLine("----------------------New Day----------------------");
        Weather.Sleep();
        Animal.IsHungry = true;

        foreach (var field in Fields)
            field.Update(Weather);

        Console.WriteLine($"Month: {Weather.GetMonth()}, Weather: {Weather.GetWeather()}");
    }

    public void Plant(int fieldNumber, Crop crop)
    {
        Fields[fieldNumber - 1].PlantCrop(crop, Weather);
    }

    public void Harvest(int fieldNumber)
    {
        int amount = Fields[fieldNumber - 1].HarvestCrop(Weather);
        Barn.AddToSilo(amount);
    }

    public void ShowFields()
    {
        for (int i = 0; i < Fields.Count; i++)
            Console.WriteLine($"Field {i + 1}");
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Write your name: ");
        string name = Console.ReadLine();

        Console.Write("Write your farm name: ");
        string farmName = Console.ReadLine();

        Farm farm = new Farm();
        Console.WriteLine($"\nWelcome {name} on your farm {farmName}");

        GameMenu(farm);
    }

    static void GameMenu(Farm farm)
    {
        while (true)
        {
            Console.WriteLine("\n--------------------------- FARM MENU ---------------------------");
            Console.WriteLine("1. Plant crop");
            Console.WriteLine("2. Harvest crop");
            Console.WriteLine("3. Feed animals");
            Console.WriteLine("4. Show farm status");
            Console.WriteLine("5. Sleep (next day)");
            Console.WriteLine("0. Exit");

            int choice = int.Parse(Console.ReadLine());

            if (choice == 1)
            {
                Console.WriteLine("Which field do you want to plant?");
                farm.ShowFields();
                int fieldNumber = int.Parse(Console.ReadLine());

                Console.Write("Which crop you want to plant? (Wheat/Oak/Corn): ");
                string cropName = Console.ReadLine();

                Crop crop = cropName switch
                {
                    "Wheat" => new Crop("Wheat",
                        new List<string> { "June", "July", "August" },
                        new List<string> { "September", "October" }),

                    "Oak" => new Crop("Oak",
                        new List<string> { "July", "August" },
                        new List<string> { "March", "April" }),

                    "Corn" => new Crop("Corn",
                        new List<string> { "October", "November" },
                        new List<string> { "April", "May" }),

                    _ => null
                };

                if (crop == null)
                {
                    Console.WriteLine("Unknown crop");
                    continue;
                }

                farm.Plant(fieldNumber, crop);
            }
            else if (choice == 2)
            {
                Console.WriteLine("Which field do you want to harvest?");
                farm.ShowFields();
                int fieldNumber = int.Parse(Console.ReadLine());
                farm.Harvest(fieldNumber);
            }
            else if (choice == 3)
            {
                if (farm.Animal.IsHungry)
                    farm.Animal.Feed(farm.Barn);
                else
                    Console.WriteLine($"Your {farm.Animal.AnimalName} are not hungry");
            }
            else if (choice == 4)
            {
                ShowFarmStatus(farm);
            }
            else if (choice == 5)
            {
                farm.NextDay();
            }
            else if (choice == 0)
            {
                Console.WriteLine("Thanks for playing!");
                break;
            }
            else
            {
                Console.WriteLine("Invalid option");
            }
        }
    }

    static void ShowFarmStatus(Farm farm)
    {
        Console.WriteLine("\n--------------------------- FARM STATUS ---------------------------");
        Console.WriteLine($"Month: {farm.Weather.GetMonth()}");
        Console.WriteLine($"Weather: {farm.Weather.GetWeather()}");
        Console.WriteLine($"Silo: {farm.Barn.Silo}");
        Console.WriteLine($"Money: {farm.Barn.Money}");

        Console.WriteLine("\nFields:");
        foreach (var field in farm.Fields)
        {
            if (field.Crop != null && field.Crop.IsOccupied)
                Console.WriteLine($" Field {field.FieldNumber}: {field.Crop.PlantName}, growth {field.Crop.Growth}/10");
            else
                Console.WriteLine($" Field {field.FieldNumber}: empty");
        }

        Console.WriteLine("\nAnimals:");
        Console.WriteLine(farm.Animal.IsHungry
            ? $"Your {farm.Animal.AnimalName} are hungry"
            : $"Your {farm.Animal.AnimalName} is feeded");
    }
}
