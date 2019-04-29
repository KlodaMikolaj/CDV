programowanie=['c','c#','php','java','r']
print(programowanie)
print(type(programowanie))

first = programowanie[0]
print(first)
last = programowanie[-1]
print(last)
element3=programowanie[0:3]
print(element3)
programowanie.append('c++')
print(programowanie)


#ZLICZANIE ELEMENTOW W LISCIE
ile = programowanie.count('c++')
print(ile)
programowanie.append('c++')
ile = programowanie.count('c++')
print(ile)

#łaczenie list
jezyki = ['c','c++']
programowanie.extend(jezyki)
print(programowanie)

#wyczyszczenie listy
nowa = programowanie
print(id(programowanie))
print(id(nowa))
nowa.append('Go');
print(nowa)
print(programowanie)

nowa.clear()
print(nowa)
print(programowanie)
