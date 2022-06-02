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


def podziel_wiersz(M, wiersz, dzielnik):
    for k in range(n):
        M[wiersz][k] /= dzielnik


# funkcja odjecie wiersza pomnozonego przez cos
# mnozenie -mnozymy licznik i mianownik
# odejmowanie
def odejmij_wiersze(M, odjemna, odjemnik, mnoznik):
    for k in range(n):
        M[odjemna][k] -= M[odjemnik][k] * mnoznik


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


def wyznacz_macierz_Mij(A, n, i, j):  # i,j - zaczynaja sie od 1
    Mij = []
    for w in range(n):
        if w == i - 1:
            pass
        else:
            kosz = []
            for k in range(n):
                if k == j - 1:
                    pass
                else:
                    kosz.append(A[w][k])
            Mij.append(kosz)
    return Mij


def oblicz_dopelnienie(A, n, i, j):
    Mij = wyznacz_macierz_Mij(A, n, i, j)
    return pow(-1, i + j) * oblicz_wyznacznik(Mij, n - 1)


def oblicz_wyznacznik(A, n):
    if n == 1:
        return A[0][0]
    else:
        wyznacznik = 0
        for k in range(n):
            wyznacznik += A[0][k] * oblicz_dopelnienie(A, n, 1, k + 1)
        return wyznacznik


# GLOBALNE
# wczytanie danych
print("n: ")
print("macierz:")
n = int(input())
M = []
U = []
L = []
for w in range(n):
    M.append([float(x) for x in input().split()])
L = [[0.0 for _ in range(n)] for _ in range(n)]
for w in range(n):
    L[w][w] = 1.0
U = [[0.0 for _ in range(n)] for _ in range(n)]
# PROGRAM
if oblicz_wyznacznik(M, n) == 0:
    print("macierz nieodwracalna")
else:
    for i in range(n):
        for j in range(i, n):
            suma = 0
            for k in range(i):
                suma += L[i][k] * U[k][j]
            U[i][j] = M[i][j] - suma
        for j in range(i + 1, n):
            suma = 0
            for k in range(i):
                suma += L[j][k] * U[k][i]
            L[j][i] = (M[j][i] - suma) / U[i][i]
    print("Macierz L")
    wypisz_macierz(L, n)
    print("Macierz U")
    wypisz_macierz(U, n)
    L1 = odwroc_macierz_trojkatna(L, n)
    print("L-1")
    wypisz_macierz(L1, n)
    U1 = odwroc_macierz_trojkatna(U, n)
    print("U-1")
    wypisz_macierz(U1, n)
    A1 = przemnoz_macierze(U1, n, n, L1, n, n)
    print("macierz odwrotna A-1")
    wypisz_macierz(A1, n)
