print("Restaurant Tip Calculator")

bill = float(input("Enter bill amount: $"))
tip_percent = float(input("Enter tip percentage: "))

tip = bill * tip_percent / 100
total = bill + tip

print(f"Tip amount: ${tip:.2f}")
print(f"Total bill: ${total:.2f}")
