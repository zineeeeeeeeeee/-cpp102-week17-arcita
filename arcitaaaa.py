gh auth login
# CPP102 Week 17
# Simulated Device Monitoring and Alert System

def starting_temps():
    return [28, 31, 35, 37, 29]


def show_menu():
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def check_number(num):
    if num == "":
        return False

    if num[0] == "-":
        num = num[1:]

    return num.isdigit() and num != ""


def view_temps(temps):
    print("\nCURRENT READINGS")
    print("----------------")

    for i in range(len(temps)):
        print(f"Reading {i + 1}: {temps[i]} °C")


def add_temp(temps, min_temp, max_temp):
    new_temp = input("Enter new reading: ")

    if new_temp == "":
        print("\nInvalid input. The reading cannot be empty.")

    elif not check_number(new_temp):
        print("\nInvalid input. Enter a whole number only.")

    else:
        value = int(new_temp)

        if value < min_temp or value > max_temp:
            print(f"\nInvalid reading. Enter a value from {min_temp} to {max_temp}.")
        else:
            temps.append(value)
            print("\nReading added successfully.")


def check_level(temp, warn, danger):
    if temp < warn:
        return "NORMAL"
    elif temp <= danger:
        return "WARNING"
    else:
        return "CRITICAL"


def show_levels(temps, warn, danger):
    print("\nREADING CLASSIFICATION")
    print("----------------------")

    for temp in temps:
        level = check_level(temp, warn, danger)
        print(f"{temp} °C -> {level}")


def get_total(temps):
    total = 0

    for temp in temps:
        total += temp

    return total


def get_average(temps):
    total = get_total(temps)
    average = total / len(temps)
    return average


def get_lowest(temps):
    lowest = temps[0]

    for temp in temps:
        if temp < lowest:
            lowest = temp

    return lowest


def get_highest(temps):
    highest = temps[0]

    for temp in temps:
        if temp > highest:
            highest = temp

    return highest


def count_levels(temps, warn, danger, level):
    count = 0

    for temp in temps:
        if check_level(temp, warn, danger) == level:
            count += 1

    return count


def get_percent(count, total):
    return (count / total) * 100


def check_status(warnings, criticals):
    if criticals > 0:
        return "ATTENTION REQUIRED"
    elif warnings > 0:
        return "MONITOR"
    else:
        return "NORMAL"


def show_summary(temps, warn, danger):
    total_readings = len(temps)

    normal = count_levels(temps, warn, danger, "NORMAL")
    warning = count_levels(temps, warn, danger, "WARNING")
    critical = count_levels(temps, warn, danger, "CRITICAL")

    avg = get_average(temps)
    lowest = get_lowest(temps)
    highest = get_highest(temps)
    total = get_total(temps)

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {total_readings}")
    print(f"Total of readings   : {total}")
    print(f"Average temperature : {avg:.2f} °C")
    print(f"Minimum temperature : {lowest} °C")
    print(f"Maximum temperature : {highest} °C")

    print()
    print(f"NORMAL   : {normal} ({get_percent(normal, total_readings):.2f}%)")
    print(f"WARNING  : {warning} ({get_percent(warning, total_readings):.2f}%)")
    print(f"CRITICAL : {critical} ({get_percent(critical, total_readings):.2f}%)")

    print()
    print("Overall Status:", check_status(warning, critical))


def main():
    min_temp = 0
    max_temp = 100
    warn = 30
    danger = 35

    temps = starting_temps()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            view_temps(temps)

        elif choice == "2":
            print()
            add_temp(temps, min_temp, max_temp)

        elif choice == "3":
            show_levels(temps, warn, danger)

        elif choice == "4":
            show_summary(temps, warn, danger)

        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


main()