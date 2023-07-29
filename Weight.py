# Ask for user's name
name = input("Please enter your name: ")

# Ask for user's weight in kilograms
weight_kg = float(input("Please enter your weight in kilograms: "))

# Convert weight to pounds (1 kg is approximately 2.20462 pounds)
weight_lb = weight_kg * 2.20462

# Output user's name and weight in pounds
print(name + ", your weight in pounds is approximately: " + str(round(weight_lb, 2)) + " lbs.")
