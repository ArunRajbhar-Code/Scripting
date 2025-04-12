#!/bin/bash
echo "Enter a number"
read num
if [ $num -gt 0 ]; then
	echo "positive"
else 
	echo "Negative"
fi
