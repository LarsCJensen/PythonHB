import csv  # Import module csv

# Create a funtion that takes filename as argument and returns a list of the file contents
def read_file(filename):
    data_list = []  # Be sure that the list is empty (should be)
    # Open file and read all data. File will automatically be closed.
    with open(filename, "r", encoding="UTF-8") as file:
        csv_data = csv.reader(file, delimiter=";")

        # Store read data in a list
        for row in csv_data:
            data_list.append(row)

    return data_list


list = read_file("kpi-1.csv")
for line in range(2):
    print(list[line])

list = read_file("tjänster-1.csv")
for line in range(2):
    print(list[line])


# Make a list for the selected month
# Parameter: Selected month (int), string elements during the year
def month_list(month, list):
    # Check that specified month are in the list (2022 is up to July)
    if (len(list)) >= 1 + month:
        return float(list[month])
    else:
        return float(list[len(list) - 1])


def month_Name(month):
    MonthNameList = [
        "januari",
        "februari",
        "mars",
        "april",
        "maj",
        "juni",
        "juli",
        "augusti",
        "september",
        "oktober",
        "november",
        "december",
    ]
    return MonthNameList[month - 1]


def month_Name_Short(month):
    MonthNameList = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "Maj",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Okt",
        "Nov",
        "Dec",
    ]
    return MonthNameList[month - 1]


# Calculate mean value per year.
# Parameter is a value list of string elements during the year
# Return list first value in the list and mean values of all other elements
def mean_list(list):
    mean_value = 0
    for i in range(1, len(list)):
        mean_value += float(list[i])
    return list[0], mean_value / (len(list) - 1)


import matplotlib.pyplot as plt  # Import module for plot and give alias plt

# Create a funtion that takes filename as argument and draw a graph
def task2(list):

    plot_list_year = []
    plot_list_mean = []
    plot_list_month = []

    # Ask for month
    showMonth = int(input(f"Ange vilken månad som ska presenteras:"))

    # list = read_file('kpi.csv')
    # Create a list to be plotted
    for i in range(1, len(list)):
        y, m = mean_list(list[i])
        plot_list_year.append(int(y))
        plot_list_mean.append(m)
        plot_list_month.append(month_list(showMonth, list[i]))

    # Create the plot diagram
    # Add curves
    plt.plot(
        plot_list_year,
        plot_list_month,
        color="red",
        label="Linje diagram för " + month_Name(showMonth),
    )
    plt.plot(
        plot_list_year,
        plot_list_mean,
        color="black",
        label="Linje diagram för medel kpi",
    )
    plt.bar(plot_list_year, plot_list_mean, color="lightblue", label="Kpi medel")

    #
    plt.title("Konsumentprisindex År 1980-2022")
    plt.xlabel("År")
    plt.ylabel("Konsumentprisindex")
    plt.legend()
    plt.grid()
    plt.xlim(plot_list_year[len(plot_list_year) - 1], plot_list_year[0] + 1)
    plt.ylim(100, 400)

    # Show curve
    plt.show()
    return


list = read_file("kpi-1.csv")
task2(list)


import matplotlib.pyplot as plt  # Import module for plot and give alias plt

# Convert list: string to float elements
def convertListToFloat(list):
    new_list = []
    for i in range(0, len(list)):
        new_list.append(float(list[i]))
    return new_list


# Create a function that plots a diagram
# Parameter is a value list of string elements during the year
#   list[0] contains year elements
#   list[1..N] contains data elements where first element in each row is type of "subject"
# Return: No return
def plotta_data(list, titel):

    # X-axel is year
    plot_list_year = []
    for i in range(1, len(list[0])):
        plot_list_year.append(int(list[0][i]))

    plt.figure(figsize=(16, 8))

    for i in range(1, len(list)):
        # Add curve
        plt.plot(plot_list_year, convertListToFloat(list[i][1:]), label=list[i][0])

    # Set some plot info
    plt.title(titel)
    plt.xlabel("År")
    plt.ylabel("Prisutveckling")
    plt.legend(loc="upper left")
    plt.grid()
    plt.xlim(1978, 2022)
    # plt.ylim(90, 920)
    plt.legend(fontsize=8)

    # Show curve
    plt.show()

    return


list = read_file("tjänster-1.csv")
plotta_data(
    list, "Prisutveckling för olika kategorier av varor och tjänster År 1980-2021"
)

list = read_file("livsmedel-1.csv")
plotta_data(list, "Prisutveckling för olika livsmedel År 1980-2021")


# Function that takes a list and returns a string text and a float of price change between year one and last year
# list: first index is product name and rest is yearly cost elements.
#
def price_change(list):
    # Define price change using first year (1980: index 1) and last year(2021: index -1 - last element)
    value = (float(list[-1]) - float(list[1])) / float(list[1])
    return list[0], value * 100.0


