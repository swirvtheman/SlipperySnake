# -*- coding: utf-8 -*-
# ============================================================
# ÖVNINGAR – DAG 1 (kluriga grunder, utan egna funktioner)
# ------------------------------------------------------------
# Så här använder du filen:
# 1) Varje uppgift är helt kommenterad. Välj en uppgift.
# 2) Avkommentera (ta bort "# " i början på rader) under den uppgiften.
# 3) Kör filen och testa. Lägg tillbaka kommentarer när du är klar.
# 4) "Uppgradera med input" finns som tips under varje uppgift.
# OBS: Inga egna def-funktioner i denna fil – håll allt på grundnivå.
# ============================================================

# ------------------------------------------------------------
# Done!!!1) Biljettkassan – summera inkomster (split, strip, int, loop)
# ------------------------------------------------------------
# Startvärden (hårdkodat):
# belopp = "120, 75, 120, 90, 75"
#
# Instruktion:
# - Dela strängen med split(",")
# - Ta bort mellanslag runt varje del med strip()
# - Konvertera varje del till int i en loop
# - Räkna antal biljetter och total summa
# - Skriv en kort sammanfattning
#
# Exempelkod att avkommentera:
#"from posixpath import split


#belopp = input("Skriv belopp separerade med kommatecken: ")
#delar = belopp.split(",")
#total = 0
#antal = 0
#for d in delar:
#     pris = int(d.strip())
#     total += pris
#     antal += 1
#print("Antal biljetter:", antal)
#print("Total summa:", total, "kr")
#
# Uppgradera med input:
 

# ------------------------------------------------------------
# Done!!!!2) Temperaturvakt – klassificera mätningar (if/elif, loop, räknare)
# ------------------------------------------------------------
# Startvärden:
# temps = [2.5, 7.0, 12.3, 16.8, 22.0, 28.1]
#
# Instruktion:
# - Bestäm egna intervall för "kallt/svalt/lagom/varmt/hett"
# - Loopa igenom temps och skriv klassificering för varje
# - Räkna hur många som är "lagom" (använd en räknare)
#
# Exempelkod:
#temps = [2.5, 7.0, 12.3, 16.8, 22.0, 28.1] 
#temps = [int(input(" Write the temperature: "))]
#lagom_count = 0
 
#for t in temps:
#     if t < 5:
#         kategori = "kallt"
#     elif t <= 10:
#         kategori = "svalt"
#     elif t <= 20:
#         kategori = "lagom"
#         lagom_count += 1
#     elif t <= 27:
#         kategori = "varmt"
#     else:
#         kategori = "hett"
#     print(t, "->", kategori)
#     print("Antal 'lagom':", lagom_count)
#
# Uppgradera med input:
# Läs gränserna (t.ex. kall/svalt/lagom/varmt/hett) via input och använd dem i if-satsen.

# ------------------------------------------------------------
# Done!!!!!3) Mini-kalkylator (if/elif/else, typkonvertering, delningsvakt)
# ------------------------------------------------------------
# Startvärden:
# a = 15
# b = 0
# op = "/"
#
# Instruktion:
# - Om op är "+", "-", "*", "/" -> beräkna resultat
# - Om op är "/" och b==0 -> skriv vänligt felmeddelande
#
# Exempelkod:
#a = float(input("a: "))
#b = float(input("b: "))
#op = input("Operator (+ - * /): ")
#if op == "+":
#    print(a + b)
#elif op == "-":
#    print(a - b)
#elif op == "*":
#    print(a * b)
#elif op == "/":
#    if b == 0:
#        print("Kan inte dela med noll.")
#    else:
#        print(a / b)
#else:
#    print("Okänd operator:", op)
#
# Uppgradera med input:
# a = float(input("a: ")); b = float(input("b: ")); op = input("Operator (+ - * /): ")

