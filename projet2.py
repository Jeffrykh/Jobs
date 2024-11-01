#Job01
for i in range (21):
    print (i)

#Job02
for i in range (21):
    if i % 2 ==0:
        print (i)

#Job03
for i in range (21):
    if i % 2 ==0:
        print (i**2)

#Job04
n = int(input("Entrer un nombre supérieure à 0 : "))
for i in range(n+1):
    print("table de ", i)
    for a in range(11):
     print(i*a)

#Job5
n=1
while n < 13 :
    n = n +1  
    print(n)

#Job6
n = int(input("Entrer un nombre supérieure à 0 : "))
i=0
while i <= n:
    print (i,"X 7 = ",i*7)
    i=i+1
    
#Job07
for i in range (1,13):
    print ("Tour",i," : ",i*3-2)

#Job08
r=0
for i in range (1,13):
    r= r + 2 
    print ("Tour",i," : ",r)

#Job09
for i in range (1,30):
    if i % 2 ==0:
        print ("Nombre pair : ",i)
    else : 
        print ("Nombre impair",i)