# Function that that prints the item and its price change as formated text
# list: The given list with
def price_development_tabel(list, text):
    print("+-------------------------------------------------------------------------+")
    print("|{:41s}|{:s}".format(text, "Prisutvecklingen i procentform"))
    print("+=========================================+===============================+")
    for i in range(1, len(list)):
        item, rate = price_change(list[i])
        print(
            "+-----------------------------------------+-------------------------------+"
        )
        print("|{:41s}|{:.2f}".format(item, rate))
    print("+------------------------------------------------------------------------+")
    return


# Function that that prints the item and its price change in a bar graph
#
def price_development_bar(list_1, list_2):

    plt.figure(figsize=(16, 12))

    for i in range(1, len(list_1)):
        item, rate = price_change(list_1[i])
        plt.barh(item, rate, color="blue")

    for i in range(1, len(list_2)):
        item, rate = price_change(list_2[i])
        plt.barh(item, rate, color="darkblue")

    fsize = 10  # Font size
    plt.title(
        "Prisutveckling för olika kategorier av varor och tjänster samt för olika typer av livsmedel År 1980-2021 i procentform",
        fontsize=fsize,
    )
    plt.xlabel("Prisutvecklingen i procentform", fontsize=fsize)
    plt.ylabel(
        "Olika kategorier av varor och tjänster samt för olika typer av livsmedel",
        fontsize=fsize,
    )
    plt.xlim(0, 810)

    # Show curve
    plt.show()

    return


# Plot table
list = read_file("tjänster-1.csv")
price_development_tabel(list, "Kategorier av varor och tjänster")

list = read_file("livsmedel-1.csv")
price_development_tabel(list, "Kategorier olika typer av livsmedel")

# Plot bar
print("\n\n")
list1 = read_file("tjänster-1.csv")
list2 = read_file("livsmedel-1.csv")
price_development_bar(list1, list2)


# Inparameter: List: Dec previous year if exist, Months elements
# Return Max KPI change (float), which month (str), mean KPI value for all months (float)
def checkMaxKpiYear(oldDec, list):
    # KPI change defined as (KPI_month+1 - KPI_month)/KPI_month
    maxtal = False
    month = 0
    yearKPI = 0.0

    #                   KPImonth - KPImonth-1
    # KPIchg(month) = ------------------------
    #                         KPImonth-1
    #

    for i in range(1, len(list)):
        # If month is January it needs to be compared with Dec previous year (if value exist).
        if i == 0:  # Jan is first element in list
            if (oldDec != "") and (
                list[i] != 0.0
            ):  # Check that it is not divided by zero
                value = (float(list[i]) - float(oldDec)) / float(oldDec)
        else:
            # All other months. Check that it is not divided by zero
            if list[i] != 0.0:
                value = (float(list[i]) - float(list[i - 1])) / float(list[i - 1])

        if maxtal is False or abs(value) > maxtal:
            maxtal = value
            month = i  # First list element is 0 (Jan) so increase by one

        yearKPI += float(list[i])

    return maxtal, month, (yearKPI / float(len(list)))


# Prints a table with KPI info between year 2000 and 2022
# Inparameter: List: Year (first element) and rest are months elements
# Return None
def printKpiTable(list):

    table_list = []
    row = 0
    max_change = 0
    max_change_row = 0

    for year in range(1, len(list) - 1):
        # Select the years to be used for the calculation

        if (int(list[year][0]) >= 2000) and (int(list[year][0]) <= 2022):
            # Get Dec month from previous year for doing the check. First check Dec is not before 2000.

            if int(list[year][0]) > 2000:
                oldDec = list[year + 1][-1]  # Dec is last element in yearly list
            else:
                # Use empty string to indicate no info exist from Dec previous year
                oldDec = ""

            # Get the parameters
            maxKpi, month, yearMean = checkMaxKpiYear(oldDec, list[year][1:])

            table_list.append([])
            table_list[row].append(int(list[year][0]))
            table_list[row].append((maxKpi * 100.0))
            table_list[row].append(month)
            table_list[row].append(yearMean)
            row += 1
            # Keept track of the largest KPI change
            if maxKpi > max_change:
                max_change = maxKpi
                max_change_row = row

    print("=" * 74, "\n")
    print(f'{"ANALYS AV KPI UNDER ÅREN 2000 - 2022":^74}')
    print(f'{"------------------------------------":^74}', "\n")
    print(f'{" ":<22}{"Största förändring"}')
    print(f'{" ":<22}{"------------------"}')
    print(f'{"År":<22}{"%":<13}{"månad":<23}{"Årsmedelvärde":<16}')
    print("-" * 74)

    for i in range(len(table_list) - 1, -1, -1):
        print(
            f"{table_list[i][0]:<22}{table_list[i][1]:<13.2f}{month_Name_Short(table_list[i][2]):<23}{table_list[i][3]:<10.2f}"
        )

    print()
    print(
        f'{"Största förändringen:":<22}{table_list[max_change_row][1]:<13.2f}{month_Name_Short(table_list[max_change_row][2]):<4}{table_list[max_change_row][0]:<10}'
    )
    print("=" * 74, "\n")

    # Plot the result
    plt.figure(figsize=(10, 6))
    # Show the values per month
    y_list = []
    for i in range(len(table_list) - 1, -1, -1):
        plt.scatter(table_list[i][2], table_list[i][0], color="blue")
        y_list.append(table_list[i][0])

    plt.title("Största förändringav KPI för en enskild månad under åren 2000-2022")
    plt.xlabel("Månad")
    plt.ylabel("År")
    plt.xlim(1, 13)
    plt.ylim(1999, 2023)
    plt.tight_layout
    plt.yticks(y_list)

    plt.grid(True, which="both", axis="both")
    # Show curve
    plt.show()

    return


