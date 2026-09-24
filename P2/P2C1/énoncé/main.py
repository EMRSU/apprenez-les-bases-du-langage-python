# Ecrivez votre code ici !
#Question 1:
nombre1 = input("Entrer un nombre ")
nombre2 = input("Entrer un second nombre ")

#Question 2, 3 & 4:
if not nombre1.isnumeric() and not nombre2.isnumeric():
    print("les deux nombre doivent être des entier")
    raise SystemExit("Fin du programme")
nombre1 = int(nombre1)
nombre2 = int(nombre2)

#Question 5:
operation = input("Entrez l'opération souhaitée ('+', '-', '*' ou '/') ")

#Question 6:
if operation not in ["+", "-", "*", "/"]:
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    raise SystemExit("Fin du programme")

#Question 7, 8 & 9:
if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    # Vérifie si la variable `nombre2` n'est pas nulle pour la division
    if nombre2 == 0:
        print("Erreur: impossible de diviser par zéro.")
        raise SystemExit("Fin du programme") 

    resultat = round(nombre1 / nombre2, 2)

#Question 10:
print(f"Le résultat de l'opération est: {round(resultat, 2)}")