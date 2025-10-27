# -*- coding: utf-8 -*-
# ============================================================
# ÖVNINGAR – DEBUGG 10 (Dag 1)
# ------------------------------------------------------------
# Så här använder du filen:
# - Varje uppgift innehåller FEL KOD som kommentarer.
# - Läs "Vad ska det göra?" och "Ledtråd".
# - Avkommentera koden i uppgiften, kör, felsök och fixa.
# - Inga egna funktioner behövs/önskas i dessa övningar.
# ============================================================


# ------------------------------------------------------------
# 1) Split & strip – extra mellanslag kvar
# ------------------------------------------------------------
# FEL KOD (avkommentera för att testa):
# gäster = "Anna, Jesper,  Marcus"
# delar = gäster.split(",")
# print(delar)  # ska ge rena namn på separata rader
#
# Vad ska det göra?
# - Skriva namnen ett per rad, utan extra mellanslag.
# Ledtråd:
# - split räcker inte; trimma varje del med .strip()
# - skriv en rad i taget (loop) eller använd "\n".join(...)


# ------------------------------------------------------------
# 2) Heltal + sträng – typfel
# ------------------------------------------------------------
# FEL KOD (avkommentera för att testa):
# antal = "3"
# pris = 79
# total = antal * pris
# print("Totalt:", total, "kr")
#
# Vad ska det göra?
# - Multiplicera 3 med 79 och skriva totalsumman i kr.
# Ledtråd:
# - antal är sträng; konvertera till int före beräkningen.


# ------------------------------------------------------------
# 3) If-villkor – fel operator
# ------------------------------------------------------------
# FEL KOD (avkommentera för att testa):
# hastighet = 95
# grans = 90
# if hastighet < grans:
#     print("För fort")
# else:
#     print("OK")
#
# Vad ska det göra?
# - Meddela att 95 är "För fort".
# Ledtråd:
# - Jämför med rätt operator när hastighet är större än gränsen.


# ------------------------------------------------------------
# 4) Räkna 1..n – off-by-one
# ------------------------------------------------------------
# FEL KOD (avkommentera för att testa):
# n = 5
# for i in range(1, n):
#     print(i)
#
# Vad ska det göra?
# - Skriva 1, 2, 3, 4, 5 på varsin rad.
# Ledtråd:
# - range stoppar innan övre gränsen; justera slutvärdet.


# ------------------------------------------------------------
# 5) Tidsformat – modulus miss
# ------------------------------------------------------------
# FEL KOD (avkommentera för att testa):
# sek = 3725
# h = sek // 3600
# m = sek // 60
# s = sek % 60
# print(h, m, s)  # ska bli 1 2 5
#
# Vad ska det göra?
# - Visa 1 timme, 2 minuter, 5 sekunder.
# Ledtråd:
# - Minuter ska beräknas på återstoden efter timmarna, inte på totalen.


# ------------------------------------------------------------
# 6) Vokalräknare – saknar ÅÄÖ
# ------------------------------------------------------------
# FEL KOD (avkommentera för att testa):
# text = "Göteborg är härligt"
# vokaler = "aeiouyAEIOUY"
# antal = 0
# for ch in text:
#     if ch in vokaler:
#         antal += 1
# print("Vokaler:", antal)
#
# Vad ska det göra?
# - Räkna alla vokaler, även å/ä/ö (både små och stora).
# Ledtråd:
# - Utöka vokal-strängen med åäöÅÄÖ.


# ------------------------------------------------------------
# 7) Case-insensitive jämförelse – glömmer strip/lower
# ------------------------------------------------------------
# FEL KOD (avkommentera för att testa):
# a = " Hej"
# b = "hej  "
# if a == b:
#     print("lika")
# else:
#     print("olika")
#
# Vad ska det göra?
# - Säga "lika".
# Ledtråd:
# - Normalisera båda strängarna: .strip() och .lower() före jämförelse.


# ------------------------------------------------------------
# 8) FizzBuzz – ordningen i if/elif
# ------------------------------------------------------------
# FEL KOD (avkommentera för att testa):
# gräns = 15
# for i in range(1, gräns+1):
#     if i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 15 == 0:
#         print("FizzBuzz")
#     else:
#         print(i)
#
# Vad ska det göra?
# - Skriva "FizzBuzz" för tal delbara med både 3 och 5.
# Ledtråd:
# - Kontrollera fallet för både 3 och 5 först (annars hinner de tidigare träffa).


# ------------------------------------------------------------
# 9) Spegeltext – fel byggsätt
# ------------------------------------------------------------
# FEL KOD (avkommentera för att testa):
# s = "Python"
# rev = ""
# for ch in s:
#     rev = rev + s  # lägger till hela s varje varv
# print(rev)
#
# Vad ska det göra?
# - Skriva "nohtyP".
# Ledtråd:
# - Lägg till ett tecken i taget på rätt plats, t.ex. rev = ch + rev.


# ------------------------------------------------------------
# 10) Slicing – sista tecknet missas
# ------------------------------------------------------------
# FEL KOD (avkommentera för att testa):
# text = "Programmering"
# # plocka de sista 4 tecknen
# sista4 = text[len(text)-4 : len(text)-1]
# print(sista4)
#
# Vad ska det göra?
# - Visa de sista fyra tecknen i ordet.
# Ledtråd:
# - Slicing exkluderar slutindex; använd len(text) som övre gräns eller text[-4:].
