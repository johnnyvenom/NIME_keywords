# keyword.sh

A command line utility to search the archive of NIME conference proceedings (http://nime.org/archive). 

written by John Sullivan | johnny@johnnyvenom.com

## To use: 

- Go to http://nime.org/proceedings/ZIPs/ to download conference proceedings for all years
- Unzip and place each year's proceedings (several .pdf files) in its own directory with the year as its name, and place this script in the parent directory. 
- Run the following command to make it executable:
    
    `chmod u+x keyword.sh`

- Run the command with as many search terms you want to return:

    `./keyword.sh searchterm1 searchterm2 searchterm3 etc.`

The script will save the results to data.csv in two parts: 

1. A table will show the number of occurrences for each search term by year. 
2. Below the table, the full filenames for all occurrences will be listed by year and by search term. 

## Notes: 
 
- This script uses the `mdfind -count` command to search. 
- It runs a loop to search through all years, but can easily be modified to more specific search criteria, or to search other collections.
- This script was written to assist research in the preparation of [this]() paper for the 2018 SMC conference. The methodology was adapted from the 2014 NIME paper ["To gesture or Not? An Analysis of Terminology in NIME Proceedings 2001-2013"](https://www.nime.org/proceedings/2014/nime2014_351.pdf) by A. Jensenius. 
- See also the [additional_scripts](additional_scripts) folder, which contains additional information and tools for the analysis used for the SMC paper. 
