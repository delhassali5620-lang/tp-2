# temperature.py

# Conversion Celsius → Fahrenheit/Kelvin
try:
    c = float(input("Température en Celsius : "))
    f = c * 9/5 + 32
    k = c + 273.15
    print(f"{c}°C = {f}°F = {k}K")
except ValueError:
    print("Erreur : entrez un nombre valide.")

# Conversion Fahrenheit → Celsius/Kelvin
try:
    f_input = float(input("Température en Fahrenheit : "))
    c2 = (f_input - 32) * 5/9
    k2 = c2 + 273.15
    print(f"{f_input}°F = {c2:.2f}°C = {k2:.2f}K")
except ValueError:
    print("Erreur : entrez un nombre valide.")

# Bonus : menu pour choisir le sens de conversion
