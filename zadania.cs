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
    
    public static void Main(string[] args)
    {
        Console.WriteLine("Podaj zadanie które chcesz wybrać: ");
        int zadanie = int.Parse(Console.ReadLine());
        switch(zadanie)
        {
            case 1:
                Console.WriteLine(zadanie1());
                break;
            default:
                Console.WriteLine("Nie ma takiej opcji");
                break;
        }
    }
}