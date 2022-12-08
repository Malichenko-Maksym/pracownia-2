"""Klasa, w ktorej mozna zrealizowac rozwiazanie Zadania 1"""

import uklad, wykresy
import iteracjaprosta, iteracjaseidela
import numpy as np

class Zadanie1:

    def __init__(self):
        """Konstruktor"""
        self.k = 5            # liczba pomiarow dla jednej wartosci parametru
        
    def testy(self):
        """Testy wstepne"""
        # miejsce na rozwiazanie pierwszej czesci zadania 1
        self.n=80
        self.norma = 1
        self.eps = 1e-10
        # okreslam uklad rownan
        u1 = uklad.Uklad(wymiar = self.n)
        # losujemy uklad
        u1.losuj_uklad_symetryczny_dodatnio_okreslony()
        # rozwiazuje uklad z wykorzystaniem metody iteracji prostej
        
        test1 = iteracjaprosta.IteracjaProsta(ukl = u1)
        test1.przygotuj()
        
        # losuje wektor poczatkowy
        wek = np.random.random([self.n, 1])
        # obliczam norme tego wektora
        norma_wek = u1.norma_wektora(typ = self.norma, wektor = wek)
        # skaluje wylosowany wektor i tworze 2 wektory o roznych normach
        sk1 = pow(10, 3)/norma_wek
        wek1 = wek.copy()*sk1

        iter1 = test1.iteruj_roznica(eps = self.eps, norma = self.norma, wyswietlaj=0, X0=wek1)
        niedokl1 = test1.sprawdz_rozwiazanie(self.norma)
        print("Dla rozmiaru macierzy ",self.n," oraz eps=",self.eps,":")
        print("Liczba iterecji: ",iter1)
        print("Niedokładność oszacowania: ",niedokl1)
        print(u1.norma_macierzy(typ=1))
       
        return 0
        
    def badaj_zbieznosc(self):
        """Badam zbieznosc metody iteracyjnej"""
        # miejsce na realizacje eksperymentu - drugiej czesci zadania 1

        return 0

z1=Zadanie1()
z1.testy()