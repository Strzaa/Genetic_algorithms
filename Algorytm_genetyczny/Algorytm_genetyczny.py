import random
import math

####PARAETRY############################
p_k = 0.7 #prawd. krzyzowanie
p_m = 0.001 #prawd. mutacji
iteracje = 100 #ilosc iteracji
populacja = 6 #wielkosc populacji

###LOSOWANIE_POCZATKOWEJ_POPULACJI######
x = []
for t in range(populacja):
    x.append(random.randint(1,31))

x = [24,26,30,19,29,10]

###FUNKCJA_PRZYSTOSOWANIA###############
def func(x: int) ->int: #funkcja
    return x/15 * (math.sin(math.pi * x / 8) + 1)

###CIAG_DZIALANIA#######################
f_max = 0 #obecny max func()

f_x = list(map(lambda k: func(k), x)) #lista f(x)
f_max = max(f_x)

sum_f = sum(f_x) 

p_x = list(map(lambda k: k/sum_f,f_x)) #lista p(x)
if round(sum(p_x), 5) != 1: print("sum p(x) is not 1") 

n_x = list(map(lambda k: populacja*k, p_x)) #lista dominacji

# napisaæ geerator liczb po prawdopodobienstwie

x_new = [] #grupa rodzicow
for i in range(populacja):
    x_new.append(random.choices(x, p_x)[0]) # losowanie grupy rodziców

#teraz dobranie w pary i krzyzowanie
#kolejne 2 ciagi bitow w liscie sa parami 
x_new_bin = list(map(lambda k: bin(k)[2:].zfill(5), x_new)) #zmiana liczb z int na binary

for i in range(populacja/2):
    #krzyzowanie
    pass
