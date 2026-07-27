print("Hello Roshan")
company = "Aachi"
vehicle = "TN02BV2890"
driver = "Roshan"
source = "Chennai"
destination = "Madurai"
distance = 450
mileage = 7
diesel_price = 100
print("Company    :", company)
print("Vehicle    :", vehicle)
print("Driver     :", driver)
print("Source     :", source)
print("Destination:", destination)
print("Distance   :", distance)
print("Mileage    :", mileage)
print("Diesel Price:", diesel_price)

print(type(company))
print(type(distance))
print(type(diesel_price))

trip_no = 125
vehicle_weight = 8.75
trip_completed = True

trip_details = trip_no * vehicle_weight
print("Trip Details:", trip_details)

diesel_used = distance / mileage
diesel_cost = diesel_used * diesel_price
print("Distance:", distance)
print("Mileage:", mileage)
print("Diesel Price:", diesel_price)
print("Diesel Used:", diesel_used)
print("Diesel Cost:", diesel_cost)
print("================================")
print("VEHICLE COST CALCULATION")
print("================================")

print("Distance:", distance, "km")
print("Mileage:", mileage, "km/l")
print("Diesel Price:", round(diesel_price, 2), "per litre")
print("Diesel Used:", round(diesel_used, 2), "litres")
print("Diesel Cost:", round(diesel_cost, 2), "INR")
