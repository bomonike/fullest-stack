#!/usr/bin/env python3
# caiq-html-gen.py in https://github.com/bomonike/fullest-stack/blob/main/python/caiq-html-gen/caiq-html-gen.py
# by Wilson Mar and Kermit Vestal

import csv
    # See https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html

# User selections: TODO: choose in parameters:
file_to_open='CAIQ4.0.1.csv'

# TODO: Output to file instead of STDOUT:
output_file_name="caiq-html-gen.txt"

print_annually=True
print_annually_only=False
print_answers=True
  
with open(file_to_open, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    caiq_rows_read = 0
    caiq_rows_printed = 0
    prev_first_qid_chars=""
    caiq_categories = {
    'A&A': 'Audit Assurance & Compliance',
    'AIS': 'Application & Interface Security',
    'BCR': 'Business Continuing Management & Operational Resilience',
    'CCC': 'Change Control & Configuration Management',
    'CEK': 'Cryptography, Encryption, and Key Management',
    'DCS': 'Datacenter Security',
    'DSP': 'Data Security & Privacy Lifecycle Management',
    'GRC': 'Governance, Risk Management, and Compliance',
    'HRS': 'Human Resources',
    'IAM': 'Identity & Access Management',
    'IPY': 'Interoperability & Portability',
    'IVS': 'Infrastructure & Virtualization Security',
    'LOG': 'Logging and Monitoring',
    'SEF': 'Security Incident Management, E-Discovery, and Cloud Forensics',
    'STA': 'Supply Chain Management, Transparancy, and Accountability',
    'TVM': 'Threat and Vulnerability Management',
    'UEM': 'Universal Endpoint Management'
    }
    
    if print_annually == True :
        print(f'*** Printing annually ')
    else:
       print(f'*** NOT Printing annually ')

    if print_annually_only == True :
        print(f'*** Printing annually_only ')
    
    # Print only if there is an answer: Print only if there is no answer:
    if print_answers == True :
       print(f'*** Printing answers ')
    else:
       print(f'*** NOT Printing answers ')

    prev_title=""  # Def for next row.

    for row in csv_reader:
        if caiq_rows_read == 0:
            print(f'*** Column names are {", ".join(row)}')
            #  ID, _QID, _Title, _Question, _Answer_ID, _Answer
            # WARNING: Retrieving first column (ID) causes an error.
            caiq_rows_read += 1

        # Rest of lines: Get first 3 characters of _QID:
        first_qid_chars=row["_QID"][0:3]
        
        bool_print_caiq_line=True   # starting with all lines unless restricted.

        if (row["_Question"].find('annual') != -1) :  # FOUND
            # print(" annually found")
            if print_annually == True :
                bool_print_caiq_line=True
        else:
            if print_annually_only == True :
                bool_print_caiq_line=False
    
        # See https://stackoverflow.com/questions/23866442/how-to-implement-efficient-filtering-logic-in-python

        # Print only if there is an answer: Print only if there is no answer:
        # if print_filter == "all" or len(row["_Answer"]) > 0 :
        if bool_print_caiq_line == True :
            caiq_rows_printed += 1

            # TODO: Instead Lookup CategoryText from csv file?
            # Lookup CategoryText from in-code table:
            if first_qid_chars != prev_first_qid_chars :
                Category_text = caiq_categories[first_qid_chars]  # not work
                print(f'\r\n   <a name="{first_qid_chars}-"></a>\r\n\r\n   ### {first_qid_chars} = {Category_text} \r\n ')
                prev_first_qid_chars = first_qid_chars
                #   <a name="AIS-"></a>
                #   ### AIS = Application & Interface Security  <- based on lookup of text for caiq-categories

            if len(row["_Title"]) == 0 :
                caiq_title=prev_title
            else :
                caiq_title=row["_Title"]
            print(f'1. <a href="#{row["_QID"]}">{row["_QID"]}</a> - {caiq_title}<br /><br />\r\n   {row["_Question"]} ')

            if print_answers == True :
                # Show only if there is content - https://datagy.io/python-check-empty-string/
                if len(row["_Answer"]) != 0  and print_answers == True :  # blank value
                    if len(row["_Answer_ID"]) != 0 :  # blank value
                       answer_text=row["_Answer_ID"] + " : "+ row["_Answer"]
                    else :
                       answer_text=": "+ row["_Answer"]
                    print(f'   ANSWER {answer_text} \r\n')
#                else :
#                    print("   ________ \r\n")

        prev_title=row["_Title"]  # for next row.

        caiq_rows_read += 1
    
    print(f'*** {caiq_rows_read} rows read, -1 title row. {caiq_rows_printed} rows printed.')
