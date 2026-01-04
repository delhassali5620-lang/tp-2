# calculatrice.py

# Lecture de deux nombres
try:
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))
except ValueError:
    print("Erreur : veuillez entrer un nombre valide.")
    exit()

# Menu des opérations
print("Choisissez l'opération : + - * /")
op = input("Opération : ")

# Calcul selon l'opérateur
if op == "+":
    resultat = a + b
elif op == "-":
    resultat = a - b
elif op == "*":
    resultat = a * b
elif op == "/":
    if b != 0:
        resultat = a / b
    else:
        print("Erreur : division par zéro")
        exit()
else:
    print("Opérateur invalide")
    exit()

# Affichage du résultat
print(f"{a} {op} {b} = {resultat}")
