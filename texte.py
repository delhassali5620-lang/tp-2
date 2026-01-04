# texte.py

texte = input("Entrez un mot ou une phrase : ")

# Longueur du texte
print("Longueur :", len(texte))

# Majuscules et minuscules
print("En majuscules :", texte.upper())
print("En minuscules :", texte.lower())

# Texte inversé
inverse = texte[::-1]
print("Inverse :", inverse)

# Vérification palindrome
if texte.lower().replace(" ", "") == inverse.lower().replace(" ", ""):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")

# Remarque sur immutabilité
print("L'objet texte initial reste :", texte)
