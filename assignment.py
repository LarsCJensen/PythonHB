# Uppgift 1

import csv


def read_file(file_name):
    data_list = []
    # Använder with så att filen stängs automatiskt när man lämnar scopet av with
    with open(file_name, "r", encoding="UTF-8") as file:
        csv_reader = csv.reader(file, delimiter=";")
        # Lägger till varje rad till listan
        for line in csv_reader:
            data_list.append(line)

    return data_list


kpiData = read_file("data/kpi-1.csv")
tjansteData = read_file("data/livsmedel-1.csv")
livsmedelData = read_file("data/tjänster-1.csv")

print(kpiData[:3])
print("------")
print(tjansteData[:3])
print("------")
print(livsmedelData[:3])

# Uppgift 2
import matplotlib.pyplot as plt


def calculate_yearly_means():
    yearly_means = []
    for year in kpiData[1:]:
        yearly_means.append(_calculate_mean_for_year(year))
    # Vi vill ha värden i stigande årtalsordning
    yearly_means.reverse()
    return yearly_means


def _calculate_mean_for_year(year):
    # Första kolumnen innehåller året, så den tar vi bort när vi räknar på medelvärdet
    # Jag använder mig av list comprehension för att göra om värden till float innan
    # beräkning av medelvärdet
    return sum([float(value) for value in year[1:]]) / len(year) - 1


# Hjälpfunktion för att hämta KPI för en månad
def get_kpis_for_month(month):
    values = _get_values_for_month(month)
    # Vi vill ha värden i stigande årtalsordning
    values.reverse()
    return values


# Hjälpfunktion för att hämta ut värden för en specifik månad
def _get_values_for_month(month):
    month_values = []
    # Jag hoppar över första raden eftersom den innehåller rubriker
    for year in kpiData[1:]:
        # Eftersom första kolumnen innehåller året så skippar vi det i jämförelsen
        if not len(year) - 1 < month:
            month_values.append(year[month])

    return month_values


# Hjälpfunktion för att hämta alla år från filen
def get_years():
    years = []
    for year in kpiData[1:]:
        # Året finns i första kolumnen
        years.append(year[0])
    # Jag sorterar listan så att vi får åren i rätt ordning
    years.sort()
    return years


# Jag gör en oändlig loop tills användaren matar in ett accepterat värde
while True:
    month = input("För vilken månad som KPI ska presenteras? ")
    try:
        # Om användaren matat in ett värde som inte kan konverteras till int så
        # slängs ett ValueError och loopen kör vidare.
        month = int(month)
        if month > 12 or month < 0:
            continue
        # Vi har fått ett giltigt månadsnummer
        break
    except ValueError:
        continue

years = get_years()
yearly_means = calculate_yearly_means()
monthly_kpis = get_kpis_for_month(month)


plt.plot(yearly_means, color="black", label="Linjediagram för medel-KPI")
plt.bar(years, yearly_means, label="KPI-medel")
plt.plot(monthly_kpis, color="red", label="Linjediagram för februari")
plt.title("Konsumentprisindex År 1980-2022")
plt.xlabel("År")
plt.ylabel("KPI")
plt.grid()
plt.show()
print("tes")
