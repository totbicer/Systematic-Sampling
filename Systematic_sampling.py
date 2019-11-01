#!/usr/bin/env python 3
# -*- coding: UTF-8 -*-
karsilama= """
_____________________________________________________________________________________
S Y S T E M A T I C    S A M P L I N G   P R O G R A M 
                                   Vesion: (P).2.1
by Tülin (Otbiçer) ACAR \u00A9 2019 (P)arantez Education Research Consultancy and Publishing
https://parantezanaliz.com & totbicer@gmail.com
_____________________________________________________________________________________"""
print(karsilama)

evren = input("1# The size of the universe defined and limited (N): ")
while True:
        if evren.isdigit() and int(evren)>0:
                break
        else:
                print("You logged in incorrectly. You must enter a naturel number greater than zero.")
                evren = input("1# The size of the universe defined and limited (N): ")
        
                                        
orneklem = input("2# Sample size (Ss) : ")
while True:
        if orneklem.isdigit() and int(orneklem)>0:
                break
        else:
                print("You logged in incorrectly. You must enter a naturel number greater than zero.")
                rneklem = input("2# Sample size (Ss) :  ")
N=int(evren)
s=int(orneklem)
k=int(round(N/s))

import random
baslangic = random.randint(1, k) #1 ile k arasında random tam sayı seçer. random.randrange(k) komutu ile eşdeğer.
print("\n >>> C A L C U L A T E D    R E S U L T <<<\n The number of universes are ", N, " and The sample size is ", s , "\nSystematic sample selection coefficient (k) =", k, "and", "Start sequence number (Ssn) =", baslangic)
print ("\nThe sequence numbers of the units to be sampled according to the systematic sampling method are listed below.")
print(*range(baslangic, N, k), sep="\t" )

a = input()

