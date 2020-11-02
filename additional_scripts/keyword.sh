#!/bin/bash
# return count of papers containing keywords

startyear=2004
endyear=2016
f="data.csv"
echo "keyword extractor" > $f

# table with # of papers containing keywords by year
#create header row with years
printf "terms," >> $f
for (( i=$startyear; i<=$endyear; i++))
do 
	printf "$i," >> $f
done
printf "\n" >> $f

printf "total number of papers, " >> $f
for (( i=$startyear; i<=$endyear; i++))
do 
	papers_by_year=$(mdfind -count -onlyin $i pdf)
	printf "Year: $i - $papers_by_year papers \n"
	printf "$papers_by_year," >> $f
done
printf "\n" >> $f

#output data to table
for KEYWORD in "$@"
do
	printf "$KEYWORD, "
	printf "$KEYWORD," >> $f
	for (( i=$startyear; i<=$endyear; i++))
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

for (( i=$startyear; i<=$endyear; i++))
do
	echo "Year: $i"
	echo $i >> $f
	for KEYWORD in "$@"
	do
		echo "Keyword: $KEYWORD"
		echo " , $KEYWORD" >> $f
		filename=$(mdfind $KEYWORD -onlyin $i)
		printf "$filename," >> $f
		echo $filename
		# printf "$KEYWORD," >> $f
		# printf "$i," >> $f
		printf "\n\n" >> $f
		
	done
done		
