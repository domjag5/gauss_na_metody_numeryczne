def odwroc_macierz_trojkatna(A, n):
    if czy_na_przekatnej_sa_zera(A, n):
        print("macierz nieodwracalana")
        return -1
    elif czy_dol_to_zera(A, n) and czy_gora_to_zera(A, n):
        if czy_na_przekatnej_sa_tylko_jedynki(A, n) == False:
            odwroc_elementy_na_przekatnej(A, n)
    elif czy_gora_to_zera(A, n):
        if czy_na_przekatnej_sa_tylko_jedynki(A, n):
            odwroc_dolnotrojkatna_z_jedynkami(A, n)
        else:
            odwroc_dolnotrojkatna_bez_jedynek(A, n)
    elif czy_dol_to_zera(A, n):
        A = znajdz_transpozycje(A, n, n)
        if czy_na_przekatnej_sa_tylko_jedynki(A, n):
            odwroc_dolnotrojkatna_z_jedynkami(A, n)
        else:
            odwroc_dolnotrojkatna_bez_jedynek(A, n)
        A = znajdz_transpozycje(A, n, n)
    return A


def sumuj_macierze(X, X_liczba_wierszy, X_liczba_kolumn, Y, Y_liczba_wierszy, Y_liczba_kolumn):
    if X_liczba_wierszy != Y_liczba_wierszy or X_liczba_kolumn != Y_liczba_kolumn:
        print("operacja niewykonalna")
    else:
        A = []
        for w in range(X_liczba_wierszy):
            wiersz = []
            for k in range(X_liczba_kolumn):
                wiersz.append(X[w][k] + Y[w][k])
            A.append(wiersz)
        return A


def przemnoz_macierze(X, X_liczba_wierszy, X_liczba_kolumn, Y, Y_liczba_wierszy, Y_liczba_kolumn):
    if X_liczba_kolumn != Y_liczba_wierszy:
        print("operacja niewykonalna")
    else:
        A = []
        for w in range(X_liczba_wierszy):
            wiersz = []
            for k in range(Y_liczba_kolumn):
                pom = 0
                for i in range(X_liczba_kolumn):
                    pom += X[w][i] * Y[i][k]
                wiersz.append(pom)
            A.append(wiersz)
        return A


def przemnoz_macierz_przez_skalar(X, X_liczba_wierszy, X_liczba_kolumn, skalar):
    for w in range(X_liczba_wierszy):
        for k in range(X_liczba_kolumn):
            X[w][k] *= skalar


def znajdz_transpozycje(X, X_liczba_wierszy, X_liczba_kolumn):
    A = []
    for k in range(X_liczba_kolumn):
        wiersz = []
        for w in range(X_liczba_wierszy):
            wiersz.append(X[w][k])
        A.append(wiersz)
    return A


def przepisz_macierz(Z, DO, n):
    for w in range(n):
        for k in range(n):
            DO[w][k] = Z[w][k]


def czy_gora_to_zera(A, n):
    czy = True
    for w in range(n):
        for k in range(w + 1, n):
            if A[w][k] != 0:
                czy = False
                break
    return czy


def czy_dol_to_zera(A, n):
    czy = True
    for w in range(n):
        for k in range(0, w - 1):
            if A[w][k] != 0:
                czy = False
                break
    return czy


def czy_na_przekatnej_sa_tylko_jedynki(A, n):
    czy = True
    for w in range(n):
        if A[w][w] != 1:
            czy = False
            break
    return czy


def czy_na_przekatnej_sa_zera(A, n):
    czy = False
    for w in range(n):
        if A[w][w] == 0:
            czy = True
            break
    return czy


def odwroc_elementy_na_przekatnej(A, n):
    for w in range(n):
        A[w][w] = 1 / A[w][w]


