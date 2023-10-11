import random
import math

# Parametry algorytmu
𝜇 = 4
𝜆 = 4

# Warunek zatrzymania algorytmu
def warunek_zatrzymania(iteration):
    return iteration >= 100

# Funkcja przystosowania (cel optymalizacji)
def funkcja_przystosowania(x):
    return (x[0] - 2) * 2 + (x[1] - 3) * 2

# Inicjalizacja początkowej populacji 𝑷
def inicjalizuj_populacje():
    populacja = []
    for _ in range(𝜇):
        x = [random.uniform(-5, 5), random.uniform(-5, 5)]
        populacja.append(x)
    return populacja

# Ocen populację 𝑷
def ocen_populacje(populacja):
    oceny = []
    for x in populacja:
        ocena = funkcja_przystosowania(x)
        oceny.append(ocena)
    return oceny

# Reprodukcja (losowanie 𝜆osobników z populacji 𝑷)
def reprodukcja(populacja):
    populacja_tymczasowa = []
    for _ in range(𝜆):
        x = random.choice(populacja)
        populacja_tymczasowa.append(x)
    return populacja_tymczasowa

# Krzyżowanie i mutacja
def krzyzowanie_mutacja(populacja_tymczasowa):
    nowa_populacja = []
    for _ in range(𝜆):
        rodzice = random.sample(populacja_tymczasowa, 2)
        x = []
        for i in range(len(rodzice[0])):
            if i + 2 < len(rodzice[0]):
                a = random.uniform(0, 1)
                gen = a * rodzice[0][i] + (1 - a) * rodzice[1][i]
                sigma_gen = a * rodzice[0][i + 2] + (1 - a) * rodzice[1][i + 2]
                x.append(gen + sigma_gen * random.gauss(0, 1))
            else:
                x.append(random.uniform(-5, 5))  # Dodaj losowy element dla krzyżowania poza zakresem indeksów
        nowa_populacja.append(x)
    return nowa_populacja


# Wybór 𝜇najlepszych osobników z populacji 𝑷∪𝑶
def wybor_najlepszych(populacja, nowa_populacja, oceny_populacji, oceny_nowej_populacji):
    populacja.extend(nowa_populacja)
    oceny_populacji.extend(oceny_nowej_populacji)
    populacja_i_oceny = list(zip(populacja, oceny_populacji))
    populacja_i_oceny.sort(key=lambda x: x[1])
    najlepsze_populacja_i_oceny = populacja_i_oceny[:𝜇]
    najlepsza_populacja = [x for x, _ in najlepsze_populacja_i_oceny]
    oceny_najlepszej_populacji = [ocena for _, ocena in najlepsze_populacja_i_oceny]
    return najlepsza_populacja, oceny_najlepszej_populacji

# Główna funkcja algorytmu
def strategia_ewolucyjna():
    populacja = inicjalizuj_populacje()
    oceny_populacji = ocen_populacje(populacja)
    iteracja = 0

    while not warunek_zatrzymania(iteracja):
        populacja_tymczasowa = reprodukcja(populacja)
        nowa_populacja = krzyzowanie_mutacja(populacja_tymczasowa)
        oceny_nowej_populacji = ocen_populacje(nowa_populacja)
        populacja, oceny_populacji = wybor_najlepszych(populacja, nowa_populacja, oceny_populacji, oceny_nowej_populacji)
        najlepsza_ocena = min(oceny_populacji)

        print("Iteracja:", iteracja)
        print("Najlepsza ocena:", najlepsza_ocena)

        iteracja += 1

    najlepszy_osobnik = populacja[oceny_populacji.index(min(oceny_populacji))]

    print("Najlepszy osobnik:", najlepszy_osobnik)
    print("Najlepsza ocena:", min(oceny_populacji))

strategia_ewolucyjna()