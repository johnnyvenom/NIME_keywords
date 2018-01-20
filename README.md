keyword.sh
written by John Sullivan
January 2018

A command line utility to search the archive of NIME conference proceedings (nime.org/archive). 

To use: 
- Go to www.nime.org/archive to download conference proceedings for all years (2001 - 2017)
- Place each year's proceedings (several .pdf files) in its own directory with the year as its nome, and place this script in the parent directory. 
- Run the following command to make it executable:
    
    chmod u+x keyword.sh

- Run the command with as many search terms you want to return:

    ./keyword.sh searchterm1 searchterm2 searchterm3 etc.

The script will save the results to data.csv in two parts: 

1. A table will show the number of occurrences for each search term by year. 
2. Below the table, the full filenames for all occurrences will be listed by year and by search term. 

Notes: 
 
- This script uses the 'mdfind -count' command to search. 
- It runs a loop to search through all years, but can easily be modified to more specific search criteria. 

