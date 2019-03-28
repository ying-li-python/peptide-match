"""
This is the core part of the Python program. I created nested functions where the 
first function reads the FASTA file as a reference sequence wnd the second is the 
peptide match and records each output on a new line in the csv file. 

REQUIREMENTS
The entire protein sequence from FASTA must be written in a single line 
(no breaks in between). Please visit here for guidance: 
https://github.com/ying-li-python/fasta-fix 


"""
def peptideSearch(peptide, phospho_site):

    # the first function (no arguments needed)
    def fastaFile(): 

        # create variable to store reference sequence 
        ref_seq = ''

        # open FASTA file, please change accordingly 
        fastaFile = open("period.fasta", 'r')

        # create for loop 
        for line in fastaFile: 

            # ignore first line in FASTA 
            if line.startswith(">"):

                # this does nothing, allows script to keep going 
                pass
            
            # next line is your reference sequence, so will be stored as ref_seq 
            else: 
                ref_seq = line 

        # the function will return the ref_seq 
        return ref_seq

    # assign output variable to store ref_seq
    output = fastaFile()

    # this is the main function to perform the peptide match
    def peptideMatch(peptide, phospho_site): 
        
        # import dependencies 
        import re
        import csv
        import os 

        # create variables to store lists 
        peptide_list = []
        start_list = []
        end_list = []
        p_site_list = []

        # use regex module to match the peptide sequece to reference sequence 
        match = re.search(peptide, output)

        # for every peptide entered, add to peptide list 
        peptide_list.append(peptide)
        
        # set phosphorylation position to 0 
        phospho_position = 0
        
        # create conditional if peptide matches
        if match: 

            # create variable to store the location of start and end position 
            start_position = match.start()
            end_position = match.end()

            # add 1 to start and end position to correct indexing 
            start_position = int(start_position) + 1
            end_position = int(end_position) + 1

            # add results to list 
            start_list.append(start_position)
            end_list.append(end_position)
            
            # calculate the phosphorylation site 
            if int(phospho_site) > 0: 
                phospho_position = (start_position - 1) + phospho_site
                p_site_list.append(phospho_position)

            # if 0 is entered, return "None"
            else: 
                phospho_position = "None" 
                p_site_list.append(phospho_position)

            # print results in terminal
            print("-----------------") 
            print(f"Peptide matched and added to analysis!")
            print("-----------------")

            # compile all the lists as a tuple 
            peptide_search_results = zip(peptide_list, start_list, end_list, p_site_list)


            # add peptide sequence and results to current csv file 
            with open('peptideSearch_output.csv', 'a') as csvfile: 

                # initiate csvwriter 
                peptide_writer = csv.writer(csvfile, delimiter=',')

                # write the results to each row for every peptide entered
                peptide_writer.writerows(peptide_search_results)
            
        # print an error message if peptide sequence not matched  
        else: 
            print("-----------------") 
            print("Peptide not found in reference FASTA sequence. Please try again.")
            print("-----------------")

    # return the results
    return peptideMatch(peptide, phospho_site)