# ------------------------------------------------------------
#Done!!! 4) Gästlista – snygg split (split, strip, sträng → lista → strängar)
# ------------------------------------------------------------
# Startvärden:
# gäster = "Anna, Jesper,  Marcus  ,Linn  "
#
# Instruktion:
# - Dela på kommatecken
# - Trimma mellanslag
# - Skriv ett namn per rad
#
# Exempelkod:
#gäster = "Anna, Jesper,  Marcus  ,Linn  "
#gäster = input("Skriv namn, separerade med kommatecken: ")
#delar = gäster.split(",")
#for namn in delar:
#    print(namn.strip())

#Uppgradera med input:
#gäster = input("Skriv namn, separerade med kommatecken: ")

# ------------------------------------------------------------
# 5) Loggbok – räkna vokaler (loop, strängtest, å/ä/ö)
# ------------------------------------------------------------
# Startvärden:
# text = "Systemstart kl 07:15 i Göteborg"
#
# Instruktion:
# - Gå igenom text tecken för tecken
# - Räkna hur många vokaler som finns (a e i o u y å ä ö, även versaler)
# - Skriv antalet
#
# Exempelkod:
# text = "Systemstart kl 07:15 i Göteborg"
# vokaler = "aeiouyåäöAEIOUYÅÄÖ"
# antal = 0
# for ch in text:
#     if ch in vokaler:
#         antal += 1
# print("Antal vokaler:", antal)
#
# Uppgradera med input:
# text = input("Skriv en kort text: ")

# ------------------------------------------------------------
# 6) Lösenords-check light (längd + minst en siffra, loop och flagga)
# ------------------------------------------------------------
# Startvärden:
# pwd = "Passw0rd"
#
# Instruktion:
# - "Godkänt" om längd >= 8 och minst en siffra finns
# - Annars "för svagt"
# - Hitta siffra genom att loopa tecken och sätta en bool-flagga
#
# Exempelkod:
# pwd = "Passw0rd"
# har_siffra = False
# for ch in pwd:
#     if ch.isdigit():
#         har_siffra = True
# if len(pwd) >= 8 and har_siffra:
#     print("Godkänt")
# else:
#     print("För svagt")
#
# Uppgradera med input:
# pwd = input("Lösenord: ")

# ------------------------------------------------------------
# 7) Rabattstegar i butik (if/elif, procent, beräkning)
# ------------------------------------------------------------
# Startvärden:
# belopp = 1350.0
#
# Instruktion:
# - Om belopp >= 2000 -> 20%
# - Elif belopp >= 1000 -> 10%
# - Annars -> 0%
# - Räkna slutpris och skriv vilken nivå som gällde
#
# Exempelkod:
# belopp = 1350.0
# rabatt = 0.0
# nivå = "ingen"
# if belopp >= 2000:
#     rabatt = 0.20
#     nivå = "20%"
# elif belopp >= 1000:
#     rabatt = 0.10
#     nivå = "10%"
# slutpris = belopp * (1 - rabatt)
# print("Nivå:", nivå)
# print("Att betala:", slutpris, "kr")
#
# Uppgradera med input:
# belopp = float(input("Belopp: "))

# ------------------------------------------------------------
# 8) Multiplikationstabell (for-loop, formatering)
# ------------------------------------------------------------
# Startvärden:
# n = 7
#
# Instruktion:
# - Skriv n × 1..10 rad för rad
#
# Exempelkod:
# n = 7
# for i in range(1, 11):
#     print(n, "*", i, "=", n*i)
#
# Uppgradera med input:
# n = int(input("Tal: "))

# ------------------------------------------------------------
# 9) Fakultet med while (ackumulator, while, multiplikation)
# ------------------------------------------------------------
# Startvärden:
# n = 6
#
# Instruktion:
# - Beräkna n! med en while-loop
# - Använd en ackumulator som startar på 1
#
# Exempelkod:
# n = 6
# res = 1
# i = 2
# while i <= n:
#     res *= i
#     i += 1
# print(n, "!", "=", res)
#
# Uppgradera med input:
# n = int(input("n (>=0): "))

