my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_height_cm = my_height * 2.54
my_weight = 180 # lbs
my_weight_kg = my_weight * 0.45359237
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height_cm} cm tall.")
print(f"He's {my_weight_kg} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right 
total = my_age + my_height_cm + my_weight_kg
print(f"If I add {my_age}, {my_height_cm}, and {my_weight_kg} I get {total}.")
