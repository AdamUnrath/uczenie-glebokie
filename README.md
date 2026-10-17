# Uczenie głębokie

Repozytorium z zadaniami z przedmiotu **Uczenie głębokie** (2026).


## Zawartość

| Plik | Opis |
|------|------|
| `komiwojazer.py` | Problem komiwojażera rozwiązany metodą brute force (Python) |

## Zadanie: problem komiwojażera

Program szuka najkrótszej trasy, która zaczyna się w Gdańsku, odwiedza każde z pozostałych miast dokładnie raz i wraca do Gdańska.

**Miasta:** Gdańsk, Warszawa, Kraków, Wrocław, Poznań

### Jak to działa

1. Odległości między miastami są zapisane w macierzy `odleglosci` (kolejność wierszy i kolumn odpowiada liście miast).
2. Gdańsk jest punktem startowym, a pozostałe 4 miasta ustawiane są we wszystkich możliwych kolejnościach (`itertools.permutations`), czyli 4! = 24 trasy.
3. Dla każdej trasy program sumuje odległości między kolejnymi miastami.
4. Zapamiętywana jest trasa o najmniejszej łącznej długości.

### Uruchomienie

Wymagany jest Python 3 (nie trzeba instalować żadnych dodatkowych bibliotek).

```bash
python komiwojazer.py
```

### Wynik

```
Najlepsza trasa: Gdańsk -> Warszawa -> Kraków -> Wrocław -> Poznań -> Gdańsk
Długość: 1380 km
Liczba sprawdzonych tras: 24
```

### Uwaga

Metoda brute force sprawdza wszystkie możliwe trasy, więc liczba obliczeń rośnie jak silnia liczby miast. Dla 5 miast działa natychmiast, ale przy większej liczbie miast staje się niepraktyczna.
