# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 18:17:28 2020

@author: Oussama
"""
#Question 5

#Write a NumPy program to convert a NumPy array into a Python list structure.
#Expected Output: 
#Original array elements: [[0 1] [2 3] [4 5]] 
#Array to list: [[0, 1], [2, 3], [4, 5]] 

#Import
import numpy as np

#Creation des variables.
# Creation du tableau Np
np_Tableau = np.array([[0, 1], [2, 3], [4, 5]])
Liste = []

#Methode long

#Boucle sur np_Tableau et création de la liste
for i,j in (np_Tableau):
    Liste.append([i,j])

#Affichage 
print ('Liste : Méthode Boucle', Liste)


#Méthode Court

# Utilisation map et List
Liste = list(map(list,(np_Tableau)))

#Affichage 
print ('Liste : Méthode Map   ', Liste)
