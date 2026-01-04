# variables.py

# Déclaration des variables
entier = 42             # int
flottant = 3.14         # float
texte = "Python"        # str
vrai_ou_faux = True     # bool

# Affichage du type de chaque variable
print(entier, "→", type(entier))
print(flottant, "→", type(flottant))
print(texte, "→", type(texte))
print(vrai_ou_faux, "→", type(vrai_ou_faux))

# Vérification avec isinstance
print("entier est int ?", isinstance(entier, int))
print("flottant est float ?", isinstance(flottant, float))
print("texte est str ?", isinstance(texte, str))
print("vrai_ou_faux est bool ?", isinstance(vrai_ou_faux, bool))
