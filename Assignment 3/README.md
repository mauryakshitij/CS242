# Assignment 03

---

1. **Name**: Kshitij Maurya
2. **Roll No.** : 210101059

## Task 01

- Open terminal in the directory containing the program file

- Run the program using the following command in terminal (use python3 instead of python on linux based systems)

      python josephus.py

- Enter the value of total number of people and the skip number as inputs

#### Explanation

- First all the people are stored in a list as 1,2,3...n (alphabets are not used as n may be >26)and the first person is assigned to be the killer
- The killer kills the person who is skip number indexes right to him
- Then the person to the right of the person killed is assigned to be the killer
- This loop keeps running till there is only a single person remaining

## Task 02

- Open terminal in the directory containing the program file

- Run the program using the following command in terminal (use python3 instead of python on linux based systems)

      python puzzle.py

- Enter the configuration of the initial grid and final grid in a single line (use 0 for blank space)

- eg. 

      4 5 6 
      1 2 3 should be entered as 1 2 3 4 5 6 7 8 0 
      7 8 0 

#### Explanation

- The underlying algorithm is based on cyclic rotation of the grid in 4 different cycles 
- First the program checks if the last position of the final grid is 0 or not , if it is 0 it proceeds else it makes the last position 0 using some moves and stores the moves in a list called fixFinal
- Then a dictionary maps the reference grid to the final grid
- The algorithm then fixes the position of 0 in the initial grid to the last index
- After that 1 is shifted to the 0th index of grid using some moves
- After that 2 is shifted to the 2nd index of grid and the position of 3 is checked
- If the positioning of 3 is correct we proceed to fix 2 and 3 at their correct respective positions, if the positioning of 3 was wrong we make some fixed steps to make its positioning correct
- Then 4 is placed at the 6th index using some moves and the position of 7 is checked
- If the positioning of 7 is correct we proceed to fix 4 and 7 at their correct respective positions, if the positioning of 7 was wrong we make some fixed steps to make its positioning correct
- Then 5 is brought to the 4th index using some moves 
- If the positioning of 6 and 8 is correct after this we print all the steps required till here and the steps required to fix the final grid in reverse order
- If the positioning of 6 and 8 is not correct then the input it prints not solvable and exits
