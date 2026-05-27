def zadanie1():
            a = int(input("Podaj pierwszą liczbę: "))
            b = int(input("Podaj drugą liczbę: "))
            dzialanie = input("Podaj działanie jakie chcesz wykonać")

            if(dzialanie == "+"):
                print(a+b)
                return
            elif(dzialanie == "-"):
                print(a-b)
                return
            elif(dzialanie == "*"):
                print(a*b)
                return
            elif(dzialanie == "/"):
                print(a/b)
                return
            else:
                print("Nie ma takiego działania")
                return
            
def zadanie2():
    wybor_skali = input("Wybierz jednostkę z której chcesz przeliczać (F/C): ")
    stopnie = float(input("Podaj ile jest stopni w podanej skali: "))
    if(wybor_skali == "C"):
        print((stopnie*1.8)+32)
        return
    elif(wybor_skali == "F"):
        print((stopnie-32)/1.8)
        return
    else:
         print("Nie ma takiej opcji")
         return


x = int(input("Które zadanie chcesz wybrać: "))
def wybor_zadania(x):
    match x:
        case 1:
            return zadanie1()
        case 2:
            return zadanie2()
        case _:
            print("Nie ma takiego zadania")
            return

wybor_zadania(x)