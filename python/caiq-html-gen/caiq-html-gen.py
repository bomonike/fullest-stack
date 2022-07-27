#!/usr/bin/env python3
# caiq-html-gen.py in https://github.com/bomonike/fullest-stack/blob/main/python/caiq-html-gen/caiq-html-gen.py
# by Wilson Mar and Kermit Vestal

import datetime
import time
import csv
# from os.path import exists
import os
from datetime import datetime 
from datetime import timezone


    # See https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
# User selections: TODO: choose in parameters within a GUI:
bool_output_console=True
bool_output_file=True
file_to_open='CAIQ4.0.1.csv' 
output_file_name="caiq-html-gen.md"  # GitHub Markdown format (no yaml)
print_categories=True
print_questions=True
print_annually=True
print_annually_only=False   # ignore lines with no annual in question
print_answers=True
print_answers_only=True     # ignore lines with no answers

# Validate run parameters:
output_file_delete_if_exists=True
# To avoid io.UnsupportedOperation: not writable, first verify if file exists
if os.path.exists(output_file_name) :
    print(f'*** file {output_file_name} being removed for rewrite ...')
    # No Prompt so this can run silent.
    os.remove(output_file_name)      
f = open(output_file_name, "a")

# Show what setting were selected for this run:
# Display run stats:
utc_dt = datetime.now(timezone.utc) # UTC time
local_dt = utc_dt.astimezone() # local time

now = datetime.now()  # Local time
local_now = now.astimezone()
local_tz = local_now.tzinfo
local_tzname = local_tz.tzname(local_now)

if bool_output_console == True :
    print("*** "+ str(local_dt) +" "+ local_tzname +" \r\n")
if bool_output_file == True :
    f.write("<-- "+ str(local_dt) +" "+ local_tzname +" -->\r\n")

run_stats_line=""
if bool_output_file == True :
    if len(output_file_name) == 0 :
        run_stats_line=run_stats_line + "output_file_name not specified. "
        bool_output_file=False

if print_annually == True :
    run_stats_line=run_stats_line + "Printing annually. "
else:
    run_stats_line=run_stats_line + "NOT Printing annually. "

if print_annually_only == True :
    run_stats_line=run_stats_line + "Printing annually_only. "

# Print only if there is an answer: Print only if there is no answer:
if print_answers == True :
    run_stats_line=run_stats_line + "Printing answers. "
else:
    run_stats_line=run_stats_line + "NOT Printing answers. "

if bool_output_console == True :
    print("*** "+ run_stats_line +"\r\n")
if bool_output_file == True :
    f.write("<-- "+ run_stats_line +" -->\r\n")

# Internal formatting options:
line_prefix="   "  # 3 chars
category_format="bold"  # or "Not"

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
    
    prev_title=""  # Def for next row.

    for row in csv_reader:
        if caiq_rows_read == 0:
            print(f'*** Column names are {", ".join(row)}')
            #  ID, _QID, _Title, _Question, _Answer_ID, _Answer
            # WARNING: Retrieving first column (ID) causes an error.
            caiq_rows_read += 1

        # Rest of lines: Get first 3 characters of _QID for Categories:
        first_qid_chars=row["_QID"][0:3]
        
        bool_print_caiq_line=True   # starting with all lines unless restricted.

        # See https://stackoverflow.com/questions/23866442/how-to-implement-efficient-filtering-logic-in-python
        if (row["_Question"].find('annual') != -1) :  # NOT FOUND
            if print_annually_only == True :
                bool_print_caiq_line=False
    
        if len(row["_Answer"]) == 0 and len(row["_Answer_ID"]) == 0 :  # Answer NOT present in line:
            if print_answers_only == True :  
                bool_print_caiq_line=False   # ignore lines with no answers
    
        # Print only if there is an answer: Print only if there is no answer:
        # if print_filter == "all" or len(row["_Answer"]) > 0 :
        if bool_print_caiq_line == True :
            caiq_rows_printed += 1
            prev_title=row["_Title"]  # for next row.

            # TODO: Instead Lookup CategoryText & CCM from csv file?
            # Lookup CategoryText from in-code table:
            if print_categories == True :
                if first_qid_chars != prev_first_qid_chars :
                    category_text = caiq_categories[first_qid_chars]  # not work
                    if category_format == "bold" :
                        category_display = "<strong>"+ first_qid_chars +" = "+ category_text + "</strong>"
                    else:
                        category_display = "### "+ first_qid_chars +" = "+ category_text
                    category_line="\r\n"+ line_prefix + category_display +"\r\n  \r\n"
                    if bool_output_console == True :
                        print(category_line)
                    if bool_output_file == True :
                        f.write(category_line)

                    prev_first_qid_chars=first_qid_chars  # for next row.
                    #   <a name="AIS-"></a>
                    #   ### AIS = Application & Interface Security  <- based on lookup of text for caiq-categories

            # If no title, get from previous row:
            if len(row["_Title"]) == 0 :
                caiq_title=prev_title
            else :
                caiq_title=row["_Title"]
            # Mix of ' and " works?
            title_line='1. <a href="#'+ row["_QID"] +'">'+ row["_QID"] +"</a> - "+ caiq_title +"<br /><br />\r\n  \r\n"
               #print(f'1. <a href="#{row["_QID"]}">{row["_QID"]}</a> - {caiq_title}<br /><br />\r\n   {row["_Question"]} ')
            if bool_output_console == True :
                print(title_line)
            if bool_output_file == True :
                f.write(title_line)

            if print_questions == True :
                question_text=line_prefix+ row["_Question"] +"\r\n"
                if bool_output_console == True :
                    print(question_text)
                if bool_output_file == True :
                    f.write(question_text)

            if print_answers == True :
                if len(row["_Answer_ID"]) != 0 :  # blank value
                    answer_text=row["_Answer_ID"] + " : "+ row["_Answer"]
                else :
                    answer_text=": "+ row["_Answer"]
                answer_line=line_prefix+ "ANSWER "+ answer_text +"\r\n  \r\n"
                if bool_output_console == True :
                    print(answer_line)
                if bool_output_file == True :
                    f.write(answer_line)

        caiq_rows_read += 1
    
    last_stats_line=str(caiq_rows_read) +" rows read, -1 title row. "+ str(caiq_rows_printed) +" rows printed."
    if bool_output_console == True :
        print("*** "+ last_stats_line)
    if bool_output_file == True :
        f.write("<-- "+ last_stats_line +" -->")

    # from dateutil import relativedelta
    # relativedelta.relativedelta(end_time,start_time).seconds

    f.close()