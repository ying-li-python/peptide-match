"""
Piecing together peptide data from mass-spectrometry proteomics is time-consuming and daunting. 

Luckily, this script can help find the sequence location of a target protein and locate a PTM site. 
Every peptide entered and analyzed will be recorded to a new csv file so you will have a copy of 
your peptide analysis. 

BEFORE STARTING 
You will need to add a reference FASTA file in peptides.py for Python to match the peptide. 


EXPECTED RESULTS 
The program will generate a new csv file containing for every peptide sequence entered, as well 
as the peptide location (start and end), and the PTM site. 

Good luck!

"""

# import the functions to this file and csv module 
from peptides import peptideSearch
import csv 


# create a new csv file and write header rows 
with open('peptideSearch_output.csv', 'w') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(["Peptide Sequence", "Start", "End", "PTM Site"])

# create variable for while loop 
ans = "y"

# create variable to store list of peptides entered by user 
peptide_list = []

# while loop for user to enter peptide sequence and phosphorylation site 
while ans == "y": 

    # count the number of peptides entered 
    peptide_count = len(peptide_list)

    # set conditional that once one peptide has been entered, it will track the number of peptides entered 
    if peptide_count > 0: 
        print(f"The number of peptides you have analyzed: {peptide_count}")

    # asks user for peptide sequence 
    peptide = input("Please enter a peptide sequence to analyze: ").upper()

    # add peptide sequence to peptide list 
    peptide_list.append(peptide)
    
    # asks phosphorylation position. if you do not have one, please enter 0.  
    phospho_site = int(input("Please enter the phosphorylation position on the sequence (if none, enter 0): "))

    # call the function to perform the peptide analysis 
    peptideSearch(peptide, phospho_site)
        
    # asks if you want to continue adding more peptide sequences     
    ans = input("Do you want to add another peptide sequence? (y/n) ")
    

