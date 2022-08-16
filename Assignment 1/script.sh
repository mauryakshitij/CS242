#!/bin/bash
printf '\n\t\t\t\t\tPAYROLL REGISTER\n\n'
echo " Employee No.  Department    Pay rate   Exempt  Hours worked    Base pay   Overtime pay  Total pay"
printf '\n'


file="EMPLOYEE.txt"

#storing data from fields into variables
while IFS=" " read employeeNo department payRate exempt hoursWorked
do

if [ "$exempt" = "Y" ];
then
    overtime=0
else
    overtime=$(echo $payRate*$(($hoursWorked-40))*0.5|bc)
    
fi
    basicPay=$(echo $payRate*$hoursWorked | bc)
    totalPay=$(echo $basicPay+$overtime|bc)
    printf ' %s\t\t%s\t\t%s\t  %s\t\t%s\t%.2f\t\t%.2f\t %.2f\n' "$employeeNo" "$department" "$payRate" "$exempt" "$hoursWorked" "$basicPay" "$overtime" "$totalPay"

done <"$file"

printf '\n'