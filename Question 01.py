# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 16:20:07 2020

@author: Oussama
"""
#Question 1 
#Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a sequence on a single line.
#Hints: Consider use range(#begin, #end) method 

#Methode avec numpy

#Import
import numpy as np


#Utilisation du masque boolean
np_range = np.array(range(2000,3200+1))
np_range = np_range [(np_range // 7 ==  np_range / 7 )  &  (np_range // 5 != np_range /5 )]


#Affichage du Résultat
print ('Résultat Format Numpy \n' , np_range)


#Methode sans numpy

#Creation des variables.
#Creation de la séquence Liste.
Liste= []

# LOOP
for i in range(2000,3200 + 1):
   #verification  que 7 devise 'i' et que 5 ne le divise pas
    if (i // 7) == ( i / 7 )  and  (i // 5) != (i /5 ):
        #ajoutez a la séquence
        Liste.append(i)

#Affichage du resultat
print ('Résultat Format Liste \n ', Liste)