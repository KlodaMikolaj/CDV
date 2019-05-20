#listy
programowanie=['PHP','Java','Python']
print(type(programowanie)) #class 'list'
programowanie.append('C#')
programowanie.append('PHP')
print(programowanie)
ile=programowanie.count("PHP")
print(f'PHP wystepuje {ile} razy')


###tuple
imiona={'julia','ania','tomek'}
print(type(imiona))
print(imiona)
firstname=imiona[0]
print(f'First name: {First Name}')

#słownik
osoba={
    'imie':'Janusz',
    'nazwisko':'Nowak',
    'miasto':'Poznan',
    'wiek':20,
    'umowaoprace':True
}
print(type(osoba)) #class<'dict'>
print(osoba)
print(osoba['miasto'])
print(osoba.get('xyz','Brak Klucza'))
print(osoba.get('imie','Brak Klucza'))
print(osoba.keys())

#direct_keys
