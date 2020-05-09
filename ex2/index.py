import math
import re
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

# # ex5
# pSeuil = 2.3
# vSeuil = 7.41

# p = float(input("pression : "))
# v = float(input("volume courant : "))

# # –si le volume et la pression sont supérieurs aux seuils : arrêt immédiat ;
# # –si seule la pression est supérieure à la pression seuil : demander d’augmenter le volume de l’enceinte ;
# # –si seul le volume est supérieur au volume seuil : demander de diminuer le volumede l’enceinte ;
# # –sinon déclarer que « tout va bien ».
# if p > pSeuil and v > vSeuil :
#     print("Arret immédiat")
# elif p > pSeuil:
#     print("augmenter le volume de l’enceinte")
# elif v > vSeuil:
#     print("diminuer le volumede l’enceinte")
# else:
#     print('tout va bien ')

# ex6

# mail = str(input("votre mail : "))
# if(re.search(r"\b@\b.*\b.com\b", mail)):
#     print("Valid mail")
# else:
#     print("Invalid mail")

# ex7
# for x in range(0, 10):
#     print('o')

# ex8
# for x in ("alouette"):
#     print(x)

# ex9

# a = 0 
# b = 10

# while a < b:
#   print(a)
#   a += 1

# ex 10

# b = 10

# while b > 0:
#     if b%2 != 0:
#         print("impaire")
#     else:
#         print("pair")
#     b = b-1

# ex 11

# u=True
# while u:
#     n = int(input("Entrez un nombre:"))
#     if 1 <= n <= 10:
#         print(n)
#         u = False

# ex 12
# my_list = ["azerty","azeqsdqs", "zeaesq"]
# for i in my_list:
#     print(i)

# ex 13

# for i in range(1,15):
#     if i%3==0:
#         print(i)

#ex 14

# n = int(input("n : "))
# i = 0
# while i < n:
#     i+=1
#     if i%2==0:
#       print(i)

# for r in range(1,n+1):
#     if r%2==0:
#         print(r)

#ex 15
