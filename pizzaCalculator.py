small = 3.99
medium = 5.00
large = 6.00

#klant krijgt de prijzen te zien.
print("""Prijzen in euro's
small = 3.99
medium = 5
large = 6""")

aantalSmall = float(input("Hoeveel small pizza's wil je? "))
print("Dit kost", aantalSmall * small)

aantalMedium = float(input("Hoeveel medium pizza's wil je? "))
print("Dit kost", aantalMedium * medium)

aantalLarge = float(input("Hoeveel large pizza's wil je?"))
print("Dit kost", aantalLarge * large)

print("Totaalprijs =", aantalSmall * small + aantalMedium * medium + aantalLarge * large)