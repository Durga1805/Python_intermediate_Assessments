item= input("[car/Bike/suv] : ")
hrs=float(input("Duration : "))
vehicle=["car","bike","suv"]
if item.lower() not in vehicle:
  print("invalid Vehicle Type")
elif hrs<0:
  print("Invalid parking duration")
else:
  if item.lower() == "car":
    rate=50
    add_rate=20
  elif item.lower() =="bike":
    rate=30
    add_rate=10
  else:
    rate=70
    add_rate=30
if hrs<1:
  hrs=1
if hrs<=2:
  fee =rate
else:
  add_hrs=hrs-2
  fee=rate+(add_hrs*add_rate)

print("="*30)
print("Vehicle : ",item)
print("Hourse : ",hrs)
print(f"Parking Fee : {int(fee)}/-")