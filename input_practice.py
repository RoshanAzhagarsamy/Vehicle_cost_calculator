name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to the program.")
driver = input("Enter the driver's name: ")
source = input("Enter the source Location: ")
destination = input("Enter the destination Location: ")

distance = input("Enter the distance :")
mileage = input("Enter the mileage :")

diesel_used = distance / mileage
print("Diesel Used:", round(diesel_used, 2), "litres")
