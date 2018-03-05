# Quiz z pierwszego dnia kursu
#
# Definicje zmiennych
x = 0
dobrze = "Dobrze!"
zle = "Może lepiej Ci pójdzie z następnym pytaniem... :-("
zle10 = "Chyba jednak nie."
blad = "Coś poszło nie tak. Spróbuj jeszcze raz."
zakonczenie = "Python gratuluje odwagi! :-)"
wynik1_3 = "Lepiej powtórz materiał."
wynik4_6 = "Nieźle, ale przyłóż się."
wynik7_9 = "Dobrze: keep calm and carry on."
wynik10 = "SUPER! Otrzymujesz czarny pas w sztuce walki z Pythonem :-)"
pytanie1 = "1. Które z poniższych zasobów są najlepsze do znalezienia wskazówek na temat Pythona: Facebook, Google czy Instagram?"
odp1 = ["Facebook", "Google", "Instagram"]
pytanie2 = "2. Jaki system liczbowy używany jest w komputerach: binarny, szesnastkowy czy dziesiętny?"
odp2 = ["binarny", "szesnastkowy", "dziesiętny"]
pytanie3 = "3. Częścią kodu w Pythonie są: instrukcje warunkowe, klemy, deoksyrybonukleotydy"
odp3 = ["instrukcje warunkowe", "klemy", "deoksyrybonukleotydy"]
pytanie4 = "4. W wierszu poleceń/terminalu, aby przejść do innej lokalizacji, używamy komendy: ls, emerge, cd"
odp4 = ["ls", "emerge", "cd"]
pytanie5 = "5. W wierszu poleceń/terminalu komenda służąca do utworzenia pliku to: create, touch, mkdir"
odp5 = ["create", "touch", "mkdir"]
pytanie6 = "6. Python to język: kompilowany, obcy, interpretowany"
odp6 = ["kompilowany", "obcy", "interpretowany"]
pytanie7 = "7. Jakim systemem wersjonowania plików jest Git: rozproszonym, centralnym, gwiezdnym"
odp7 = ["rozproszonym", "centralnym", "gwiezdnym"]
pytanie8 = "8. Git - jakim poleceniem pobrać zmiany ze zdalnego repozytorium: git pull, git add, git init"
odp8 = ["git pull", "git add", "git init"]
pytanie9 = "9. Skończony zestaw instrukcji potrzebnych do wykonania zadania to: zbiór instrukcji, archiwum, algorytm"
odp9 = ["zbiór instrukcji", "archiwum", "algorytm"]
pytanie10 = "10. Woda, kawa i herbata w Akademii są: niedostępne, gratis, płatne w chińskich yuanach"
odp10 = ["niedostępne", "gratis", "płatne w chińskich yuanach"]
#
#
#
# WPROWADZENIE
print()
print("""**QUIZ**

Witaj, śmiałku! :-)
Zmierz się z Pythonem po pierwszym dniu kursu.
Na każde pytanie jest tylko jedna prawidłowa odpowiedź.""")
print()
print("Startujemy?")
while True:
    odp_0 = input("tak/nie: ")
    if odp_0 == "tak":
        print()
        print(pytanie1)
        break
    elif odp_0 == "nie":
        print("Szkoda. Pa, pa!")
        exit()
    else:
        print(blad)

# Pytanie 1
while True:
    odp_1 = input("Odp.: ")
    if odp_1 == "Google":
        print(dobrze)
        x += 1
        print()
        print(pytanie2)
        break
    elif odp_1 == "Facebook":
        print(zle)
        print()
        print(pytanie2)
        break
    elif odp_1 == "Instagram":
        print(zle)
        print()
        print(pytanie2)
        break
    elif odp_1 != odp1[0:3]:
        print(blad)

# Pytanie 2
while True:
    odp_2 = input("Odp.: ")
    if odp_2 == "binarny":
        print(dobrze)
        x += 1
        print()
        print(pytanie3)
        break
    elif odp_2 == "szesnastkowy":
        print(zle)
        print()
        print(pytanie3)
        break
    elif odp_2 == "dziesiętny":
        print(zle)
        print()
        print(pytanie3)
        break
    elif odp_2 != odp2[0:3]:
        print(blad)

