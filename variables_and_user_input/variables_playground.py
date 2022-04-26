from dis import dis


weather = "rainy"


# print("rainy")
# print(weather)

# Data Types - String is a text data
# Integer numerical data (whole number) 
# Float numerical (with decimals)
height = 155
weight = 55.8
# print(type(name))
# print(type(height))
# print(type(weight))

day = "Saturday"
# print(type(day))
message = f"Today is {day}!"
message2 = "Today is " + day
# print(message2)

#Integers 
#Run distance in m
run1_dist = 1400
run2_dist = 1800

#Addition
total_dist = run1_dist + run2_dist
# print(total_dist)

#Floats 
#Run distance in km
run3_dist = 1.7
run4_dist = 6.35
# print(total_dist)
#Addition2
total_dist = run3_dist + run4_dist
# print(total_dist)

#Division and Multiplication
# print(run1_dist / 1000)
# print(run3_dist * 1000)

#Divison is always produce floats
#Other calculations depends on the data type 
#As long as there is one float, float 

# Different Scenarios
name = "Asli"
# print(name + run2_dist)
# print(name * run2_dist)

#Typecast to change the data type
print(name * int(run4_dist))
# print(name / run1_dist)