list = read_file("kpi-1.csv")
year = list[3][0]

printKpiTable(list)


##### Three files to be used. Set default value
# list = read_file('kpi.csv')
# list1 = read_file('tjänster.csv')
# list2 = read_file('livsmedel.csv')

file_kpi = "kpi.csv"
file_tjanster = "tjänster.csv"
file_livsmedel = "livsmedel.csv"

# Read files - use default name or get a new name per csv file
def task1():
    global file_kpi
    global file_tjanster
    global file_livsmedel

    message = "namn för kpi.csv (annars används ", file_kpi, "): "
    filename = input(message)
    if filename != "":  # Default file will NOT be used
        file_kpi = filename

    message = "namn för tjänster.csv (annars används ", file_tjanster, "): "
    filename = input(message)
    if filename != "":  # Default file will NOT be used
        file_tjanster = filename

    message = "namn för livsmedel.csv (annars används ", file_livsmedel, "): "
    filename = input(message)
    if filename != "":  # Default file will NOT be used
        file_livsmedel = filename

    print("\nCSV fil för kpi:", file_kpi)
    list = read_file(file_kpi)
    for line in range(2):
        print(list[line])

    print("\nCSV fil för tjanster:", file_tjanster)
    list = read_file(file_tjanster)
    for line in range(2):
        print(list[line])

    print("\nCSV fil för livsmedel:", file_livsmedel)
    list = read_file(file_livsmedel)
    for line in range(2):
        print(list[line])

    return


# Read csv file and the use defined function
def task3():
    list = read_file(file_tjanster)
    plotta_data(
        list, "Prisutveckling för olika kategorier av varor och tjänster År 1980-2021"
    )

    list = read_file(file_livsmedel)
    plotta_data(list, "Prisutveckling för olika livsmedel År 1980-2021")

    return


# Read csv file and the use defined function
def task4():
    # Plot tabel
    list_tj = read_file(file_tjanster)
    price_development_tabel(list_tj, "Kategorier av varor och tjänster")

    list_livs = read_file(file_livsmedel)
    price_development_tabel(list_livs, "Kategorier olika typer av livsmedel")

    # Plot bar
    price_development_bar(list_tj, list_livs)

    return


#
# MAIN program that will run until selection to end
#
# Menu with 6 selections. Last one will end the program
print("Program för att läsa in och analysera resultatet i uppgift 1 – 5")
print()
print("1. Läser in csv-filerna")
print("2. Konsumentprisindex under åren 1980 – 2022")
print(
    "3. Prisutvecklingen för de olika kategorierna i filerna ”Varor och \ntjänster” samt ”Livsmedel” under åren 1980 – 2021"
)
print(
    "4. Prisutvecklingen i procentform för de olika kategorierna i filerna \n”Varor och tjänster” samt ”Livsmedel” under åren 1980 – 2021"
)
print("5. Förändringar i KPI under åren 2000 – 2022")
print("6. Avsluta programmet")
print()


menu = 0
# Continue to ask until choice 6 for termination
while menu != 6:
    # Ask for month
    menu = input(f"Välj menyalternativ (1–6):")

    if menu == "1":
        task1()

    elif menu == "2":
        print("2. Konsumentprisindex under åren 1980 – 2022")
        list = read_file(file_kpi)
        task2(list)

    elif menu == "3":
        print(
            "3. Prisutvecklingen för de olika kategorierna i filerna ”Varor och \ntjänster” samt ”Livsmedel” under åren 1980 – 2021"
        )
        task3()

    elif menu == "4":
        print(
            "4. Prisutvecklingen i procentform för de olika kategorierna i filerna \n”Varor och tjänster” samt ”Livsmedel” under åren 1980 – 2021"
        )
        task4()

    elif menu == "5":
        print("5. Förändringar i KPI under åren 2000 – 2022")
        list = read_file(file_kpi)
        printKpiTable(list)

    elif menu == "6":
        break
    else:
        # Just to be safe
        continue

print("\n\n======================")
print("Programmet är avslutat")
print("======================")