def stworz_macierz_skladowa(X, n, kolumna, A):
    for w in range(n):
        kosz = []
        for k in range(n):
            if k == kolumna and w > k:
                kosz.append(-A[w][k])
            elif w == k:
                kosz.append(float(1))
            else:
                kosz.append(float(0))
        X.append(kosz)


def odwroc_dolnotrojkatna_z_jedynkami(A, n):
    X = []
    stworz_macierz_skladowa(X, n, n - 2, A)
    for i in range(n - 3, -1, -1):
        Y = []
        stworz_macierz_skladowa(Y, n, i, A)
        X = przemnoz_macierze(X, n, n, Y, n, n)
    przepisz_macierz(X, A, n)


def odwroc_dolnotrojkatna_bez_jedynek(A, n):
    D = []
    for w in range(n):
        kosz = []
        for k in range(n):
            kosz.append(float(0))
        D.append(kosz)
        D[w][w] = A[w][w]
    odwroc_elementy_na_przekatnej(D, n)
    L = przemnoz_macierze(D, n, n, A, n, n)
    odwroc_dolnotrojkatna_z_jedynkami(L, n)
    L = przemnoz_macierze(L, n, n, D, n, n)
    przepisz_macierz(L, A, n)


def zamien_wiersze(M, x, y):
    for k in range(n):
        M[x][k], M[y][k] = M[y][k], M[x][k]


# funkcja dzielenie wiersza - mnozymy przez odwrotnosc
def podziel_wiersz(M, wiersz, dzielnik):
    for k in range(n):
        M[wiersz][k] /= dzielnik


# funkcja odjecie wiersza pomnozonego przez cos
# mnozenie -mnozymy licznik i mianownik
# odejmowanie
def odejmij_wiersze(M, odjemna, odjemnik, mnoznik):
    for k in range(n):
        M[odjemna][k] -= M[odjemnik][k] * mnoznik


def wypisz_rownanie():
    for i in range(n):
        for k in range(n):
            print('{0:5.2f}'.format(M[i][k] + 0), end=" ")
        print("\t|", '{0:5.2f}'.format(D[i][0] + 0))


def wypisz_macierz(A, n):
    for i in range(n):
        for k in range(n):
            if A[i][k] + 0 == 0:
                print('{0:5}'.format(0), end=" ")
            elif A[i][k] + 0 == 1:
                print('{0:5}'.format(1), end=" ")
            else:
                print('{0:5.2f}'.format(A[i][k] + 0), end=" ")
        print()


# GLOBALNE
# wczytanie danych
print("n: ")
print("macierz:")
# print("iksy: ")
n = int(input())
M = []
D = []
L = []
# macierz wejsciowa (ukladu)
for w in range(n):
    M.append([float(x) for x in input().split()])
# macierz L
for w in range(n):
    L.append([0.0 for _ in range(n)])
    L[w][w] = 1.0
# iksy (wektor wyrazow wolnych)
# kosz = input().split()
kosz = [float(x) for x in range(n)]
for w in range(n):
    D.append([0 for x in range(n)])
    D[w][0] = float(kosz[w])
