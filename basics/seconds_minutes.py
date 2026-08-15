print("\nSegundos a minutos\n")

seconds = int(input("Número de segundos: "))

minutes = seconds // 60 
remain_seconds = seconds % 60 

print(seconds, "son", minutes, "minutos")
print("con", remain_seconds, "segundos\n")