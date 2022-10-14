# To run the program
# Open terminal in the directory containing this file
# Run the following command
# >> python josephus.py
# Give input for number of people and skip number
# In all cases this game will run till one person survives

# taking input for the number of people
numPeople = int(input('Enter the number of people: '))

# throwing error if number of people is invalid
if(numPeople < 1):
    print('Error: Value of n should be greater than 0')
    exit()

# taking input for the skip number
skipNum = int(input('Enter the value of skip number: '))

# throwing error if skip number is invalid
if(skipNum < 0):
    print('Error: Value of n should be greater than 0')
    exit()

# storing all the people in a list
listOfPeople = [*range(1, numPeople+1, 1)]

# print(listOfPeople)

# initialising the index at the first person
index = 0
while(len(listOfPeople) != 1):
    # finding the index of person who is to be killed
    x = (index+skipNum) % len(listOfPeople)
    print(listOfPeople[index % len(listOfPeople)],
          " killed ", listOfPeople[x])  # printing who killed whom
    index = x  # updating my index to the person to the right of the person killed
    # deleting the person who was killed from the list of people
    del listOfPeople[x]


print(listOfPeople[0], " survived")  # printing the survivor at the end
