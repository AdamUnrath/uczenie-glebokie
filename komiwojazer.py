from itertools import permutations

miasta = ["Gdańsk", "Warszawa", "Kraków", "Wrocław", "Poznań"]

# Kolejność wierszy i kolumn odpowiada liście miast.
odleglosci = [
    [  0, 340, 600, 480, 300],  # Gdańsk
    [340,   0, 290, 350, 310],  # Warszawa
    [600, 290,   0, 270, 450],  # Kraków
    [480, 350, 270,   0, 180],  # Wrocław
    [300, 310, 450, 180,   0],  # Poznań
]

start = 0  # Indeks Gdańska na liście miast
pozostale = [1, 2, 3, 4]
najkrotsza_dlugosc = float("inf")  # Nieskończoność
najlepsza_trasa = None
liczba_tras = 0

# Sprawdzamy wszystkie kolejności pozostałych miast.
for kolejnosc in permutations(pozostale):
    trasa = [start] + list(kolejnosc) + [start]
    dlugosc = 0

    # Sumujemy odległości między kolejnymi miastami.
    for i in range(len(trasa) - 1):
        skad = trasa[i]
        dokad = trasa[i + 1]
        dlugosc += odleglosci[skad][dokad]

    # Zapamiętujemy lepsze rozwiązanie.
    if dlugosc < najkrotsza_dlugosc:
        najkrotsza_dlugosc = dlugosc
        najlepsza_trasa = trasa

    liczba_tras += 1

nazwy_miast = [miasta[i] for i in najlepsza_trasa]
print("Najlepsza trasa:", " -> ".join(nazwy_miast))
print("Długość:", najkrotsza_dlugosc, "km")
print("Liczba sprawdzonych tras:", liczba_tras)
