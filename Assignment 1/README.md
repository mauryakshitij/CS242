# Assignment 01

---

1. **Name**:  Kshitij Maurya  
2. **Roll No.** : 210101059
3. **OS** : Ubuntu 22.04 LTS

## Task 01

- The awk script takes input from "INVENTORY.txt" and stores the fields in variables and then calculates
the output amount depending on the quantity of item available on hand.

- To run the awk script open terminal in the directory containing the program and run the following command

  `$ awk -f 210101059_Assign01.awk INVENTORY.txt`


## Task 02

- The bash script takes EMPLOYEE.txt as input and calculates the total pay of the employees according to 
their exemption status and hours worked

    *Base pay is calculated by multiplying the total hours worked times pay rate*
    *Overtime pay is calculated by multiplying half the hours worked over 40 times pay rate*
    *Therefore Total pay is the sum of Base pay and Overtime pay*

- To run the bash script, make it executable by running the following command in the terminal window in the directory
containing the program

    `$ chmod +x 210101059.Assign01.sh`

- Execute the bash script using the following command

    `$ ./210101059.Assign01.sh`