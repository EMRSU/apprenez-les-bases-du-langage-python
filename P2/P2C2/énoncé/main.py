# Ecrivez votre code ici !
#1, 2
nombres = input("Entrer des nombres séparer par des virgules ")

# 3
liste = nombres.split(",")

# 4
liste_entiers = []
for nombre in liste:
    nombre_entier = int(nombre)
    liste_entiers.append(nombre_entier)

# 5
somme = 0
for nombre in liste_entiers:
    somme += nombre
print("Somme des nombres:", somme)

# 6
moyenne = somme / len(liste_entiers)

# 7
nombre_au_dessus_moyenne = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        nombre_au_dessus_moyenne += 1
print("Nombre de nombres supérieurs à la moyenne:", nombre_au_dessus_moyenne)
