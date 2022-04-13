units = int(input("Enter number of units (KWh) consumed : "))
unitRate = float(input("Enter rate of 1 unit : "))

totalBill = int(units * unitRate)
print("You will be billed INR", totalBill)