'''
text = "Anna, Paweł, Anna"
lista = text.split(", ")
print(text)
print(lista)
print(type(lista))

imie1=lista[0]
print(imie1)

print("Twoje imie: ",imie1)

imieduze=imie1.upper()
print(imieduze)
imiemale=imie1.lower()
print(imiemale)

#sprawdzenie zawartosci
print("Podaj swoje nazwisko: ", end="")
nazwisko = input()

zawartosc = nazwisko.isalpha() # sprawdza czy zawartosc jest pusta
print(zawartosc)
#sprawdzić dlaczego przy liczbach jest FALSE
#Liczba + cokolwiek = FALSE

text1="Julia\n"
text2="Nowak"
print(text1+text2)

text1=text1.rstrip()   #usuwanie znaków(spacje,tab,itd.) z prawej strony
print(text1+text2)

print(text1+" "+text2)
'''
#Wyswietlanie łańcucha znaków

text3 = "%s, Java i %s" % ("PHP","PYTHON")
print(text3)

text4= "{1}, JAVA i {0}".format("PHP","PYTHON")
print(text4)

#help(text.replace)

new=text4.replace("PHP", "C#")
print(new)

rok = 2019
miesiac = "marzec"
dzien = 25
print("Data: ", end="")
print(dzien,miesiac,rok)
print("Data: ", end="")
print(dzien,miesiac,rok,sep="-")
