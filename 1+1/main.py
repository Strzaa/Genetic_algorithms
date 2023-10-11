import random
import matplotlib.pyplot as plt

# PARAMETRY
c1 = 0.82
c2 = 1 / c1
fi = 1
k = 5
t = 200  # iteracje
x = [random.uniform(-2, 2), random.uniform(-2, 2)]  # chromosom
ilosc_sukcesow = 0

# Wykres
time = []
tab_wyniki = []
tab_fi = []

# Debug
debug = True

def f_x1_x2(tab):  # funkcja przystosowania
    return 2 - tab[0] ** 2 - tab[1] ** 2


def generate_y(value, fii):
    new = value + fii * random.gauss(0, 1)
    if new < -2: new = -2
    if new > 2: new = 2
    return new


for i in range(t):
    if i % k == 0 and i != 0:
        if debug: print(f"Old fi: {fi}")
        if (ilosc_sukcesow / k) < 0.2:
            fi = c1 * fi
        elif (ilosc_sukcesow / k) > 0.2:
            fi = c2 * fi
        if debug: print(f"New fi: {fi}")
        ilosc_sukcesow = 0

    wynik_x = f_x1_x2(x)
    y = [generate_y(x[0], fi), generate_y(x[1], fi)]
    wynik_y = f_x1_x2(y)

    if wynik_y > wynik_x:
        x = y
        ilosc_sukcesow += 1

    time.append(i)
    tab_wyniki.append(wynik_x)
    tab_fi.append(fi)

    if debug: print(f"Iteracja: {i+1}, Sukces: {ilosc_sukcesow}, X: {x}, Wynik_x: {round(wynik_x, 4)}, Y: {y}, Wynik_y: {round(wynik_y, 4)}")

plt.plot(time, tab_wyniki, label="Wartosc_funkcji")
plt.plot(time, tab_fi, label="Wartosc_mutacji")

plt.xlabel("Iteracja")
plt.ylabel("Wartosc")

plt.legend()

plt.show()
