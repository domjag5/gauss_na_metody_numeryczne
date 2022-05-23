# GLOBALNE
# wczytanie danych
n = int(input())
M = []
D = []
# macierz wejsciowa (ukladu)
for w in range(n):
    kosz = input().split()
    wiersz = []
    for k in range(n):
        pole = [int(kosz[k]), 1]
        wiersz.append(pole)
    M.append(wiersz)
# iksy (wektor wyrazow wolnych)
for w in range(n):
    kosz = int(input())
    wiersz = []
    for k in range(n):
        if k == 0:
            pole = [int(kosz), 1]
        else:
            pole = [0, 1]
        wiersz.append(pole)
    D.append(wiersz)
#FUNKCJE
# funkcje nwd i nww
def nwd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def nww(a, b):
    c = b / nwd(a, b) * a
    return c


# funkcja skracanie ulamka w macierzy
def skroc_ulamek(M, w, k):
    dzielimy_przez = nwd(M[w][k][0], M[w][k][1])
    M[w][k][0] /= dzielimy_przez
    M[w][k][1] /= dzielimy_przez


# funkcja skracanie ulamka nie w macierzy
def skroc_ulamek_niewt(x, y):
    dzielimy_przez = nwd(x, y)
    x /= dzielimy_przez
    y /= dzielimy_przez
    return x, y


# funkcja zamiana wiersza
def zamien_wiersze(M, x, y):
    for k in range(n):
        M[x][k][0], M[y][k][0] = M[y][k][0], M[x][k][0]
        M[x][k][1], M[y][k][1] = M[y][k][1], M[x][k][1]


# funkcja dzielenie wiersza - mnozymy przez odwrotnosc
def podziel_wiersz(M, wiersz, dzielnik_licznik, dzielnik_mianownik):
    for k in range(n):
        M[wiersz][k][0] *= dzielnik_mianownik
        M[wiersz][k][1] *= dzielnik_licznik
        skroc_ulamek(M, wiersz, k)


# funkcja odjecie wiersza pomnozonego przez cos
# mnozenie -mnozymy licznik i mianownik
# odejmowanie
def odejmij_wiersze(M, odjemna, odjemnik, mnoznik_licznik, mnoznik_mianownik):
    for k in range(n):
        odjemnik_licznik = M[odjemnik][k][0] * mnoznik_licznik
        odjemnik_mianownik = M[odjemnik][k][1] * mnoznik_mianownik
        odjemnik_licznik, odjemnik_mianownik = skroc_ulamek_niewt(odjemnik_licznik, odjemnik_mianownik)
        nowy_mianownik = nww(M[odjemna][k][1], odjemnik_mianownik)
        M[odjemna][k][0] *= (nowy_mianownik / M[odjemna][k][1])
        odjemnik_licznik *= (nowy_mianownik / odjemnik_mianownik)
        M[odjemna][k][1] = nowy_mianownik
        odjemnik_mianownik = nowy_mianownik
        M[odjemna][k][0] -= odjemnik_licznik
        skroc_ulamek(M, w, k)


def wypisz_rownanie():
    for i in range(n):
        for k in range(n):
            dwa_po_przecinku = round(M[i][k][0] / M[i][k][1], 2) + 0
            jedno_po_przecinku = round(M[i][k][0] / M[i][k][1], 1) + 0
            if dwa_po_przecinku == jedno_po_przecinku:
                print((M[i][k][0] / M[i][k][1]) + 0, end=" ")
            else:
                print('{0:.2f}'.format(dwa_po_przecinku), end=" ")
        print("\t\t|", (D[i][0][0] / D[i][0][1]))


# PROGRAM
# poczatek
aktualny_pierwszy_wiersz = 0
aktualna_pierwsza_kolumna = 0
aktualna_liczba_wierszy = n
aktualna_liczba_kolumn = n
# xd
a_j0 = 0
#
wypisz_rownanie()
while aktualny_pierwszy_wiersz < n and aktualna_pierwsza_kolumna < n and \
        aktualna_liczba_wierszy > 0 and aktualna_liczba_kolumn > 0:
    # a_w,k - element glowny
    # modyfikowany - el o najwiekszej wartoci bezwzglednej
    # wybor elemntu glownego
    w = aktualny_pierwszy_wiersz
    k = aktualna_pierwsza_kolumna
    a_licznik = M[w][k][0]
    a_mianownik = M[w][k][1]
    
    for k in range(aktualna_pierwsza_kolumna, n):
        for w in range(aktualny_pierwszy_wiersz, n):
            a_licznik = M[w][k][0]
            a_mianownik = M[w][k][1]
            if a_licznik != 0:
                break
        if a_licznik != 0:
            break
    print("element glowny:", a_licznik / a_mianownik)
    if a_licznik == 0:
        break
    else:
        a_i0 = w
        a_j0 = k
        # zamiana pierwszego wiersza z wierszem i0
        zamien_wiersze(M, aktualny_pierwszy_wiersz, a_i0)
        zamien_wiersze(D, aktualny_pierwszy_wiersz, a_i0)
        # dzielenie pierwszego wiersza przez a
        podziel_wiersz(M, aktualny_pierwszy_wiersz, a_licznik, a_mianownik)
        podziel_wiersz(D, aktualny_pierwszy_wiersz, a_licznik, a_mianownik)
        # Dla wszystkich wierszy oprocz pierwszego:
        # od danego wiersza odejmujemy wiersz pierwszy macierzy A
        # pomnożony przez element stojący w danym wierszu w kolumnie j0
        print("mnozniki:", end=" ")
        for w in range(n):
            mnoznik_licznik = M[w][a_j0][0]
            mnoznik_mianownik = M[w][a_j0][1]
            print('{0:.2f}'.format((mnoznik_licznik / mnoznik_mianownik) / (a_licznik / a_mianownik)), end=" ")
            if w != aktualny_pierwszy_wiersz:
                odejmij_wiersze(M, w, aktualny_pierwszy_wiersz, mnoznik_licznik, mnoznik_mianownik)
                odejmij_wiersze(D, w, aktualny_pierwszy_wiersz, mnoznik_licznik, mnoznik_mianownik)
            else:
                pass
        print()
    # zmniejszamy macierz (rozpatrywana czesc macierzy)
    aktualny_pierwszy_wiersz += 1
    aktualna_pierwsza_kolumna = a_j0 + 1
    aktualna_liczba_wierszy -= 1
    aktualna_liczba_kolumn = n - aktualna_pierwsza_kolumna
    #
    print()
    wypisz_rownanie()
# rzad macierzy
i = 0
pom = M[n - 1][n - 1][0]
for i in range(n - 1, -1, -1):
    for k in range(n - 1, -1, -1):
        pom = M[i][k][0]
        if pom != 0:
            break
    if pom != 0:
        break
if i + 1 < n:
    print("macierz nieodwracalna")
else:
    print()
    # wypisanie macierzy w postaci calkowicie zredukowanej
    for i in range(n):
        for k in range(n):
            dwa_po_przecinku = round(D[i][k][0] / D[i][k][1], 2) + 0
            jedno_po_przecinku = round(D[i][k][0] / D[i][k][1], 1) + 0
            if dwa_po_przecinku == jedno_po_przecinku:
                print((D[i][k][0] / D[i][k][1]) + 0, end=" ")
            else:
                print('{0:.2f}'.format(dwa_po_przecinku), end=" ")
        print()