# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:24:58 2020

@author: Oussama
"""
#Question 4 

#Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive). 
#missing_char('kitten', 1) → 'ktten' 
#missing_char('kitten', 0) → 'itten' 
#missing_char('kitten', 4) → 'kittn' 

#Creation de la Fonction  missing_char
def missing_char(chaine, n):
        #verification de la condition n est dans la palge de len(chaine) 
    if -1 < n < len(chaine)   :
              return chaine.replace(chaine[n],'')
    else:
              return "Le paramètre ‘n’ est  hors plage de la chaine de caractère"


#Affichage 
print (missing_char('kitten', 1))

print (missing_char('kitten', 0))

print (missing_char('kitten', 4))

#test hors plage de l'index
print (missing_char('kitten', 6))

