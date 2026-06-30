device_status = "active"
temp = int(input("Enter the today temperature:"))

if device_status == "active":
    if temp > 35:
        print("High Temperature alert")
    else:
        print("Normal temperature")
else:
    print("Device is offline")
