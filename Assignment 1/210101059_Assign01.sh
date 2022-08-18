# Run the program in ubuntu
# open terminal in the directory containing the program
# make the script executable by entering
# >> chmod +x 210101059_Assign01.sh
# execute by script by entering
# >> ./210101059.Assign01.sh 

#!/bin/bash

#printing the header
printf '\n\t\t\t\t\t\033[4mPAYROLL REGISTER\033[0m\n\n'
echo -e " \033[1mEmployee No.  Department    Pay rate   Exempt  Hours worked    Base pay   Overtime pay  Total pay\033[0m"
printf '\n'


input="EMPLOYEE.txt"

#storing data from fields into variables
while IFS=" " read employeeNo department payRate exempt hoursWorked
do

if [ "$exempt" = "Y" ];
then
    overtime="false"
else
    overtime="true"    
fi


if [ "$overtime" = "true" ];
then
    overtimePay=$(echo $payRate*$(($hoursWorked-40))*0.5|bc)
else
    overtimePay=0
fi

basicPay=$(echo $payRate*$hoursWorked|bc)
totalPay=$(echo $basicPay+$overtimePay|bc)
printf ' %s\t\t%s\t\t%s\t  %s\t\t%s\t%.2f\t\t%.2f\t %.2f\n' "$employeeNo" "$department" "$payRate" "$exempt" "$hoursWorked" "$basicPay" "$overtimePay" "$totalPay"

done <"$input"

printf '\n'