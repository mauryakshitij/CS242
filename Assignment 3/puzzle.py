# To run the program
# Open terminal in the directory containing this file
# Run the following command
# >> python puzzle.py
# use 0 as blank space in input
# Enter the input for initial and final grid in a single line , eg 1 2 3 4 5 6 7 8 0

# initialising a reference grid to be used in future
referenceGrid = [1, 2, 3,
                 4, 5, 6,
                 7, 8, 0]
# initialising empty initial and final state grids
initialGrid = []
finalGrid = []

# taking input for the initial grid
initialGrid = [int(item)
               for item in input("Enter the Initial Grid : ").split()]

# throwing error in case the no of elements is not 9 in the initial grid
if(len(initialGrid) != 9):
    print("Error: initial grid should have 9 elements")
    exit()

# taking input for the final grid
finalGrid = [int(item) for item in input("Enter the Final Grid   : ").split()]

# throwing error in case the no of elements is not 9 in the final grid
if(len(finalGrid) != 9):
    print("Error: final grid should have 9 elements")
    exit()

# initialising a empty list which will store the moves made by the algorithm
steps = []
# initialising a emplty list which will store the moves made to make the bottom right element of final grid 0
fixFinal = []


# defining a function to append steps in the list of steps
def appendStep():
    if(len(steps) == 0):
        steps.append(initialGrid.copy())
        # printing all steps and exiting program if the program reached the final grid
        if(steps[-1] == finalGrid):
            for i in range(len(steps)):
                show(steps[i])
            for i in range(len(fixFinal)):
                show(fixFinal[i])
            print('Number of steps: ',len(steps)+len(fixFinal)-1)
            exit()
    elif(initialGrid != steps[-1]):
        steps.append(initialGrid.copy())
        # printing all steps and exiting program if the program reached the final grid
        if(steps[-1] == finalGrid):
            for i in range(len(steps)):
                show(steps[i])
            for i in range(len(fixFinal)):
                show(fixFinal[i])
            print('Number of steps: ',len(steps)+len(fixFinal)-1)
            exit()

# defining a function to append steps of fixing the final grid so that 0 is at bottom right
def appendFinal():
    fixFinal.append(finalGrid.copy())

# defining a function to print the grid in a structure
def show(a):
    print()
    for i in range(9):
        print(a[i], end=" ")
        if(i % 3 == 2):
            print()
    print("\n--------------------------------------------------------")


# defining a function that shifts 0 to the bottom right of grid if it is not in the center initially
def shift0(a):
    list = [8, 7, 6, 3, 0, 1, 2, 5]

    #find the position of 0 in the list
    index0 = a.index(0)
    index0 = list.index(index0)
    
    #run a loop until 0 reaches the bottom right
    for i in range(len(list)-1):
        a[list[(i+index0) % len(list)]], a[list[(i+1+index0) % len(list)]
                                           ] = a[list[(i+1+index0) % len(list)]], a[list[(i+index0) % len(list)]]
        if a == initialGrid:
            appendStep()
        else:
            appendFinal()
        if(a[8] == 0):
            break


# defining a function that shifts 0 to the bottom right of grid if it is in the center initially
def shiftCenter0(a):
    #shift 0 to right
    a[5], a[4] = a[4], a[5]
    if a == initialGrid:
        appendStep()
    else:
        appendFinal()
    #shift 0 down
    a[8], a[5] = a[5], a[8]
    if a == initialGrid:
        appendStep()
    else:
        appendFinal()


# defining a function that does 1 cyclic rotation in the outer most 3*3 square
def switch1(a):
    list = [8, 5, 2, 1, 0, 3, 6, 7, 8]
    for i in range(len(list)-1):
        a[list[i]], a[list[i+1]] = a[list[i+1]], a[list[i]]
        appendStep()

# defining a function that does 1 cyclic rotation in the right 2*3 rectangke
def switch2(a):
    list = [8, 5, 2, 1, 4, 7, 8]
    for i in range(len(list)-1):
        a[list[i]], a[list[i+1]] = a[list[i+1]], a[list[i]]
        appendStep()


