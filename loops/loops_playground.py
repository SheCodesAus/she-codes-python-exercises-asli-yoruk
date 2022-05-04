# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# for digit in range(6): #0,1,2,3,4,5
#     #digit =0, #digit = 1
#     print(digit)


numbers = [10,20,30,40]
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# for number in numbers:
#     print(number)

# for num in range(10):
#     print(num)

# for num in range(1,11):
#     print(num)

# for num in range(0,13,2):
#     print(num)

# chilli_wishlist = ["igloo", "chicken", "donut toy", "carboard box"]
# for item in range(len(chilli_wishlist)): # range(4)
#     print(chilli_wishlist[item]) #chilli_wishlist[2]
# for item in chilli_wishlist: 
#     print(item)

chilli_wishlist = [
    ["igloo"],
    ["donut toy", "tennis ball", "croc toy"],
    ["chicken", "peanut butter"],
    ["cardboard box", "kong", "dig mat"]
]

# for category in chilli_wishlist:
#     # ['igloo']
#     # ['donut toy', 'tennis ball', 'croc toy'] 
#     for item in category:
#         print(item)

#While Loop
num = 1
# while num > 0:
#     print("Hi")
#     num = 0

# guess = ""
# while guess != "a":
#     guess = input("Guess a letter: ")

counter = 10
# while counter <= 10:
#     print(counter)
#     counter = counter + 1
    
# Exercise Question Sample Answer
number = int(input("Enter a number: "))

for i in range(1, number+1):
    print(f"{number} * {i} = {number * i}")