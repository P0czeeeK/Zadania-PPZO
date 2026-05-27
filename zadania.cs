// Online C# Editor for free
// Write, Edit and Run your C# code using C# Online Compiler

using System;

public class HelloWorld
{
    static int zadanie1()
    {
        Console.WriteLine("Podaj pierwszą liczbę: ");
        int a = int.Parse(Console.ReadLine());
        Console.WriteLine("Podaj drugą liczbę: ");
        int b = int.Parse(Console.ReadLine());
        Console.WriteLine("Podaj działanie które chcesz wykonać: ");
        string dzialanie = Console.ReadLine();
        
        
        if(dzialanie == "+"){
            return(a+b);
        }
        else if(dzialanie == "-"){
            return(a-b);
        }
        else if(dzialanie == "*"){
            return(a*b);
        }
        else if(dzialanie == "/"){
            return(a/b);
        }
        else{
            Console.WriteLine("Nie ma takiego działania");
            return(0);
        }
    }
    
        static double zadanie2()
    {
        Console.WriteLine("Wybierz jednostkę z której chcesz przeliczać (F/C): ");
        string skala = Console.ReadLine(); 
        Console.WriteLine("Podaj temperaturę w podanej jednostce: ");
        double temp = double.Parse(Console.ReadLine());
        if(skala == "C"){
            return((temp*1.8)+32);
        }
        else if(skala == "F"){
            return((temp-32)/1.8);
        }
        else{
            Console.WriteLine("Nie ma takiej skali");
            return 0;
        }
    }
    
    public static void Main(string[] args)
    {
        Console.WriteLine("Podaj zadanie które chcesz wybrać: ");
        int zadanie = int.Parse(Console.ReadLine());
        switch(zadanie)
        {
            case 1:
                Console.WriteLine(zadanie1());
                break;
            case 2:
                Console.WriteLine(zadanie2());
                break;
            default:
                Console.WriteLine("Nie ma takiej opcji");
                break;
        }
    }
}