# ------------------------------------------------------------
# 10) Gissa talet (simulerad lista) (for, break, jämförelse)
# ------------------------------------------------------------
# Startvärden:
# hemligt = 17
# gissningar = [10, 20, 17]
#
# Instruktion:
# - Loopa över gissningar
# - Skriv "för lågt" / "för högt" tills rätt
# - Skriv "Rätt!" och avbryt (break) när det blir rätt
#
# Exempelkod:
# hemligt = 17
# gissningar = [10, 20, 17]
# for g in gissningar:
#     if g < hemligt:
#         print(g, "är för lågt")
#     elif g > hemligt:
#         print(g, "är för högt")
#     else:
#         print("Rätt!")
#         break
#
# Uppgradera med input:
# while True:
#     g = int(input("Gissa: "))
#     if g < hemligt: print("för lågt")
#     elif g > hemligt: print("för högt")
#     else: print("Rätt!"); break

# ------------------------------------------------------------
# 11) Primtalstest – enkel variant (for, flagga)
# ------------------------------------------------------------
# Startvärden:
# n = 29
#
# Instruktion:
# - Anta är_prim = True
# - Testa delare 2..n-1
# - Om delbart -> sätt False och avbryt
# - Skriv True/False på slutet
#
# Exempelkod:
# n = 29
# är_prim = True
# if n < 2:
#     är_prim = False
# else:
#     for d in range(2, n):
#         if n % d == 0:
#             är_prim = False
#             break
# print(är_prim)
#
# Uppgradera med input:
# n = int(input("Tal > 1: "))

# ------------------------------------------------------------
# 12) Spegeltext – utan slicing (loop, bygga sträng)
# ------------------------------------------------------------
# Startvärden:
# s = "Python"
#
# Instruktion:
# - Skapa en tom sträng
# - Bygg den baklänges genom att lägga till tecken i början eller slutet
#
# Exempelkod:
# s = "Python"
# rev = ""
# for ch in s:
#     rev = ch + rev   # läggs framför för baklänges
# print(rev)
#
# Uppgradera med input:
# s = input("Text: ")

# ------------------------------------------------------------
# 13) Tidsomvandlare – hh:mm:ss (// och %)
# ------------------------------------------------------------
# Startvärden:
# sek = 3725
#
# Instruktion:
# - Beräkna h = sek // 3600
# - m = (sek % 3600) // 60
# - s = sek % 60
# - Skriv med tvåsiffrig form: hh:mm:ss
#
# Exempelkod:
# sek = 3725
# h = sek // 3600
# m = (sek % 3600) // 60
# s = sek % 60
# print(f"{h:02d}:{m:02d}:{s:02d}")
#
# Uppgradera med input:
# sek = int(input("Sekunder: "))

# ------------------------------------------------------------
# 14) Lista → summa och största (utan sum/max) (loop, jämförelse)
# ------------------------------------------------------------
# Startvärden:
# tal = [3, 7, 11, -2, 10]
#
# Instruktion:
# - Gå igenom listan en gång
# - Håll två variabler: summa och största
# - Uppdatera dessa i loopen
#
# Exempelkod:
# tal = [3, 7, 11, -2, 10]
# summa = 0
# största = tal[0]
# for x in tal:
#     summa += x
#     if x > största:
#         största = x
# print("Summa:", summa)
# print("Största:", största)
#
# Uppgradera med input:
# Läs tal från användaren rad för rad tills tom rad → avbryt.

# ------------------------------------------------------------
# 15) Case-insensitive jämförelse (strip, lower)
# ------------------------------------------------------------
# Startvärden:
# a = " Hej"
# b = "hej  "
#
# Instruktion:
# - Normalisera båda med strip() och lower()
# - Skriv "lika" om de matchar, annars "olika"
#
# Exempelkod:
# a = " Hej"
# b = "hej  "
# if a.strip().lower() == b.strip().lower():
#     print("lika")
# else:
#     print("olika")
#
# Uppgradera med input:
# a = input("Ord 1: "); b = input("Ord 2: ")

