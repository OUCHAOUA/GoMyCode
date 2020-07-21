# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 23:02:51 2020

@author: Oussama
"""

#Question 7

#Question: Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24 
#Hints: If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26) In case of input data being supplied to the question, it should be assumed to be a console input. 


#Création d'une Fonction de Calcule avec des Valeur par Default
def calcule (D, C=50,H=30):   
    return int(((2*C*D)/H)**.5)


#Récupere la séquence des nombres avec input
#Utilisation de Map pour convertir "un par un" la sequence str en int et l'enregistrer dans une list
in_Liste = list(map(int,(input("\nEntrer une séquence de nombres 'séparer par une virgule: ").split(','))))
 
#Toujours avec map envoi la séquence in_Liste "un par un"  vers la fonction Calcule
out_Liste =  list(map(calcule, in_Liste))

#Affichage 
print ('Séquence Entrer : \n', in_Liste , '\n Séquence de Sortie : \n', out_Liste )
