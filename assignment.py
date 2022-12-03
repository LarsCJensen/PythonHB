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


def calculate_and_get_yearly_kpi_means():
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
        # Om användaren har valt en månad som inte har värde sätter vi den till None.
        if not len(year) - 1 < month:
            month_values.append(float(year[month]))
        else:
            month_values.append(None)
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

months = ["Januari"]
years = get_years(kpiData[1:])
yearly_means = calculate_and_get_yearly_kpi_means()
monthly_kpis = get_kpis_for_month(month)

plt.plot(years, yearly_means, color="black", label="Linjediagram för medel-KPI")
plt.bar(years, yearly_means, label="KPI-medel")
plt.plot(
    years, monthly_kpis, color="red", label=f"Linjediagram för {kpiData[0][month]}"
)
plt.title("Konsumentprisindex År 1980-2022")
plt.xlabel("År")
# Här sätter jag startvärden för x- och y-axeln
plt.xlim([1980, 2022])
plt.ylim([100, 400])
plt.ylabel("KPI")
plt.grid()
plt.legend()
plt.show()


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


# Uppgift 4

# Hjälpmetod för att räkna ut prisförändringen över tid
def _get_price_diff_for_category(values):
    # Vi subtraherar sista värdet med första värdet för att få reda på skillnaden
    return float(values[len(values) - 1]) - float(values[0])


def print_price_over_time(list_of_data):
    title = ""
    title2 = "Prisutvecklingen i procentform"
    print("+----------------------------------------------------------------------+")
    # Tar reda på vilken data och anpassar rubriker
    if "livsmedel" in list_of_data[1][0]:
        title = "Kategorier av varor och tjänster"
    else:
        title = "Kategorier olika typer av livsmedel"
    # Skriv ut rubrikerna
    print(f"|{title:<40}|{title2:<15}")
    # Skippa första raden med kollumnnamn
    for row in list_of_data[1:]:
        price_diff = _get_price_diff_for_category(row[1:])
        # Skriv ut kategorin, vänsterställd 40 tecken lång och skillnaden med två decimaler
        print(f"|{row[0]:<40}|{price_diff:<15.2f}")


def plot_price_over_time():
    groceries_categories = []
    groceries_price_changes = []
    # Hämta ut kategorier och prisutveckling för livsmedeldata
    for row in livsmedelData[1:]:
        groceries_categories.append(row[0])
        groceries_price_changes.append(_get_price_diff_for_category(row[1:]))

    services_categories = []
    services_price_changes = []
    # Hämta ut kategorier och prisutveckling för tjänster
    for row in tjansteData[1:]:
        services_categories.append(row[0])
        services_price_changes.append(_get_price_diff_for_category(row[1:]))

    # Sätt storleken på plotytan
    fig, ax = plt.subplots(figsize=(16, 9))

    # Ta fram start och slutår och ha i titeln
    plt.title(
        f"Prisutveckling for olika varor och tjänster samt för olika typer av \
            livsmedel År {tjansteData[0][1]}-{tjansteData[0][len(tjansteData[0])-1]}"
    )
    plt.xlabel("Prisutveckling i procentform")
    plt.ylabel("Olika varor och tjänster samt för olika typer av livsmedel")

    # Skapa en horizontell bar med livsmedel
    ax.barh(groceries_categories, groceries_price_changes, color="darkblue")

    # Skapa en horizontell bar med tjänstedata
    ax.barh(services_categories, services_price_changes, color="blue")

    plt.show()


print_price_over_time(livsmedelData)
print_price_over_time(tjansteData)

plot_price_over_time()

# Uppgift 5
# Gå över kpidata, beräkna månad med störst KPI-förändring
# År | KPI-förändring i % | Månad | Årsmedel

# Hjälpmetod för att beräkna kpi-skillnader mellan månader
def _get_KPI_diff_for_months(month1, month2):
    return (month2 - month1) / month1


# Hjälpmetod för att beräkna kpi-skillnader för ett givet år
def _get_biggest_KPI_diff_for_year_index(yearly_kpis):
    kpi_diffs = []
    i = 0
    for kpi in yearly_kpis:
        # Vi skickar in nästa värde för att beräkna mot värdet innan
        kpi_diff = _get_KPI_diff_for_months(float(yearly_kpis[i + 1]), float(kpi))
        # Vi sparar skillnaden som absolut värde för att kunna beräkna största skillnaden
        kpi_diffs.append(abs(kpi_diff))
        i += 1
        # Om i är lika stort som längden på listan-1 (sista månaden) finns inga fler månader att beräkna
        if i == len(yearly_kpis) - 1:
            break
    # Vi returnerar indexet av det värde som är störst
    return kpi_diffs.index(max(kpi_diffs))


# Metod för att beräkna årliga KPI-skillnader för kpiData
def get_yearly_kpi_diffs():
    yearly_kpi_diffs = []
    yearly_kpis = []
    dec_value = None
    # Vi vill beräkna från 2000 - 2022
    kpi_data_reversed = kpiData[1:]
    kpi_data_reversed.reverse()
    # Vi återanvänder metoden för att räkna ut yearly means
    yearly_means = calculate_and_get_yearly_kpi_means()
    # Vi använder den här variabeln för att ta fram det årliga medelvärdet
    i = 0
    # Vi skippar första raden som innehåller rubriker
    for yearly_kpi in kpi_data_reversed:
        # Initierar tom dict att fylla med år och kpi-skillnad
        yearly_kpi_diff = {}
        yearly_kpis = yearly_kpi[1:]
        # Om vi har ett december-värde lägger vi till det först i listan av kpi:er
        if dec_value:
            yearly_kpis.insert(0, dec_value)

        # Vi hämtar ut indexet i listan som har störst skillnad
        biggest_diff_index = _get_biggest_KPI_diff_for_year_index(yearly_kpis)
        # Vi räknar ut för vilken månad som maxvärdet finns
        # Om decembervärdet är insertat måste vi ta hänsyn till det
        if dec_value:
            month = kpiData[0][biggest_diff_index + 1]
        else:
            month = kpiData[0][biggest_diff_index]
        # Sätter nyckeln till året och värdet till en dict med år och max-värdet av beräkningen
        yearly_kpi_diff[yearly_kpi[0]] = {
            month: yearly_kpis[biggest_diff_index],
            "yearly_mean": yearly_means[i],
        }
        yearly_kpi_diffs.append(yearly_kpi_diff)
        # Om året innehåller tolv månaders KPI sparar vi sista(dec) värdet
        if len(yearly_kpi[1:]) == 12:
            dec_value = yearly_kpis[len(yearly_kpis) - 1]
        i += 1

    return yearly_kpi_diffs


# Metod för att printa beräkningen till tabell
def print_yearly_kpi_changes(yearly_kpi_diffs):
    print("================================================================")
    title = "ANALYS AV KPI UNDER ÅREN 2000 - 2022"
    # Börja skriv ut titeln 100 tecken in
    print(f"{title:^100}")
    sub_title = "Största förändring"
    print(f"{sub_title:^100}")

    print(f"{'År':<15}{'%':<10}{'Månad':<15}{'Årsmedelvärde':<15}")
    for year in yearly_kpi_diffs:
        print(f"|{year[0]:<40}|{year:<15.2f}")


yearly_kpi_diffs = get_yearly_kpi_diffs()
print_yearly_kpi_changes(yearly_kpi_diffs)
