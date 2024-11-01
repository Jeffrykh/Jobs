#Job01
#fruits = ["pomme","cerise","orange"]
#def ma_fonction():
#    return fruits
#print(ma_fonction())

#Job02
#def ma_fonction():
#    fruits = ["pomme","cerise","orange"]
#    print(fruits[1])
#ma_fonction()

#Job03
#def ma_fonction():
#    fruits = ["pomme","cerise","orange"]
#    fruits.append("melon")
#    print(fruits)
#ma_fonction()

#Job04
#def ma_fonction():
#    fruits = ["pomme","cerise","orange","melon"]
#    fruits.insert(2,"mangue")
#    print(fruits)
#ma_fonction()

#Job05
#l=[1,2,3,4,5]
#print(l[1])
#def ma_fonction ():
#    l[3] = l[2]+l[4]
#    print (l[3])
#ma_fonction()
#print(l)
#print (l[-1])

#Job06
#l=[1,2,3,4,5]
#l[0],l[-1] = l[-1],l[0]
#print(l)

#Job07
#l = [8, 24,48,2,16]
#multiple = len([i for i in l if i % 3 == 0])
#print(multiple)

#Job08
#l = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
#somme = []
#for i in l :
#    if i % 2 == 0: 
#        somme.append(i)
#    else :
#        continue
#print (sum(somme))

#Job09
#L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
#L.sort()
#print("la valeur max est : ", L[-1])
#print("la valeur min est : ", L[0])

#Job10
#L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
#somme = 0
#for i in L:
#  if i >= 25 and i <= 90 :
#    somme = somme + i
#  else : 
#    continue
#print(somme)

#Job11
#L = [7, 11, 42, 39, 2]
#L = [i+1 for i in L]
#print(L)

#Job12
#L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
#for a in range (len(L)) :
#        for b in range(a+1,len(L)):
#                if L[a] > L[b]:
#                        L[a],L[b]=L[b],L[a]
#print(L)
        
#Job13
#l = [10, 20,30, 20, 10, 50, 60, 40, 80, 50, 40]
#l2 = []
#for i in l:
#    if i not in l2:
#        l2.append(i)
#print(l2)

#Job14
#def my_long_word(a : str, b : int):
#    for i in a :
#        mot = len(i)
#        if mot <= b :
#            return a.replace(i,"") 
#print(my_long_word("La peur est le chemin vers le côté obscur",3))

#Job15
#L = [22.4, 4.0, 16.22,9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
#l2 = []
#for a in L :
#        if a not in l2:
#             l2.append(int(a)) 
#def ma_fonction():
#    for c in range (len(l2)) :
#     for d in range(c+1,len(l2)):
#        if l2[c] > l2[d]:
#            l2[c],l2[d]=l2[d],l2[c]
#            return l2
#print(ma_fonction())