"""
Dette er en Python-fil, der demonstrerer forskellige syntaktiske elementer og koncepter i Python.
"""

# Import af indbyggede moduler
import math  # Importerer math-modul til matematiske operationer
import random  # Importerer random-modul til tilfældige tal

# Definering af en funktion med parametre
def kvadratrod(n):
    """Denne funktion tager et tal som input og returnerer kvadratroden."""
    resultat = math.sqrt(n)  # Beregner kvadratroden ved hjælp af math.sqrt
    return resultat

# Definering af en klasse
class Person:
    # Konstruktør metode
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

    # Metode i klassen
    def hilsen(self):
        print(f"Hej, jeg hedder {self.navn} og er {self.alder} år gammel.")

# Brug af en betinget udsagn (if-else)
a = 10
if a > 5:
    print("a er større end 5")  # Udskriver en besked, hvis betingelsen er sand
else:
    print("a er ikke større end 5")  # Udskriver en besked, hvis betingelsen er falsk

# Brug af en løkke (for-loop)
for i in range(5):
    print(f"Dette er iteration nummer {i}")  # Udskriver aktuel iteration

# Listeudtryk
kvadrater = [x**2 for x in range(1, 6)]  # Opretter en liste med kvadraterne af tal fra 1 til 5

# Generatorfunktion
def tal_generator(n):
    for i in range(n):
        yield i  # Yielder tal fra 0 til n-1

# Brug af en generator
for nummer in tal_generator(3):
    print(f"Genereret tal: {nummer}")  # Udskriver tal genereret af generatorfunktionen

# Liste
min_liste = [1, 2, 3, 4, 5]  # Opretter en liste med tal

# Dictionary
min_dict = {"navn": "Peter", "alder": 30}  # Opretter en dictionary med navn og alder

# Kald af funktionen
resultat = kvadratrod(25)  # Beregner kvadratroden af 25 ved at kalde funktionen
print(f"Kvadratroden af 25 er {resultat}")  # Udskriver resultatet

# Oprettelse af et objekt fra en klasse
person1 = Person("Alice", 28)  # Opretter et Person-objekt med navn og alder
person2 = Person("Bob", 35)

# Kald af en metode på objektet
person1.hilsen()  # Kalder hilsen-metoden på person1-objektet
person2.hilsen()

# Generering af et tilfældigt tal
tilfældigt_tal = random.randint(1, 100)  # Genererer et tilfældigt heltal mellem 1 og 100
print(f"Et tilfældigt tal mellem 1 og 100: {tilfældigt_tal}")  # Udskriver det tilfældige tal

