import random
import matplotlib.pyplot as plt
import math

# PARAMETRY
c1 = 0.82
c2 = 1 / c1
fi = 5
k = 5

x = [random.randint(0, 31)]  # chromosom
ilosc_sukcesow = 0

iteracja = 0
podRzad = 0
ilePodRzad = 30
wyniki = [0, 0]

# Wykres
time = []
tab_wyniki = []
tab_fi = []

# Debug
debug = True


def f_x1(tab):  # funkcja przystosowania
    return (tab[0] / 15) * (math.sin((math.pi * tab[0]) / 8) + 1)


def generate_y(value, fii):
    new = value + fii * random.gauss(0, 1)
    if new < 0: new = 0
    if new > 31: new = 31
    new = round(new, 0)
    return new


def wykres():
    plt.plot(time, tab_wyniki, label="Wartosc_funkcji")
    plt.plot(time, tab_fi, label="Wartosc_mutacji")

    plt.xlabel("Iteracja")
    plt.ylabel("Wartosc")

    plt.legend()

    plt.show()


while True:
    if iteracja % k == 0 and iteracja != 0:
        if (ilosc_sukcesow / k) < 0.2:
            fi = c1 * fi
        elif (ilosc_sukcesow / k) > 0.2:
            fi = c2 * fi
        ilosc_sukcesow = 0

    wynik_x = f_x1(x)
    y = [generate_y(x[0], fi)]
    wynik_y = f_x1(y)

    if wynik_y > wynik_x:
        x = y
        ilosc_sukcesow += 1
        wyniki.append(wynik_y)
    else:
        wyniki.append(wynik_x)

    if (iteracja + 1) % 2 == 0:
        if wyniki[0] == wyniki[1]:
            podRzad += 1
            wyniki.clear()
        else:
            podRzad = 0
            wyniki.clear()

    time.append(iteracja)
    tab_wyniki.append(wynik_x)
    tab_fi.append(fi)

    if debug: print(
        f"Iteracja: {iteracja + 1}, Sukces: {ilosc_sukcesow}, X: {x}, Wynik_x: {round(wynik_x, 4)}, Y: {y}, Wynik_y: {round(wynik_y, 4)}, PodRzad: {podRzad}")
    iteracja += 1
    
    if podRzad >= ilePodRzad:
        wykres()
        break