#Job01
#def My_print_hello():
#    print("Hello world")
#My_print_hello()

#Job02
#def My_print_name(name):
#   print(name)
#My_print_name("Messi")
#My_print_name("Karim Benzema")
#My_print_name("Ronaldo")

#Job03
#def add(a,b):
#    print(a+b)
#add(1,2)
#add(15,25)
#add(45,2)

#Job04
#def GetHello():
#    return "Hello la Plateforme"
#print(GetHello())

#Job05

#def calcul(num1,operator,num2):
#    if operator == "+":
#        return num1 + num2
#    elif operator == "*":
#        return num1 * num2
#    elif operator == "-":
#        return num1 - num2
#    elif operator == "/":
#        return num1 / num2
#    elif operator  == "%":
#        return num1 % num2
#    else : 
#        return "Entrez un opérateur correct"
#print(calcul(15,"*",2))

#Job06
#def nombre(nombre):
#    if nombre > 0:
#        print("Le nombre est positif")
#    else :
#        print("Le nombre est négatif")
#nombre(-1)
#nombre(15)
#nombre(-6)

#Job07
#def langue(langage : str ):
#    if langage == "javascript":
#        print("tu es un développeur web")
#    elif langage == "python":
#        print("tu es un développeur IA")
#    elif langage == "java":
#        print("tu es un développeur logiciel")
#    elif langage == "reactjs":
#        print("tu es un développeur mobile")
#    else : 
#        print("un jour, je serai le meilleur développeur...")
#langue(langage="java")

#Job08
#def ma_fonction(type,saison):
#    if type == "fruits" and saison == "hiver":
#        print("orange, mandarine et kiwi")
#    elif type == "fruits" and saison == "été":
#        print("Poire, fraise, cassis")
#    elif type == "légumes" and saison == "hiver":
#        print("carotte, topinambour, endive")
#    elif type == "légumes" and saison == "été":
#        print("artichaut, aubergine,navet")
#    else : 
#        print("NONE")
#ma_fonction(type="légumes",saison="été")

#Job09
#def moyenne(note1 = int(input("Entrez votre premiere note : ")),note2 = int(input("Entrez votre deuxieme note : ")),note3 = int(input("Entrez votre note3 : "))):
#    return (note1 + note2+ note3) / 3
#moyenne_etudiant = moyenne()
#if moyenne_etudiant > 15 and moyenne_etudiant<20:
#    print(moyenne_etudiant,"Très bon élève")
#elif moyenne_etudiant <= 14 and moyenne_etudiant>11:
#    print(moyenne_etudiant,"bon élève")
#elif moyenne_etudiant <= 8 and moyenne_etudiant>10:
#    print(moyenne_etudiant,"Élève moyen")
#else : 
#    print(moyenne_etudiant,"Élève devant faire des efforts")

#Job10
#def nbre(nombre):
#    if nombre % 2 == 0 and nombre > 0 and nombre % 1 == 0  :
#            print("Le nombre est pair")
#    elif nombre > 0 and nombre % 1 == 0 : 
#            print("Le nombre est inpair")
#    else : 
#           print("Rentre un nbre")
#nbre(-2)

#Job11
#def time_to_text(nbre : int):
#    print(nbre // 60 , "heures",nbre % 60 ,"minutes")
#time_to_text(50)