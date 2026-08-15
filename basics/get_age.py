from datetime import datetime

print("\nIngresa tu fecha de nacimiento\n")

my_year = int(input("Año: "))
my_month = int(input("Mes: "))
my_day = int(input("Día: "))

current_year = datetime.today().year
current_month = datetime.today().month

if (current_month > my_month):
    current_age = current_year - my_year
    months = current_month - my_month
else:
    current_age = (current_year - my_year) - 1
    months = current_month

print("\nTu edad actual es de:", current_age, "años con", months, "meses", "\n")