# defining a function that does 1 cyclic rotation in the bottom 3*2 rectangle
def switch3(a):
    list = [8, 5, 4, 3, 6, 7, 8]
    for i in range(len(list)-1):
        a[list[i]], a[list[i+1]] = a[list[i+1]], a[list[i]]
        appendStep()

# defining a function that does 1 cyclic rotation in the bottom right 2*2 square
def switch4(a):
    list = [8, 5, 4, 7, 8]
    for i in range(len(list)-1):
        a[list[i]], a[list[i+1]] = a[list[i+1]], a[list[i]]
        appendStep()


if(finalGrid[8] != 0):
    appendFinal()

# shifing 0 to bottom right of final grid if it is in the center
if(finalGrid[4] == 0):
    shiftCenter0(finalGrid)

# shifitng 0 to bottom right of final grid if it is not at bottom right or center
if(finalGrid[8] != 0):
    shift0(finalGrid)

fixFinal.reverse()

# initialising a dictionary which will store the mapped positions from reference to final grid
mappedPositions = {}

# mapping the final grid to reference grid
for i in range(9):
    mappedPositions[referenceGrid[i]] = finalGrid[i]

# Appending the initial grid to the steps list
appendStep()

# shifing 0 to bottom right if it is in the center
if(initialGrid[4] == mappedPositions[0]):
    shiftCenter0(initialGrid)


# shifitng 0 to bottom right if it is not at bottom right or center
if(initialGrid[8] != mappedPositions[0]):
    shift0(initialGrid)

# shifting 1 to its correct position
if(initialGrid[4] == mappedPositions[1]):
    switch4(initialGrid)
while(initialGrid[0] != mappedPositions[1]):
    switch1(initialGrid)

# shifting 2 to index 2
while(initialGrid[3] == mappedPositions[2] or initialGrid[6] == mappedPositions[2]):
    switch3(initialGrid)

while(initialGrid[2] != mappedPositions[2]):
    switch2(initialGrid)

# shifting 3 to 2nd column if it is in the 1st column
while(initialGrid[3] == mappedPositions[3] or initialGrid[6] == mappedPositions[3]):
    switch3(initialGrid)

# shifting 2 and 3 to their correct positions
if(initialGrid[1] != mappedPositions[3]):
    while(initialGrid[5] != mappedPositions[3]):
        switch4(initialGrid)
    while(initialGrid[2] != mappedPositions[3]):
        switch2(initialGrid)
else:
    switch2(initialGrid)
    switch4(initialGrid)
    while(initialGrid[2] != mappedPositions[2]):
        switch2(initialGrid)
    switch4(initialGrid)
    while(initialGrid[1] != mappedPositions[2]):
        switch2(initialGrid)


# shifting 4 to index 6
while(initialGrid[6] != mappedPositions[4]):
    switch3(initialGrid)

# shifting 4 and 7 to their correct positions
if(initialGrid[3] != mappedPositions[7]):
    while(initialGrid[7] != mappedPositions[7]):
        switch4(initialGrid)
    while(initialGrid[6] != mappedPositions[7]):
        switch3(initialGrid)
else:
    switch3(initialGrid)
    while(initialGrid[7] != mappedPositions[7]):
        switch4(initialGrid)
    while(initialGrid[3] != mappedPositions[7]):
        switch3(initialGrid)
    while(initialGrid[4] != mappedPositions[4]):
        switch4(initialGrid)
    while(initialGrid[3] != mappedPositions[4]):
        switch3(initialGrid)

# shifting 5 to the center
while(initialGrid[4] != mappedPositions[5]):
    switch4(initialGrid)

# throw error if the given configuration comes out to be not solvable else printing all the steps to the solution
if(initialGrid[5] != mappedPositions[6]):
    print("Not Solvable")
else:
    for i in range(len(steps)):
        show(steps[i])
    for i in range(len(fixFinal)):
        show(fixFinal[i])
    print('Number of steps: ',len(steps)+len(fixFinal)-1)