# Pytanie 3
while True:
    odp_3 = input("Odp.: ")
    if odp_3 == "instrukcje warunkowe":
        print(dobrze)
        x += 1
        print()
        print(pytanie4)
        break
    elif odp_3 == "klemy":
        print(zle)
        print()
        print(pytanie4)
        break
    elif odp_3 == "deoksyrybonukleotydy":
        print(zle)
        print()
        print(pytanie4)
        break
    elif odp_3 != odp3[0:3]:
        print(blad)

# Pytanie 4
while True:
    odp_4 = input("Odp.: ")
    if odp_4 == "cd":
        print(dobrze)
        x += 1
        print()
        print(pytanie5)
        break
    elif odp_4 == "ls":
        print(zle)
        print()
        print(pytanie5)
        break
    elif odp_4 == "emerge":
        print(zle)
        print()
        print(pytanie5)
        break
    elif odp_4 != odp4[0:3]:
        print(blad)

# Pytanie 5
while True:
    odp_5 = input("Odp.: ")
    if odp_5 == "touch":
        print(dobrze)
        x += 1
        print()
        print(pytanie6)
        break
    elif odp_5 == "create":
        print(zle)
        print()
        print(pytanie6)
        break
    elif odp_5 == "mkdir":
        print(zle)
        print()
        print(pytanie6)
        break
    elif odp_5 != odp5[0:3]:
        print(blad)

# Pytanie 6
while True:
    odp_6 = input("Odp.: ")
    if odp_6 == "interpretowany":
        print(dobrze)
        x += 1
        print()
        print(pytanie7)
        break
    elif odp_6 == "obcy":
        print(zle)
        print()
        print(pytanie7)
        break
    elif odp_6 == "kompilowany":
        print(zle)
        print()
        print(pytanie7)
        break
    elif odp_6 != odp6[0:3]:
        print(blad)

# Pytanie 7
while True:
    odp_7 = input("Odp.: ")
    if odp_7 == "rozproszonym":
        print(dobrze)
        x += 1
        print()
        print(pytanie8)
        break
    elif odp_7 == "gwiezdnym":
        print(zle)
        print()
        print(pytanie8)
        break
    elif odp_7 == "centralnym":
        print(zle)
        print()
        print(pytanie8)
        break
    elif odp_7 != odp7[0:3]:
        print(blad)

# Pytanie 8
while True:
    odp_8 = input("Odp.: ")
    if odp_8 == "git pull":
        print(dobrze)
        x += 1
        print()
        print(pytanie9)
        break
    elif odp_8 == "git add":
        print(zle)
        print()
        print(pytanie9)
        break
    elif odp_8 == "git init":
        print(zle)
        print()
        print(pytanie9)
        break
    elif odp_8 != odp8[0:3]:
        print(blad)

# Pytanie 9
while True:
    odp_9 = input("Odp.: ")
    if odp_9 == "algorytm":
        print(dobrze)
        x += 1
        print()
        print(pytanie10)
        break
    elif odp_9 == "zbiór instrukcji":
        print(zle)
        print()
        print(pytanie10)
        break
    elif odp_9 == "archiwum":
        print(zle)
        print()
        print(pytanie10)
        break
    elif odp_9 != odp9[0:3]:
        print(blad)

# Pytanie 10
while True:
    odp_10 = input("Odp.: ")
    if odp_10 == "gratis":
        print(dobrze)
        x += 1
        print()
        print(zakonczenie)
        break
    elif odp_10 == "płatne w chińskich yuanach":
        print(zle10)
        print()
        print(zakonczenie)
        break
    elif odp_10 == "niedostępne":
        print(zle10)
        print()
        print(zakonczenie)
        break
    elif odp_10 != odp10[0:3]:
        print(blad)

# Zakończenie
print()
print("Twój wynik to:", x, "/10")
if x == 10:
    print(wynik10)
elif x > 6 and x < 10:
    print(wynik7_9) and exit()
elif x < 7 and x > 3:
    print(wynik4_6) and exit()
else:
    print(wynik1_3) and exit()
