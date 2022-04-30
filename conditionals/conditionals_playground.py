#Data Types - Strings, Integer, Floats, Boolean
b1 = True
b2 = False
# print(type(b1))

knows_password = True
knows_username = False
login = knows_password and knows_username
# print(type(login))
# print(login)
# print(not knows_password)

#Boolean Operators - NOT, AND, OR 
recover = knows_password or knows_username

is_raining = True
is_cold = True
# print(is_raining) #True
# print(not is_raining) #False
# print(is_raining or is_cold) #True
# print(is_raining and not is_cold) #False
# print(is_raining or not is_cold) #True
# print(not is_raining and not is_cold) #False
# print(not(is_raining and is_cold)) #False

# Comparison Operators
# == Equal
# != Not Equal
# > Greater than
# < Less than
# >= Greater than or equal
# <= Less than or equal
# print(10 > 5)
# print(1 > 1.5)
# print(5.9 != 5.8)
# print("Asli" == "Georgie")
# print("Asli" < "asli")
# print(type(3) == type(3.0)) 

# temperature = 16
# print(temperature < 18)
# wind_chill = 3
# print(wind_chill > 4)
# print(temperature - wind_chill < 16)

# print("hayley" == name)

# name = "Camila"

# if name == "Asli":
#     print("Hello again")
# elif name == "Camila":
#     print(f"Hello {name}, what are we doing today?")
# else:
#     print("WOW HELLO I MISSED YOU!")

is_raining = True
temperature = 16
wind_chill = 3

if temperature - wind_chill < 16 and not is_raining:
    print("Just stay home.")
else:
    if is_raining:
        print("You'll need an umbrella today")
    if temperature - wind_chill < 16:
        print("You'll need a jumper today")

# if is_raining:
#     print("Take an umbrella!")
# else:
#     print("Do not take an umbrella")

# if temperature - wind_chill < 16:
#     print("Take a jumper")
# elif temperature - wind_chill > 30:
#     print("Euck, it's hot today, stay home")
# else:
#     print("Wow, what a lovely day!")











# print(type(is_raining))
# type(is_cold)
# print(not is_raining)
# print(is_raining and is_cold)
# print(is_raining and not is_cold)





