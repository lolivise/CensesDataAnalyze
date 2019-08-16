#!/bin/bash

echo Select States:
echo NSW, VIC, SA, WA, TAS, ACT
echo Select Parties:
echo ALP, LP, GRN

echo 
echo Pre-process Data...

# Enter the folder where the pre-process files are
cd code 
cd pre_proc_code

# Execute every file to generate pre-process data
for f in *.py;do
	echo Process file: $f
	python3 $f
done
echo
echo Display Hypotheses...

# Enter the folder where display result codes are
cd ..
cd display_code

# Execute every file to display the result
for f in *.py;do
	echo Process file: $f
	python3 $f
done
echo 
echo Complete!
