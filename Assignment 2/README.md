# Assignment 02

---

1. **Name**:  Kshitij Maurya  
2. **Roll No.** : 210101059
3. **OS** : Ubuntu 22.04 LTS

## Task 01

- Make a file that contains the list of files to be backed up ( here I have given a list.txt file for the same)
    - Enter name of each file with extension in new line
    - Make sure to add a new line after the name of last file

- Create a directory in which files are supposed to be backed up( here I have given a directory named drive for the same)

- Open terminal in the directory containing the script
- Run the following command to make the script executable

  `$ chmod +x backup.scr`

- Execute the bash script using the following command( change the name of file and directory if you create new file or directory )
    - the first argument is the name of file and the second argument is the name of directory

    `$ ./backup.scr list.txt drive`

#### Explanation

- The code stores the number of arguments entered and in case it is not equal to two it throws an error accordingly
- The code checks if the first argument is a file and if the second argument is an existing directory and throws an error if any condition fails
- A loop reads the name of files from the input file and copies it to the desired directory and adds .bak to its extension


## Task 02

- Make a file "input.txt" (already exists in this directory) and enter the string from which new random strings are to be generated in it.

- Open terminal in the directory containing the script

- Run the perl script using the following command 
    - Enter Count as the first argument and maximum length as the second argument

      `$ perl random.pl #count #length`

- *The program outputs a random string of length equal to the max length*

    

#### Explanation

- The code stores the number of arguments entered in a variable and throws an error if the number of arguments entered is not equal to 2.
- If any argument entered is 0, the code throws an error
- Initialise an empty random string and another variable which stores it's length at any instance
- Open "input.txt" and store the string in it as a character array
- A loop runs and generates two random numbers for index and number of repetitions respectively and concatenates the string so generated to the random string to be generated finally
- The code keeps a record of the last random character selected and makes sure that the next random character generated is different from the last one
- It generates a new pair of random numbers if the length of string shall exceed the max length in this iteration
- The loop ends when length of string is equal to max length

