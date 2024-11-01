#Créez un programme qui affiche dans le terminal l’alphabet.
import string 
alphabet = list(string.ascii_lowercase)
print (alphabet)

#Créez un programme qui affiche dans le terminal l’alphabet à l’envers.
import string        
alphabet = list(string.ascii_lowercase)
alphabetinverse = alphabet[::-1]
print (alphabetinverse)

#Créez un programme qui stocke la phrase « Je suis une String » dans une variable nommée « ma_string », puis affichez cette variable dans le terminal.
ma_string = "Je suis une String" 
print(ma_string)

#Créez un programme qui affiche dans le terminal la somme des variables «num1 » et « num2 ». Assignez la valeur « 40 » à « num1 » et la valeur « 2 » à «num2 ».
numl = 40
num2 = 2
print(numl + num2)

#Créez un programme qui affiche dans le terminal le produit des variables «num1 » et « num2 ». Assignez la valeur de « 3 » à « num1 » et la valeur « 14 » à «num2 ».
num1=3
num2=14
print(num1*num2)

#Job09
nom = str(input("le nom du produit : "))
prixunitaire = 16
quantitéenstock = 0
quantiteacheter = int(input("Saisir la quantité de produits que vous souhaitez acheter : "))
quantitéenstock = quantitéenstock + quantiteacheter
prixunitaire = prixunitaire * 0.1
print("Nom = ",nom,",","Prix =" ,prixunitaire,",","Quantité en stock=",quantitéenstock)

produit1 = ["Iphone","1000","2"]
produit2 = ["Samsung","500","2"]
produit = produit1 + produit2
print (produit)

#2 eme version du job 9 
prixunitaire1 = float(produit1[1]) 
prixunitaire2 = float(produit2[1])
quantiteenstock1 = int(produit1[2])
quantiteenstock2 = int(produit2[2])
print(prixunitaire1,quantiteenstock1)
nomproduit = str(input("Entrez le produit que vous souhaitez: "))
if nomproduit in produit1 and quantiteenstock1 != 0 : 
    quantitevoulu = int(input("Entrer la quantité de produit que vous souhaitez: "))
    if quantitevoulu <= quantiteenstock1  :
        print(quantitevoulu * prixunitaire1)
        print("Prix = ",quantitevoulu * prixunitaire1 + prixunitaire1 * 0.1)
    elif quantitevoulu > quantiteenstock1 :
        print("Pas en stock")

elif nomproduit in produit2 and quantiteenstock2 != 0 : 
    quantitevoulu2 = int(input("Entrer la quantité de produit que vous souhaitez: "))
    if quantitevoulu2 <= quantiteenstock2:
        print(quantitevoulu2 * prixunitaire2)
        print("Prix = ", quantitevoulu2 * prixunitaire2)
    elif quantitevoulu2 > quantiteenstock2 :
        print("Pas en stock")
else :
    print ("le produit n'est pas en stock")


#Job10
montantinitial = int(input("Enter le montant initial de l’investissement : "))
tauxannuel = int(input("Entrez le taux de rendement annuel : "))
gainannuel = montantinitial * tauxannuel/100
print ("le gain annuel en fonction du taux de rendement est ",gainannuel)

montantinitial = montantinitial + 5000
tauxannuel = tauxannuel * 0.2
print ("le gain de l’investisseur est", montantinitial * tauxannuel)

montantinitial = montantinitial / 0.1 
tauxannuel = tauxannuel / 0.01
print("le montant final de l’investissement",montantinitial,"le nouveau gain est", montantinitial * tauxannuel)

#Écrivez un script qui détermine si une chaîne contient ou non le caractère "e"
Chaine = str(input("Entrer un phrase : "))
lettre = "e"
if lettre in Chaine:
    print("La phrase" )
else :
    print("Non")