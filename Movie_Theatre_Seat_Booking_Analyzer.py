n = int(input("Enter number of shows: "))

total_booked = 0
total_available = 0
count = 0
max_occupancy = -1
max_show = ""

for i in range(n):

    name =input("Enter the Show Name: ")
    total=int(input("Total Seats: "))
    booked=int(input("Booked Seats: "))
    available = total - booked
    occupancy = (booked / total) * 100

    if occupancy >= 80:
        category = "House Full"
    elif occupancy >= 60:
        category = "High Demand"
    elif occupancy >= 40:
        category = "Moderate"
    else:
        category = "Low Demand"
    print(f"{name} -Available: {available} - Occupancy: {occupancy:.2f} % - {category}")
    

    total_booked = total_booked + booked
    total_available = total_available + available

    if category == "High Demand" or category == "House Full":
        count = count + 1

    if occupancy > max_occupancy:
        max_occupancy = occupancy
        max_show = name
print()
print(f"Highest Occupancy:{max_show}")
print(f"Total Booked Seats: {total_booked}")
print(f"Total Available Seats:{total_available}")
print(f"High Demand/House Full Shows:{count}")
