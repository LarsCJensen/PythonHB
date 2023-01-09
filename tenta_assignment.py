# Uppgift 1a
import math

# Hjälpmetod för att beräkan basen på en kon
def areaKon(r):
    # Beräkna basarean på godtycklig radie och returnera den
    return math.pi * r * r


# Hjälpmetod för att beräkna volumen för en kon
def volymKon(r, h):
    bas = areaKon(r)
    # returnera volymen enligt formeln
    return (bas * h) / 3


# Jag avrundar talet till 1 decimal innan jag printar det
# print(f"Volymen är {round(volymKon(3, 6), 1)}")

# Uppgift 1b
import random
import copy

# Hjälpmetod för att generera lista med ett visst antal element
def generate_list(num_elements):
    # Jag sätter range för randint så vi endast får värden mellan 0 och 100
    # Skapar en tvådimensionell lista via list-comprehension
    list = [
        [random.randint(0, 100) for i in range(num_elements)]
        for j in range(num_elements)
    ]
    return list


# Metod för att hitta värden i en lista
def find_values():
    values_to_find = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    list_of_numbers = generate_list(4)
    # Jag kopierar den randomiserade listan för att kunna göra ändringar utan att
    # ändra i den "riktiga" listan
    modified_list = copy.deepcopy(list_of_numbers)
    print("Talen som vi har hittat är:")
    # Loopa över listans rader
    for i in range(len(list_of_numbers)):
        # Loopa över värden som ska hittas
        for value in values_to_find:
            try:
                result = list_of_numbers[i].index(value)
                print(f"{value} som är i position {i, result}")
                modified_list[i][result] = "Hittad"
            except:
                # Om värdet inte kan hittas slängs ett exception som vi bara ignorerar
                # och låter loopen fortsätta
                continue

    print(f"Den slumpmässigt skapade listan är: {list_of_numbers}")
    print(f"Den modifierade lista är: {modified_list}")


# find_values()


# Uppgift 2a
import random


def singlaslant():
    while True:
        number = input("Skriv in önskat antal kast:")
        try:
            # Om användaren matat in ett värde som inte kan konverteras till int så
            # slängs ett ValueError och loopen kör vidare.
            number_of_throws = int(number)
            # Vi har fått ett korrekt värde
            break
        except ValueError:
            print("Vänligen ange korrekt siffra")
            continue
    krona = 0
    klave = 0
    # Loopa över antal inmatade rundor
    for i in range(number_of_throws):
        # om 0, är det krona, om 1 är det klave
        if random.randint(0, 1) == 0:
            krona += 1
        else:
            klave += 1

    print(f"Tack, jag kastar myntet {number_of_throws} gånger:")
    print(f"Utfallet blev {krona} Krona och {klave} Klave.")


# singlaslant()

# Uppgift 2b

# Hjälpmetod som validerar att personnumret är giltigt
def _valid_pers_no(pers_no):
    # Om användaren matat in fler eller färre siffror
    if len(pers_no) != 6:
        return False
    # Om månaden inte är giltig (större än 12)
    if int(pers_no[2:4]) > 12:
        return False
    # Om dagen inte är giltig (större än 31)
    if int(pers_no[4:6]) > 31:
        return False
    return True


# Hjälpmetod som validerar att lösenordet är giltigt
def _valid_password(password):
    # Om inte lösenordet är tio tecken eller mer
    if len(password) < 10:
        return False
    # Om inte lösenordet innehåller en stor bokstav
    if not any(char.isupper() for char in password):
        return False
    # Om inte lösenordet innehåller en liten bokstav
    if not any(char.islower() for char in password):
        return False
    # Om lösenordet inte innehåller något av specialtecknen
    if not any(
        char
        in ["$", "%", "&", "~", "!", "@", "#", "^", "*", "(", ")", "_", "-", "+", "="]
        for char in password
    ):
        return False
    return True


def generate_user():
    name = input("Skriv in ditt förnamn: ")
    surname = input("Skriv in ditt efternamn: ")
    # Loopa tills giltigt personnummer angivits
    while True:
        pers_no = input("Skriv in ditt födelsedatum (6 siffror): ")
        if _valid_pers_no(pers_no):
            print("Födelsedatumet är giltigt.")
            break
        else:
            print("Det var inte ett korrekt födelsedatum. Gör om.")
    # Loopa tills giltigt lösenord angivits
    while True:
        pw = input("Ange önskat lösenord: ")
        if _valid_password(pw):
            print("Lösenordet uppfyller kraven.")
            break
        else:
            print("Lösenordet uppfyller inte kraven. Gör om.")
    # Skapa användarnamnet av de fyra första bokstäverna i förnamn och fyra sista i
    # efternamn och personnummer
    username = name[:4] + surname[-4:] + pers_no[-4:]
    print(f"Ditt användarnamn är {username} och ditt lösenord är {pw}")


# generate_user()

# Assignment 2c
def Sort(lista, N):
    for i in range(N):
        # Här ska minindex sättas till i och inte 0
        min_index = i
        for j in range(i + 1, N):
            # Här ska jämförelsen vara mindre än, inte större
            if lista[j] < lista[min_index]:
                # Och min_index ska sättas till j, inte i
                min_index = j
        temp = lista[i]
        # Här ska det vara lista[i] och inte j
        lista[i] = lista[min_index]
        lista[min_index] = temp
    return lista


listan = [5, 45, -4, 101, 78, 188, 97, -104, 47]
print(f"Listan som ska sorteras är {listan} \n")
N = len(listan)
sorteradLista = Sort(listan, N)
print(f"Den sorterade listan är {sorteradLista}")
