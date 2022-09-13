#!/usr/bin/perl
use POSIX;

#Storing the number of arguments entered in the terminal in a variable
my $arguments = $#ARGV+1;

#Throwing an error if the number of arguments entered in the terminal is not equal to 2
if($arguments != 2){
    print("Error: Two arguments needed\n");
    exit();
}

my $count = $ARGV[0];    #Storing the count argument in a variable
my $maxLength = $ARGV[1];  #Storing the maximum length argument in a variable
my $randomString = "";     #Initialising an empty random string
my $stringLength = 0;      #Initiallising the length of our random string

#Throwing an error if any of the arguments entered is 0
if($count==0 || $maxLength==0){
    print("Error: Arguments can not be 0\n");
    exit();
}

open(input, "input.txt") or die "File '$input' can't be opened"; #Opening our file from which the base string for generating random string has to be taken
  

$inputString=<input>;    #Storing the string given in the file in a variable
chomp($inputString);       #Trimming the edges of input string for unwanted characters
@baseString = split("", $inputString);  #Splitting the string into characters and storing it in an array of characters

my $lastChar='@'; #Initialising a variable for storing the last randomly chosen character 

#Running a loop for generating our random string
while(1)
{    
   my $rand1 = floor(rand(length($inputString)));  #Generating the first random number for selecting the index of character from the base string
   my $rand2 = floor(rand($count));              #Generating the second random number for the number of times the character is supposed to be repeated


   # Generating new pair of random numbers if the length of our string shall exceed the max length in this iteration
   if($stringLength+$rand2 > $maxLength){     
        if($stringLength==$maxLength){             #Breaking out of the loop if the length of our string is equal to the maximum length 

            last;
        }
     next;
   }
   
   $stringLength+=$rand2;       #Updating the new length of our random string
   
   
   #Running a loop for generating new random indexes in case the current chosen character is same as the last character
   while($baseString[$rand1] eq $lastChar){       
    $rand1 = floor(rand(length($inputString)));
   }
   
   #Updating the value of last character 
   if($rand2!=0){
   $lastChar=$baseString[$rand1];
   }

   #Adding characters to the random string
   while($rand2--){
    $randomString=$baseString[$rand1].$randomString;
   }
   
}

#Printing the random string the generated
print($randomString,"\n");


   
