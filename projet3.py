#Job01
valeur1=input("Entrez une valeur : ")
valeur2=input("Entrez une valeur : ")
if valeur1 == valeur2 :
    print ("Valeur1 est égal à valeur2")
else : 
    print("Les deux valeurs ne sont pas égales")

#Job02
age=80
if age >= 18 :
    print("Tu peux voter")
else : 
    print("Tu ne peux pas voter")

#Job03
for i in range (0,101) :
    if i == 26 :
        continue
    elif i == 37 : 
        continue
    elif i == 88 :
       continue
    else :
        print(i)


#Job04
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

#Job05
for nbre in range(1000):
    if nbre >1 :
        for i in range(2,nbre):
            if (nbre % i) ==0 :
                break
        else:
                print(nbre)


#Job06
nbre = int(input("Entrez un nombre: "))
if nbre % 2 == 0 :
    print ("Le nombre",nbre,"est pair")
else : 
    print ("Le nombre",nbre,"est inpair")

#Job07
chaine = "abcdefghijklmnopqrstuvwxyz" *10
i=1  
while i <= len(chaine) : 
	print(chaine[0:i])
	i = i + 1
	

#Job08
a = int(input("Entrez une longueur A : "))
b = int(input("Entrez une longueur B : "))
c = int(input("Entrez une longueur C : "))
if (a+b) > c and (a+c) > b and (b+c) > a :
    print ("Il est possible de construire un triangle.")
    if b*c**2 == a*b**2 + a*c**2 or a*c**2 == a*b**2 + b*c**2 or b*c**2 == a*b**2 + a*c**2 : 
        print ("Le triangle est rectangle")
    elif a == b or b == c or a==c :
        print ("Le triangle est isocèle")
    elif b*c**2 == a*b**2 + a*c**2 or a*c**2 == a*b**2 + b*c**2 or b*c**2 == a*b**2 + a*c**2 and a == b or b == c or a==c: 
        print ("Le triangle rectangle et isocèle")
    elif a == b == c: 
        print ("le triangle est équilatéral")
    else : 
        print ("Le triangle est quelconque")
else : 
    print ("Il n'est pas possible de construire un triangle.")