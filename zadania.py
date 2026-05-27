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


x = int(input("Które zadanie chcesz wybrać: "))
def wybor_zadania(x):
    match x:
        case 1:
            return zadanie1()
        case _:
            print("Nie ma takiego zadania")
            return

wybor_zadania(x)