small = 3.99
medium = 5
large = 6

#klant krijgt de prijzen te zien.
print("""Prijzen in euro's
small = 3.99
medium = 5
large = 6""")
grootte = input("Welke pizza wil je?(Antwoord met s, m, of l)").upper()

if grootte == "S":
    prijs = small

if grootte == "M":
    prijs = medium

if grootte == "L":
    prijs = large

print(prijs)
#Aantal
aantal = int(input("Hoeveel pizzas wil je?(Antwoord met cijfer)"))
#Prijs
print(prijs * aantal)