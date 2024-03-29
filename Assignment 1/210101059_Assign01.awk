# Run the program in ubuntu
# open terminal in the directory containing the program and enter
# >> awk -f 210101059_Assign01.awk INVENTORY.txt

BEGIN{ print "\n\t\t\t\t","INVENTORY REPORT\n"
print "Part No.\tPrice\tQuantity on Hand\tReorder Point\tMinimum Order\tOrder amount\n"}


{partNo=$1 
price=$2 
quantityOnHand=$3 
reorderPoint=$4 
minimumOrder=$5}


(quantityOnHand>=reorderPoint){
    print partNo,"\t\t",price,"\t\t",quantityOnHand,"\t\t",reorderPoint,"\t\t",minimumOrder,"\t\t",0
}


(quantityOnHand<reorderPoint){
    orderAmt=$4+$5-$3
    print partNo,"\t\t",price,"\t\t",quantityOnHand,"\t\t",reorderPoint,"\t\t",minimumOrder,"\t\t",orderAmt
}


END{
    print "\n\t\t\t\tEND REPORT\n"
}