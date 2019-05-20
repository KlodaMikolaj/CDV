#pętle zadania

#Podaj wartosc poczatkowa i koncowa ktora bedzie wypisana w porzadku malejacym.
'''
a=int(input("Podaj wartosc a: "))
b=int(input("Podaj wartosc b: ")) -1

if b >= a:
    x=a
    a=b + 1
    b=x - 1


for c in range(a , b , -1):
    print(c)


a=int(input("Podaj wartosc a: "))+1

for x in range(a):
    for y in range (x):
        print("*",end="")
    print("")

for x in range(a):
    print(x*"*",end="")
    print("")


#zad1

a=float(input("Podaj wartosc A: "))
sumaa=a*a+b
b=float(input("Podaj wartosc B: "))
sumab=(a*a)+(2*a*b)+(b*b)
if sumab == 0:
    print("Proba dzielenia przez 0")
else:
    wynik=sumaa/sumab
    print("Wynik wyrazenia to: ",wynik)


for letter in "CDV - uczelnia ludzi ciekawych":
    if letter == "V":
        continue
    print(f'Litera: {letter}',end=" ")

'''


#uzytkowanik podaje haslo z klawiatury / jesli poda haslo okon to na ekranie wyswietlamy na ekranie komunikat poprawne haslo / uzytkownik ma na podanie hasla 3 proby / jesli przekroczy ilosc prob to ma sie wyswieltlic komunikat przekroczono limit prob podania hasla
a=0
while a<3:
    haslo=input("Podaj haslo: ")
    if haslo == 'okon':
        print("Haslo poprawne")
        break;
    a+=1
if a==3:
    print("Przekroczono maksymalna ilosc prob")