# ------------------------------------------------------------
# 16) FizzBuzz (if/elif/else + loop)
# ------------------------------------------------------------
# Startvärden:
# gräns = 30
# fizz = 3
# buzz = 5
#
# Instruktion:
# - Skriv 1..gräns
# - Multiplar av fizz → "Fizz"
# - Multiplar av buzz → "Buzz"
# - Multiplar av båda → "FizzBuzz"
# - Annars talet
#
# Exempelkod:
# gräns = 30
# fizz = 3
# buzz = 5
# for i in range(1, gräns+1):
#     if i % (fizz * buzz) == 0:
#         print("FizzBuzz")
#     elif i % fizz == 0:
#         print("Fizz")
#     elif i % buzz == 0:
#         print("Buzz")
#     else:
#         print(i)
#
# Uppgradera med input:
# gräns = int(input("Gräns: ")); fizz = int(input("Fizz: ")); buzz = int(input("Buzz: "))

# ------------------------------------------------------------
# 17) Rektangel av stjärnor (nästlade loopar)
# ------------------------------------------------------------
# Startvärden:
# bredd = 5
# höjd = 3
#
# Instruktion:
# - Skriv en rektangel av '*' i storleken bredd × höjd
#
# Exempelkod:
# bredd = 5
# höjd = 3
# for _ in range(höjd):
#     rad = ""
#     for _ in range(bredd):
#         rad += "*"
#     print(rad)
#
# Uppgradera med input:
# bredd = int(input("Bredd: ")); höjd = int(input("Höjd: "))

# ------------------------------------------------------------
# 18) Säker heltals-input (try/except + while)
# ------------------------------------------------------------
# Startvärden: – (denna är input-baserad)
#
# Instruktion:
# - Läs en sträng med input()
# - Försök int(...) i try/except
# - Vid fel: skriv felmeddelande och be igen (while-slinga)
# - Vid lyckad konvertering: skriv talet
#
# Exempelkod:
# while True:
#     s = input("Heltal: ")
#     try:
#         n = int(s)
#         print("Tack! Du skrev:", n)
#         break
#     except ValueError:
#         print("Det där var inte ett heltal, försök igen.")

# ------------------------------------------------------------
# 19) Räkna ord tills "stopp" (while, räknare, lower/strip)
# ------------------------------------------------------------
# Startvärden: – (du kan simulera med en lista om du vill)
#
# Instruktion:
# - Läs ord i en while True
# - Om ordet (case-insensitive) är "stopp" → bryt
# - Annars öka en räknare
# - Skriv hur många ord som registrerats
#
# Exempelkod (input-baserad):
# count = 0
# while True:
#     ordet = input("Skriv ett ord (stopp för att avsluta): ").strip().lower()
#     if ordet == "stopp":
#         break
#     if ordet:   # räkna bara icke-tomma
#         count += 1
# print("Antal ord:", count)
#
# Exempelkod (simulerad lista, utan input):
# ord_lista = ["hej", "på", "dig", "stopp", "mer"]
# count = 0
# for o in ord_lista:
#     if o.strip().lower() == "stopp":
#         break
#     if o.strip() != "":
#         count += 1
# print("Antal ord:", count)

# ------------------------------------------------------------
# 20) Kvittoformatterare (sträng + tal, multiplikation)
# ------------------------------------------------------------
# Startvärden:
# butik = "Teknikhörnan"
# vara = "USB-kabel"
# pris = 79
# antal = 3
#
# Instruktion:
# - Beräkna totalsumma (pris * antal)
# - Skriv en enradig kvittotext där text och siffror kombineras
# - Ingen decimalprecision krävs
#
# Exempelkod:
# butik = "Teknikhörnan"
# vara = "USB-kabel"
# pris = 79
# antal = 3
# total = pris * antal
# print(f"{butik}: {vara} x {antal} = {total} kr")
#
# Uppgradera med input:
# butik = input("Butik: "); vara = input("Vara: ")
# pris = int(input("Pris (heltal): ")); antal = int(input("Antal: "))
