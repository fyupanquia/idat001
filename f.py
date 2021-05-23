s1 = float(input("Enter speed car 1 (km/h): "))
s2 = float(input("Enter speed car 2 (km/h): "))
distance = float(input("Enter the distance between both (km) : "))

behind_vehicle = max(s1, s2)
front_vehicle = min(s1,s2)


if s1==s2:
    print("Impossible, the cars won't meet never")
else:
    time_hours = distance/(behind_vehicle-front_vehicle)
    time_minutes = time_hours*60

    print("")
    print("*"*10)
    print(f" vehicle({behind_vehicle}km/h) ----------- {distance} ----------------- vehicle({front_vehicle}km/h)")
    print("")
    print(f"Meet time: {time_minutes} minutes")