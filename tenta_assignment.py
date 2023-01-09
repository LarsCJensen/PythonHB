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
print(f"Volymen är {round(volymKon(3, 6), 1)}")

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


find_values()


# Uppgift 2
