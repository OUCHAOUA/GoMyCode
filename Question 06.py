# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 19:33:16 2020

@author: Oussama
"""
#Question 6

#Write a NumPy program to compute the covariance matrix of two given arrays. 
#Original array1: [0 1 2] 
#Original array2: [2 1 0] 
#Covariance matrix of the said arrays: [[ 1. -1.] [-1. 1.]]


#Import
import numpy as np

#Creation des variables.
np_A = np.array([0, 1, 2])

np_B = np.array([2, 1, 0])

np_AB = np.vstack((np_A,np_B))

#Utilisation de la fonction cov()
Resultat = np.cov (np_AB)

#Affichage 
print ('La matrice de covariances du Tableau : \n', np_AB , '\n est : \n', Resultat )



