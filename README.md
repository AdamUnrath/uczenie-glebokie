# Uczenie głębokie

Repozytorium z zadaniami z przedmiotu **Uczenie głębokie** (2026).

## Autor

Adam Unrath

## Zawartość

| Plik | Opis |
|------|------|
| `komiwojazer.ipynb` | Notebook Jupyter: problem komiwojażera (brute force) z wizualizacjami i wnioskami, wyniki są już zapisane w pliku |

## Zadanie: problem komiwojażera

Program szuka najkrótszej trasy, która zaczyna się w Gdańsku, odwiedza każde z pozostałych miast dokładnie raz i wraca do Gdańska.

**Miasta:** Gdańsk, Warszawa, Kraków, Wrocław, Poznań

### Jak to działa

1. Odległości między miastami są zapisane w macierzy `odleglosci` (kolejność wierszy i kolumn odpowiada liście miast).
2. Gdańsk jest punktem startowym, a pozostałe 4 miasta ustawiane są we wszystkich możliwych kolejnościach (`itertools.permutations`), czyli 4! = 24 trasy.
3. Dla każdej trasy program sumuje odległości między kolejnymi miastami.
4. Zapamiętywana jest trasa o najmniejszej łącznej długości.

### Wynik

```
Najlepsza trasa: Gdańsk -> Warszawa -> Kraków -> Wrocław -> Poznań -> Gdańsk
Długość: 1380 km
Liczba sprawdzonych tras: 24
```

### Wizualizacje (w notebooku)

- **Najlepsza trasa na wykresie:** strzałki między miastami z podpisanymi odległościami (do rysunku użyto przybliżonych współrzędnych geograficznych miast, więc wykres jest poglądowy).
- **Porównanie wszystkich 24 tras:** wykres słupkowy posortowany według długości z wyróżnioną najkrótszą trasą. Dwie trasy mają tę samą najmniejszą długość, bo to ta sama pętla przejechana w przeciwnych kierunkach (macierz odległości jest symetryczna).

## Uruchomienie

Wyniki i wykresy są widoczne od razu po otwarciu `komiwojazer.ipynb` na GitHubie. Aby uruchomić notebook samodzielnie:

- **Google Colab:** wejdź na [colab.research.google.com](https://colab.research.google.com), wybierz **File → Upload notebook** (albo **GitHub** i wklej adres repozytorium) i uruchom wszystkie komórki (**Runtime → Run all**).
- **Lokalnie:** zainstaluj biblioteki i uruchom Jupyter.

```bash
pip install jupyter matplotlib
jupyter notebook komiwojazer.ipynb
```

## Uwaga

Metoda brute force sprawdza **(n−1)!** tras, więc liczba obliczeń rośnie bardzo szybko. Dla 5 miast działa natychmiast, ale już dla 15 miast byłoby to ponad 87 miliardów tras, więc przy większej liczbie miast stosuje się metody przybliżone (heurystyki, algorytmy genetyczne, uczenie ze wzmocnieniem).
