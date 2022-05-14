# input_number = input("Enter a number, press enter when done: ")
# completed_list = []
# print(input_number)
# print(completed_list) 

# while input_number != "":
#     completed_list.append(int(input_number))
#     input_number = input("Enter a number: ")
    
# print(completed_list) 
# print(sum(completed_list))

# FOR LOOP EXERCISE Q3
total = 0
random_numbers = [3, 5, 9, 1]
counter = 0
# random_numbers[0] # 3
# while counter < len(random_numbers):
#     print(counter)
#     print(random_numbers[counter])
 
#     counter += 1 #adding 1


# a = random_numbers.pop()
# while random_numbers != []:
#     # number_to_add = random_numbers.pop()
#     # total += number_to_add
#     total += random_numbers.pop()

# print(total)




    
    # random_numbers

# for num in random_numbers:
#     total += num
    
# print(total)
# i= 20
# num=int(input("enter a number:"))

# while num!=i:
#     # num=int(input("enter a number: "))  

#     if num<i:
#         print("Too low!")
#         # num=int(input("enter a number: "))
#     elif num>i:
#         print("Too high!")
#     num=int(input("enter a number: "))  
# print("correct!")
    

list_words = ['red', 'green', 'blue', 'yellow']
red_total = 0
green_total = 0
blue_total = 0
yellow_total = 0
import csv 
with open("csv_files\colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    # next(reader)
    for line in reader:
        # print(line[4])
        if list_words[0] in line[4].lower(): #to make all the data lowercase as the list is lower case
            red_total += 1
        if list_words[1] in line[4].lower():
            green_total += 1
        if list_words[2] in line[4].lower():
            blue_total += 1
        if list_words[3] in line[4].lower():
            yellow_total += 1
                
#             elif item == list_words[1]:
#                 Green_Total = A + int(list_words[1])
#                 print(f'Green: {Green_Total}')
#             elif item == list_words[2]:
#                 Blue_Total = A + int(list_words[2])
#                 print(f'Blue: {Blue_Total}')
#             elif item == list_words[3]:
#                 Yellow_Total = A + int(list_words[3])
#                 print(f'Yellow: {Yellow_Total}')
# print(A)
# print(f'Red: {red_total}')
# print(f'Green: {green_total}')
# print(f'Blue: {blue_total}')
# print(f'Yellow: {yellow_total}')




# Find the minimum value
numbers = [4,7,10,1,2]
min_value = numbers[0]
min_location = 0
index = 0

for num in numbers:
    if num < min_value:
        min_value = num
        min_location = index
    index += 1

# print(min_value, min_location)

print("Q1 Write a function that takes a temperature in fahrenheit and returns the temperature in celsius")
def temp_celsius(temp_far):
    temp_c = (temp_far - 32) * 5 / 9
    return temp_c
print(temp_celsius(0))  
print(temp_celsius(32))
print(temp_celsius(350))  