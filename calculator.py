def calculate_trip_cost(distance, mileage, diesel_price):
    diesel_used = distance/mileage
    diesel_cost = diesel_used * diesel_price
    return(diesel_used, diesel_cost)

distance = int(input("Enter the distance (in km): "))
mileage = int(input("Enter the mileage (in km/l): "))
diesel_price = float(input("Enter the diesel price (per litre): "))

diesel_used, diesel_cost = calculate_trip_cost(
    distance,
    mileage, 
    diesel_price
)

print()
print("=======RESULTS========")
print("Diesel Used:", round(diesel_used, 2), "litres")
print("Diesel Cost:", round(diesel_cost, 2), "INR")