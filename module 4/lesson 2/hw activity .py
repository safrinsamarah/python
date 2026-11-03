#Step 1 create a restaurent menu
destination1 = ("Paris", "France", "48°51′24″N 2°21′08″E (48.8566° N, 2.3522° E)")
destination2 = ("Tokyo", "Japan", "35°41′22″N 139°41′30″E (35.6895° N, 139.6917° E)")
destination3 = ("Rio de Janeiro","Brazil", "22°54′40″S 43°12′20″W (-22.9111° S, -43.2056° W)")
destination4= ("Barcelona","Spain", "41°22′58″N 2°10′37″E (41.3828° N, 2.1774° E)")
destination5= ("Cape Town","South Africa", "33°55′31″S 18°25′26″E (-33.9258° S, 18.4232° E)")

Trips_for_tourism = (destination1, destination2, destination3,destination4,destination5)

print("Trips for tourism: ", Trips_for_tourism )

destination1, destination2, destination3, destination4, destination5 = Trips_for_tourism
print("destination1: ", destination1)
print("destination2: ", destination2)
print("destination3: ", destination3)
print("destination4: ", destination4)
print("destination: ", destination5)

print("First destination: ", Trips_for_tourism[2])
print("First destination name: ", Trips_for_tourism[0][0])

print("First two item: ", Trips_for_tourism[:2])

print("Count:", Trips_for_tourism.count(Trips_for_tourism[0]))
print("Index:", Trips_for_tourism.index(Trips_for_tourism[2]))

new_places = (
    ("Sydney", "Australia", -33.86, 151.20),
    ("Rome", "Italy", 41.90, 12.49)
)

all_destinations = Trips_for_tourism + new_places

print("All Destinations:")
for place in all_destinations:
    print(place)