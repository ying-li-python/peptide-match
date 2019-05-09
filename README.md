# Identify PTMs by peptide match
Trying piece together peptide sequences and locating PTM sites from proteomics MS data is time-consuming and repeatitive. 

Proteomics data is so common, why is there no program available to help researchers find where the peptide sequence lies on the protein and identify a PTM site? 

## Featured 
- [Peptide-match](https://peptide-match.herokuapp.com/), an alternative web-based app for peptide match and locating PTM sites
- Step-by-step [tutorial](https://creativepython.wordpress.com/2019/03/29/biologypython-peptide-match-for-ptm-site-identification-with-python-tutorial/) if you want to learn how I wrote the program

## Introduction
This folder contains the Python program that can be ran in terminal, and your analysis is recorded and stored in a new a csv file.

## Prerequisites
- Python3
- FASTA file of your target/reference sequence 

## Resources 
- Peptides of PERIOD (*Drosophila melanogaster*) were used as examples from my [*Plos Genetics* paper](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1007953)

## Getting started 
The entire protein sequence in your FASTA file should be in one line. For additional guidance, please visit my [tutorial](https://creativepython.wordpress.com/2019/03/27/biologyhelp-fix-fasta-indentation-in-python/) or my [fasta-fix](https://github.com/ying-li-python/fasta-fix) repository. 

Clone the repository from github and go into the peptide-search folder in terminal.
```
git clone https://github.com/ying-li-python/peptide-search.git
cd peptide-search 
```

## Instructions 

1. Add the FASTA file of your reference protein to the peptide-search folder.

2. In terminal, open peptides.py using a code editor of your choice 
``` 
open peptides.py
```

3. Please replace the name of example FASTA file to your FASTA file. Save the changes. 

## Running the script 
Please do steps 1-3 to confirm that the reference protein sequence is correct before your peptide analysis.

Run the script in terminal
```
python main.py
```

You should see: 

<img src="https://raw.githubusercontent.com/ying-li-python/peptide-search/master/Images/terminal.png">

You will be asked to enter a peptide sequence and the location of a phosphorylation site on the peptide. If you do not have a PTM site, enter 0.

## Results 
Once you are done adding the peptides to analyze, you can quit the program and check the output csv file in Excel or in terminal. 

It should look like this: 

<img src="https://raw.githubusercontent.com/ying-li-python/peptide-search/master/Images/output.png"> 

And you're done! 

## Author
Ying Li 
