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
livsmedelData = read_file("data/livsmedel-1.csv")
tjansteData = read_file("data/tjänster-1.csv")

print(kpiData[:3])
print("------")
print(tjansteData[:3])
print("------")
print(livsmedelData[:3])

# Uppgift 2
import matplotlib.pyplot as plt


def calculate_yearly_kpi_means():
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
    return sum([float(value) for value in year[1:]]) / (len(year) - 1)


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
        # Om användaren har valt en månad som inte har värde skippar vi den.
        if not len(year) - 1 < month:
            month_values.append(float(year[month]))

    return month_values


# Hjälpfunktion för att hämta alla år från filen
def get_years(list_of_years):
    years = []
    for year in list_of_years:
        # Året finns i första kolumnen
        years.append(int(year[0]))
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

years = get_years(kpiData[1:])
yearly_means = calculate_yearly_kpi_means()
monthly_kpis = get_kpis_for_month(month)

plt.plot(years, yearly_means, color="black", label="Linjediagram för medel-KPI")
plt.bar(years, yearly_means, label="KPI-medel")
plt.plot(years, monthly_kpis, color="red", label="Linjediagram för februari")
plt.title("Konsumentprisindex År 1980-2022")
plt.xlabel("År")
# Här sätter jag startvärden för x- och y-axeln
plt.xlim([1980, 2022])
plt.ylim([100, 400])
plt.ylabel("KPI")
plt.grid()
plt.legend()
plt.show()


def calculate_cost_increase(values):
    cost_differences = []
    for value in values:
        cost_differences.append(value / 100)
    return


# Uppgift 3
def plot_data(list_of_data):

    # Statisk lista med färger att sätta i grafen
    colors = ["red", "green", "blue", "black", "yellow", "orange", "brown", "magenta"]
    # Skippar första kolumnen som inte innehåller något år
    # Måste göra om strängar till int
    years = [int(year) for year in list_of_data[0][1:]]
    # Om första kolumnen i andra raden innehåller ordet "livsmedel" så är det tjänster
    if "livsmedel" in list_of_data[1][0]:
        plt.ylim([100, 1000])
        plt.title(
            f"Prisutveckling for olika kategorier av varor och tjänster År {years[0]}-{years[len(years)-1]}"
        )
    else:
        plt.ylim([100, 500])
        plt.title(
            f"Prisutveckling for olika livsmedel År {years[0]}-{years[len(years)-1]}"
        )
    i = 0
    for row in list_of_data[1:]:
        # Sätter x-limit till första och sista året i listan
        plt.xlim([years[0], years[len(years) - 1]])
        values = [float(value) for value in row[1:]]
        plt.plot(
            years,
            values,
            # Ett sätt att sätta ny färg dynamiskt
            color=colors[i],
            # Använd radbeskrivningen som label
            label=row[0],
        )
        i += 1
    plt.grid()
    plt.legend()
    plt.show()


plot_data(tjansteData)
plot_data(livsmedelData)
print("test")