# wypisz_rownanie()
# PROGRAM
# poczatek
aktualny_pierwszy_wiersz = 0
aktualna_pierwsza_kolumna = 0
aktualna_liczba_wierszy = n
aktualna_liczba_kolumn = n
# xd
a_j0 = 0
#
while aktualny_pierwszy_wiersz < n and aktualna_pierwsza_kolumna < n and \
        aktualna_liczba_wierszy > 0 and aktualna_liczba_kolumn > 0:
    # a_w,k - element glowny
    # bez modyfikacji - element niezerowy o najmniejszym indeksie wiersza
    # wybor elemntu glownego
    w = aktualny_pierwszy_wiersz
    k = aktualna_pierwsza_kolumna
    a = M[w][k]
    # znalezienie kolumny gdzie jest jakis niezerowy element
    for k in range(aktualna_pierwsza_kolumna, n):
        for w in range(aktualny_pierwszy_wiersz, n):
            a = M[w][k]
            if a != 0:
                break
        if a != 0:
            break
    if a == 0:
        break
    else:
        a_i0 = w
        a_j0 = k
        # zamiana pierwszego wiersza z wierszem elementu glownego
        # wypisz_rownanie()
        # if aktualny_pierwszy_wiersz != w:
        #     print("zamiana {0} <-> {1}".format(aktualny_pierwszy_wiersz, w))
        zamien_wiersze(M, aktualny_pierwszy_wiersz, a_i0)
        zamien_wiersze(D, aktualny_pierwszy_wiersz, a_i0)
        # if aktualny_pierwszy_wiersz != w:
        #     wypisz_rownanie()
        # dzielenie pierwszego wiersza przez a <- NIE!!! TERAZ zostawiamy
        # print("element glowny ({0:.2f})".format(a))
        # podziel_wiersz(M, aktualny_pierwszy_wiersz, a)
        # podziel_wiersz(D, aktualny_pierwszy_wiersz, a)
        # wypisz_rownanie()
        # Dla wszystkich wierszy oprocz pierwszego: <- NIE!!! - teraz tylko dla wierszy ponizej
        # od danego wiersza odejmujemy wiersz pierwszy macierzy A
        # pomnożony przez element stojący w danym wierszu w kolumnie elementu glownego
        # (czyli zerujemy kolejna kolumne)
        for w in range(aktualny_pierwszy_wiersz + 1, n):
            # mnozniki dajemy do macierzy L
            mnoznik = M[w][a_j0] / a
            L[w][aktualna_pierwsza_kolumna] = mnoznik
            # print('{0:5.2f}'.format(M[w][a_j0]), end=" ")
            if w != aktualny_pierwszy_wiersz:
                # print("odejmowanie od wiersza {0} wiersza {1} z mnoznikiem {2:.2f}".format(w,aktualny_pierwszy_wiersz,mnoznik))
                odejmij_wiersze(M, w, aktualny_pierwszy_wiersz, mnoznik)
                odejmij_wiersze(D, w, aktualny_pierwszy_wiersz, mnoznik)
                # wypisz_rownanie()
            else:
                pass
        # print()
    # zmniejszamy macierz (rozpatrywana czesc macierzy)
    aktualny_pierwszy_wiersz += 1
    aktualna_pierwsza_kolumna = a_j0 + 1
    aktualna_liczba_wierszy -= 1
    aktualna_liczba_kolumn = n - aktualna_pierwsza_kolumna
# rzad macierzy
i = 0
pom = M[n - 1][n - 1]
for i in range(n - 1, -1, -1):
    for k in range(n - 1, -1, -1):
        pom = M[i][k]
        if pom != 0:
            break
    if pom != 0:
        break
if i + 1 < n:
    print("macierz nieodwracalna")
else:
    # print("wynik")
    # # wypisanie macierzy w postaci calkowicie zredukowanej
    # wypisz_rownanie()
    print("Macierz L")
    wypisz_macierz(L, n)
    print("Macierz U")
    wypisz_macierz(M, n)
    # # podstawianie w tyl
    # print("iksy:")
    # X = [1.0 for _ in range(n)]
    # X[n - 1] = (D[n - 1][0] / M[n - 1][n - 1])
    # for i in range(n - 2, -1, -1):
    #     suma = 0
    #     for k in range(i + 1, n):
    #         suma += M[i][k] * X[k]
    #     X[i] = ((D[i][0] - suma) / M[i][i])
    # for i in X:
    #     print(i)
    # macierz odwrotna
    L1 = odwroc_macierz_trojkatna(L, n)
    print("L-1")
    wypisz_macierz(L1, n)
    U1 = odwroc_macierz_trojkatna(M, n)
    print("U-1")
    wypisz_macierz(U1, n)
    A1 = przemnoz_macierze(U1, n, n, L1, n, n)
    print("macierz odwrotna A-1")
    wypisz_macierz(A1, n)
