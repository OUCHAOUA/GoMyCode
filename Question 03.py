# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:16:36 2020

@author: Oussama
"""

#Question 3 
#Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} 


#Creation des variables.
dict_Carre = dict()

#Recuperer d'un Nombre de l'utilisateur
n = int (input("Entrer le Nombre de Clé??"))

#Boucle de Creation des Keys et Values
for i in range(1,n + 1):
   #ajouter le carée par indexation 
   dict_Carre [i] =  i**2
   

#Affichage du resultat
print ("Le Dictionnaire resultat : ", dict_Carre)
