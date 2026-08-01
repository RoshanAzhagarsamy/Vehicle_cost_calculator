from calculator import calculate_trip_cost

print("================================")
print(" VEHICLE COST CALCULATOR")
print("================================")

trip_distance = float(input("Enter Distance (KM): "))
vehicle_mileage = float(input("Enter Mileage (KM/L): "))
diesel_price = float(input("Enter Diesel Price (₹): "))

if trip_distance <= 0:
    print("❌ Distance must be greater than 0")

elif vehicle_mileage <= 0:
    print("❌ Mileage must be greater than 0")

elif diesel_price <= 0:
    print("❌ Diesel Price must be greater than 0")

else:
    diesel_used, diesel_cost = calculate_trip_cost(
        trip_distance,
        vehicle_mileage,
        diesel_price
    )

    print()
    print("========== RESULTS ==========")
    print("Distance     :", trip_distance, "KM")
    print("Mileage      :", vehicle_mileage, "KM/L")
    print("Diesel Price : ₹", diesel_price)
    print("Diesel Used  :", round(diesel_used, 2), "Litres")
    print("Diesel Cost  : ₹", round(diesel_cost, 2))