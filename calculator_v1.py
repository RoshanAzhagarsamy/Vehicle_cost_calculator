print("================================")
print("VEHICLE COST CALCULATION")
print("================================")

distance = int(input("Enter the distance (in km): "))
mileage = int(input("Enter the mileage (in km/l): "))
diesel_price = float(input("Enter the diesel price (per litre):" ))

diesel_used = distance / mileage
diesel_cost = diesel_used * diesel_price

print()
print("=======RESULTS========")
      
print("Distance:", distance, "km")
print("Mileage:", mileage, "km/l")
print("Diesel Price:", round(diesel_price, 2), "INR")
print("Diesel Used:", round(diesel_used, 2), "litres")
print("Diesel Cost:", round(diesel_cost, 2), "INR")