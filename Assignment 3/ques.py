

referenceGrid = [1, 2, 3,
                 4, 5, 6,
                 7, 8, 0]

finalGrid = [1, 2, 3,
             4, 5, 6,
             7, 8, 0]

initialGrid = [1, 0, 2,
               4, 5, 3,
               7, 8, 6]

steps = []

dict1 = {}

for i in range(9):
    dict1[finalGrid[i]] = referenceGrid[i]



def AppendStep():
    if(len(steps)==0):
     steps.append(initialGrid.copy())
    elif(initialGrid != steps[-1]):
        steps.append(initialGrid.copy())
    


def show(a):
    print()
    for i in range(9):
        print(a[i], end=" ")
        if(i % 3 == 2):
            print()
    print("\n--------------------------------------------------------")


def rotate0(a):
    temp = a[0]
    a[0] = a[3]
    a[3] = a[6]
    a[6] = a[7]
    a[7] = a[8]
    a[8] = a[5]
    a[5] = a[2]
    a[2] = a[1]
    a[1] = temp
    AppendStep()


def rotate1(a):
    temp = a[8]
    a[8] = a[5]
    a[5] = a[4]
    a[4] = a[7]
    a[7] = temp
    AppendStep()


def switch1(a):
    temp = a[0]
    a[0] = a[3]
    a[3] = a[6]
    a[6] = a[7]
    a[7] = a[5]
    a[5] = a[2]
    a[2] = a[1]
    a[1] = temp
    AppendStep()


def switch2(a):
    temp = a[1]
    a[1] = a[4]
    a[4] = a[7]
    a[7] = a[5]
    a[5] = a[2]
    a[2] = temp
    AppendStep()


def switch3(a):
    temp = a[3]
    a[3] = a[6]
    a[6] = a[7]
    a[7] = a[5]
    a[5] = a[4]
    a[4] = temp
    AppendStep()


def switch4(a):
    temp = a[4]
    a[4] = a[7]
    a[7] = a[5]
    a[5] = temp
    AppendStep()



AppendStep()

if(initialGrid[5] == dict1[0]):
    while(initialGrid[8] != dict1[0]):
        rotate1(initialGrid)

while(initialGrid[8] != dict1[0]):
    rotate0(initialGrid)

while(initialGrid[0] != dict1[1]):
    switch1(initialGrid)

while(initialGrid[3] == dict1[2] or initialGrid[6] == dict1[2]):
    switch3(initialGrid)

while(initialGrid[2] != dict1[2]):
    switch2(initialGrid)

while(initialGrid[3] == dict1[3] or initialGrid[6] == dict1[3]):
    switch3(initialGrid)

if(initialGrid[1] != dict1[3]):
    while(initialGrid[5] != dict1[3]):
        switch4(initialGrid)
    while(initialGrid[2] != dict1[3]):
        switch2(initialGrid)
else:
    switch2(initialGrid)
    switch4(initialGrid)
    while(initialGrid[2] != dict1[2]):
        switch2(initialGrid)
    switch4(initialGrid)
    while(initialGrid[1] != dict1[2]):
        switch2(initialGrid)


while(initialGrid[6] != dict1[4]):
    switch3(initialGrid)


if(initialGrid[3] != dict1[7]):
    while(initialGrid[7] != dict1[7]):
        switch4(initialGrid)
    while(initialGrid[6] != dict1[7]):
        switch3(initialGrid)
else:
    switch3(initialGrid)
    while(initialGrid[7] != dict1[7]):
        switch4(initialGrid)
    while(initialGrid[3] != dict1[7]):
        switch3(initialGrid)
    while(initialGrid[4] != dict1[4]):
        switch4(initialGrid)
    while(initialGrid[3] != dict1[4]):
        switch3(initialGrid)


while(initialGrid[4] != dict1[5]):
    switch4(initialGrid)
if(initialGrid[5] != dict1[6]):
    print("No Solution")
else:
    for i in range (len(steps)):
        show(steps[i])