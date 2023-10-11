import random
import math
import matplotlib.pyplot as plt

𝜇 = 100
𝜆 = 400
𝑛 = 10
𝑟 = 5.12
𝑎 = 10

time = []
best_fitness = []
average_fitness = []
mutation_ranges = []

def warunek_zatrzymania(iteration):
    return iteration >= 100

def funkcja_przystosowania(x):
    return 𝑎 * 𝑛 + sum([(x[i] ** 2 - 𝑎) * math.cos(2 * math.pi * x[i]) for i in range(𝑛)])

def inicjalizuj_populacje():
    populacja = []
    for _ in range(𝜇):
        x = [random.uniform(-𝑟, 𝑟) for _ in range(𝑛)]
        populacja.append(x)
    return populacja

def ocen_populacje(populacja):
    oceny = []
    for x in populacja:
        ocena = funkcja_przystosowania(x)
        oceny.append(ocena)
    return oceny

def reprodukcja(populacja):
    populacja_tymczasowa = []
    for _ in range(𝜆):
        x = random.choice(populacja)
        populacja_tymczasowa.append(x)
    return populacja_tymczasowa

def krzyzowanie_mutacja(populacja_tymczasowa, mutation_range):
    nowa_populacja = []
    for _ in range(𝜆):
        rodzice = random.sample(populacja_tymczasowa, 2)
        x = []
        for i in range(𝑛):
            a = random.uniform(0, 1)
            gen = a * rodzice[0][i] + (1 - a) * rodzice[1][i]
            mutated_gen = gen + random.uniform(-mutation_range, mutation_range)

            if mutated_gen < -𝑟:
                mutated_gen = -𝑟
            elif mutated_gen > 𝑟:
                mutated_gen = 𝑟

            x.append(mutated_gen)
        nowa_populacja.append(x)
    return nowa_populacja

def wybor_najlepszych(populacja, nowa_populacja, oceny_populacji, oceny_nowej_populacji):
    populacja_i_oceny = list(zip(nowa_populacja, oceny_nowej_populacji))
    populacja_i_oceny.sort(key=lambda x: x[1])
    najlepsze_populacja_i_oceny = populacja_i_oceny[:𝜇]
    najlepsza_populacja = [x for x, _ in najlepsze_populacja_i_oceny]
    oceny_najlepszej_populacji = [ocena for _, ocena in najlepsze_populacja_i_oceny]
    return najlepsza_populacja, oceny_najlepszej_populacji


def strategia_ewolucyjna():
    populacja = inicjalizuj_populacje()
    oceny_populacji = ocen_populacje(populacja)
    iteracja = 0
    mutation_range = 1.0

    while not warunek_zatrzymania(iteracja):
        populacja_tymczasowa = reprodukcja(populacja)
        nowa_populacja = krzyzowanie_mutacja(populacja_tymczasowa, mutation_range)
        oceny_nowej_populacji = ocen_populacje(nowa_populacja)
        populacja, oceny_populacji = wybor_najlepszych(populacja, nowa_populacja, oceny_populacji, oceny_nowej_populacji)
        najlepsza_ocena = min(oceny_populacji)
        srednia_ocena = sum(oceny_populacji) / len(oceny_populacji)

        print("Iteracja:", iteracja)
        print("Najlepsza ocena:", najlepsza_ocena)
        print("Srednia ocena:", srednia_ocena)
        print("Zasieg mutacji:", mutation_range)

        # Aktualizacja zasięgu mutacji
        if iteracja > 0:
            previous_best = best_fitness[-1]
            if najlepsza_ocena < previous_best:
                mutation_range *= 0.9
            else:
                mutation_range *= 1.1

        iteracja += 1

        time.append(iteracja)
        best_fitness.append(najlepsza_ocena)
        average_fitness.append(srednia_ocena)
        mutation_ranges.append(mutation_range)

    najlepszy_osobnik = populacja[oceny_populacji.index(min(oceny_populacji))]
    najlepsza_ocena = min(oceny_populacji)

    print("Najlepszy osobnik:", najlepszy_osobnik)
    print("Najlepsza ocena:", najlepsza_ocena)

strategia_ewolucyjna()

plt.plot(time, best_fitness, label="Najlepsza wartość funkcji")
plt.plot(time, average_fitness, label="Średnia wartość funkcji")
plt.plot(time, mutation_ranges, label="Zasięg mutacji")
plt.xlabel("Liczba generacji")
plt.ylabel("Wartość")
plt.ylabel("Zasięg mutacji")
plt.legend()
plt.show()