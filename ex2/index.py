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

# mliste = [17, 38, 10, 25, 72]
# mliste.sort()
# print(mliste)
# mliste.append(12)
# print(mliste)
# mliste.reverse()
# print(mliste)
# print(mliste.index(17))
# mliste.remove(38)
# print(mliste)
# print(mliste[1:3])
# print(mliste[:2])
# print(mliste[2:])
# print(set(mliste))

# ex 16

# s = "oklm"
# print(s[::-1])

# ex 17

# a = "aza"
# b = a [:: -1]
# if a==b:
#     print("Est un palindrome")
# else:
#     print("No")

# ex 18

# string = str(input("variable : "))
# if(re.search(r"^[^@]+@[^@]+\.[^@]+$",string)):  
#   print("mail ok")

# ex 19
# Initialisez truc comme une liste vide, et machin comme une liste de cinq flottants nuls.

# truc = []
# machin = [0.0,0.0,0.0,0.0,0.0]

# for i in truc:
#     print(i)
# for i in machin:
#     print(i)


# ex 20
# for i in range(0,3):
#     print(i)
# for i in range(4,7):
#     print(i)
# for i in range(2,8+1):
#     if( i%2  == 0 ):
#         print(i)

# chose = [i+1 for i in range(5)]
# print(chose)
# find = [3,6]
# for i in find :
#     exist = False
#     for y in chose:
#         if i == y:
#             exist = True
#     if exist == True:
#         print(i , " exist in chose")
#     else:
#          print(i , " don't exist in chose")

# ex 21
# mfile = open("monsupernombredufutur.txt", mode="w")
# mynumber = int(input("elelment de la ligne"))
# i = 0

# while i < mynumber :
#     nel = str(input("saisir element ;"))
#     mfile.write(nel + "\n")
#     i += 1

# mfile.close()

# ex 22
# fh = open('mail.txt')
# for line in fh:
#   if(re.search(r"^[^@]+@[^@]+\.[^@]+$", str(line))):
#     print(line)
# fh.close()

# ex 23

# def lenMots(str):
#   count = dict()
#   words = str.split()
#   for word in words:
#       if word in count:
#           count[word] += 1
#       else:
#           count[word] = 1
#   return count
# print(lenMots("azerty azrezt azdiopvd azopijckqsop cdsvpokvdpsok"))

# ex 24
# import sys
# r = int(sys.argv[1])
# pi = 3.1415926535897931
# V= 4.0/3.0*pi* r**3
# print('The volume of the sphere is: ',V," pour un ranyon de ",r)

# ex 25
# def somme(a, b, c) :
#     return print((a+b+c))
# tuplee = (1, 2, 1)
# somme(tuplee[0], tuplee[1], tuplee[2])