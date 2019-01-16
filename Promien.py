#Tworzenie zmiennych
c = 299792458.0
G = 0.0000000000667

#Zapytanie się o masę
print("Podaj masę ciałą dla którego chcesz obliczyć promień Schwarzschilda: ", end="")
masa = float(input())

#Liczenie
promien = (2*G)*masa / (c**2)

#Wypisanie na ekran
print("Promień Schwarzschilda dla masy " + str(masa) +  " kilogramów wynosi: " + str(promien) + " metra")

input("prompt: ")