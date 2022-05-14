import csv
import os
# cwd = os.getcwd()  # Get the current working directory (cwd)
# print("This is my directory" + cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("These are the files ",files)
# print("Files in %r: %s" % (cwd, files))

# with open("csv_files/2016_pilbara.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line)

population = []

with open("csv_files/2016_pilbara.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file) # create a reader or writer object
    for row in reader: #for each row create an empty list
        #seperates elements based on the delimiter that has been given
        # population.append(line)

# print(population)

# for age_group in population: #age_group = ['0-4 years', '4711']
#     print(f"{age_group[0]} {age_group[1]}")

# writing a csv file 
# with open("population.csv", mode="w", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")

#     for age_group in population: #age_group -> ['0-4 years', '4711']
#         csv_writer.writerow([age_group[1], age_group[0]]) #4711, 0-4 years