import math 
# ex1
# t = 6.892
# d = 19.7
# print(round(t,1))

# ex2
# nom = str(input("nom : "))
# age = int(input("age : "))
# print("vous vous appelez", nom, "et vous avez", age)

# ex3
# x = 3.12
# if x >= 0 :
#     print(math.sqrt(x))
# else:
#     print("err")

# ex4
# motUn =  "azerty"
# motDeux = "qsdfgh"
# print(min(motUn, motDeux))

# ex5
pSeuil = 2.3
vSeuil = 7.41

p = float(input("pression : "))
v = float(input("volume courant : "))

# –si le volume et la pression sont supérieurs aux seuils : arrêt immédiat ;
# –si seule la pression est supérieure à la pression seuil : demander d’augmenter le volume de l’enceinte ;
# –si seul le volume est supérieur au volume seuil : demander de diminuer le volumede l’enceinte ;
# –sinon déclarer que « tout va bien ».
if p > pSeuil and v > vSeuil :
    print("Arret immédiat")
elif p > pSeuil:
    print("augmenter le volume de l’enceinte")
elif v > vSeuil:
    print("diminuer le volumede l’enceinte")
else:
    print('tout va bien ')