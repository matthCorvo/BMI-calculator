#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Demander le nom de l'utilisateur
nom = input("Entrez votre nom : ")

# Demander le poids en kilogrammes
poids_kg = float(input("Entrez votre poids en kilogrammes : "))

# Demander la taille en centimètres
taille_cm = float(input("Entrez votre taille en centimètres : "))

# Convertir la taille en mètres (1 mètre = 100 centimètres)
taille_m = taille_cm / 100

# Calcul de l'IMC
IMC = poids_kg / (taille_m ** 2)

# Afficher l'IMC
print("Votre IMC est :", IMC)

# Évaluer la catégorie de poids
if IMC > 0:
    if IMC < 18.5:
        print(nom + ", vous êtes en sous-poids.")
    elif IMC <= 24.9:
        print(nom + ", votre poids est normal.")
    elif IMC < 29.9:
        print(nom + ", vous êtes en surpoids. Vous devriez faire plus d'exercice et arrêter de rester assis devant un écran.")
    elif IMC < 34.9:
        print(nom + ", vous êtes obèse.")
    elif IMC < 39.9:
        print(nom + ", vous êtes sévèrement obèse.")
    else:
        print(nom + ", vous êtes morbidement obèse.")
else:
    print("Entrez des valeurs valides.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




