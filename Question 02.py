# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 16:20:07 2020

@author: Oussama
"""
#Question 2 
#Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320 
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.




#Methode avec numpy

#Import
import numpy as np



# Recuperer un Nombre de l'utilisateur
n = int (input("Entrer un Nombre ??"))


resultat =  (np.prod(range(1,n+1)))

print ("Le Factorial de {0} est {1}.".format(n,resultat))


#Methode sans numpy

#Creation des variables.
resultat = 1


# Recuperer un Nombre de l'utilisateur
n = int (input("Entrer un Nombre ??"))

#Bocle de Multiplication
for i in range(1,n + 1):
   resultat *=  i

#Affichage du resultat
print ("Le Factorial de {0} est {1}.".format(n,resultat))

