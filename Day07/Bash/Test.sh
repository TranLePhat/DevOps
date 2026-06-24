#!/bin/bash

# echo "Hello, World!"
# echo
# echo "First line of Bash Script"


# Name=Phat
# Age=22
# Weight=60
# Date=


# echo 
# echo "My name is $Name"
# echo "My age is $Age"
# echo "My weight is $Weight"
# echo "My date is $Date"


# echo "Moi ban nhap b:"
# read b 

# echo $b
# echo

# a=5
# b=6
# echo `expr $a + $b`

# let "z=$z + 3"
# echo $z

# echo "Nhap so b:"
# read b
# echo "Nhap so a:"
# read a

# let "c=$a + $b"
# echo $c

# echo $?


echo "Nhap a:"
read a
echo "Nhap b:"
read b

if [ $a -lt $b ]
then
    echo "$a nho hon $b"
elif [ $a -eq $b ]
then
    echo "$a bang $b"
else
    echo "$a lon hon $b"
fi


