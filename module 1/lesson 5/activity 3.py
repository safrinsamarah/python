emergency = False
traffic_level = int(input("cars waiting (0 - 100): "))

if emergency:
    print("EMERGENCY MODE ALL RED LIGHTS ON>")
elif traffic_level > 80:
    print("YELLOW LIGHT: ON")
elif traffic_level > 30:
    print("GREEN LIGHTS: ON")
elif traffic_level > 10:
    print("RED LIGHT : ON")
else:
    print("INVALID INPUT")