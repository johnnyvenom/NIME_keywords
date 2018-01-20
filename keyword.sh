#!/bin/bash
# return count of papers containing keywords

f="data.csv"
echo "keyword extractor" > $f

# table with # of papers containing keywords by year
#create header row with years
printf "terms," >> $f
for (( i=2001; i<=2017; i++))
do 
	printf "$i," >> $f
done

printf "\n" >> $f

#output data to table
for KEYWORD in "$@"
do
	printf "$KEYWORD, "
	printf "$KEYWORD," >> $f
	for (( i=2001; i<=2017; i++))
	do
		num=$(mdfind -count $KEYWORD -onlyin $i)
		
		printf "$num,"
		printf "$num," >> $f
	done
	printf "\n"
	printf "\n" >> $f
done

#printf "\n" >> $f
#printf "\n" >> $f

#return filenames 
printf "\n\nany keyword\n" >> $f
#printf "\n" >> $f

for (( i=2001; i<=2017; i++))
do
	echo $i >> $f
	for KEYWORD in "$@"
	do
		echo " , $KEYWORD" >> $f
		filename=$(mdfind $KEYWORD -onlyin $i)
		printf "$filename," >> $f
		# printf "$KEYWORD," >> $f
		# printf "$i," >> $f
		printf "\n\n" >> $f
	done
done		