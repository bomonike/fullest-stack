#!/usr/bin/env python3
# caiq-yaml-gen.py in https://github.com/bomonike/fullest-stack/blob/main/python/caiq-yaml-gen/caiq-yaml-gen.py
# by Wilson Mar and Kermit Vestal

# This outputs a yaml-formatted file based on lines input from a csv file.
# The output file will be copied to a GitHub repo's _posts folder for generation for display in a github.io site.
# There is a hierarchy in the inputs and outputs: Category, Title, Question, Answer.
# Text is carries over from previous row so the assumed value is displayed if blank.
# Output is filtered and formatted according to various boolean flags.

import csv
import os
from datetime import datetime 
from datetime import timezone

this_program_name="caiq-yaml-gen.py"

# Capture date/time with local offset:
utc_dt = datetime.now(timezone.utc) # UTC time
local_dt = utc_dt.astimezone() # local time

now = datetime.now()  # Get tzname from https://www.timeanddate.com/time/zones/
local_now = now.astimezone()
local_tz = local_now.tzinfo
local_tzname = local_tz.tzname(local_now)


# User selections: TODO: choose in parameters within a GUI:
bool_output_console=True
bool_output_file=True
bool_output_table=True

print_categories=True
print_questions=True
print_annually=True
print_annually_only=False   # ignore lines with no annual in question
print_answers=True
print_answers_only=True     # ignore lines with no answers

file_subject_text="for Consul users' auditors"
file_to_open='CAIQ4.0.1.consul.csv' 

#output_file_date=str(local_dt)[0:10]
output_file_date="2022-08-09"
output_file_prefix="CAIQ4.0.1.consul"
output_file_name=output_file_date+"-"+output_file_prefix+".md"  # Like 2021-05-12-caiq-yaml-gen.md
    # See https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
# Validate run parameters:
output_file_delete_if_exists=True
# To avoid io.UnsupportedOperation: not writable, first verify if file exists
if os.path.exists(output_file_name) :
    print(f'*** file {output_file_name} being removed for rewrite ...')
    # No Prompt so this can run silent.
    os.remove(output_file_name)      
f = open(output_file_name, "a")

# Show what setting were selected for this run:
run_stats_line=""
if bool_output_file == True :
    if len(output_file_name) == 0 :
        run_stats_line=run_stats_line + "output_file_name not specified"
        bool_output_file=False

# Print only if there is an answer: Print only if there is no answer:
if print_annually == True :
    if print_annually_only == True :
        run_stats_line=run_stats_line + "Annual questions only"

if print_answers == True :
    if print_answers_only == True :
       run_stats_line=run_stats_line + "Only questions with answers"

# Internal formatting options:
line_prefix="   "  # 3 chars
category_format="###"  # "bold" or "Not"


# Output yaml heading:
if bool_output_console == True :
    print("*** "+ str(local_dt) +" "+ local_tzname +"\r\n")
    print("*** "+ run_stats_line +"\r\n")
if bool_output_file == True :
    f.write("---" +"\r\n")
    f.write("layout: post" +"\r\n")
    f.write("date: \""+ output_file_date +"\"\r\n")
    f.write("file: \""+ output_file_prefix  +"\"\r\n")
    f.write("title: \"CAIQ (Consensus Assessment Initiative Questionnaire) " + file_subject_text +".\"\r\n")
    f.write("excerpt: \""+ run_stats_line +" generated from file "+ file_to_open +" by "+ this_program_name +"\"\r\n")
    f.write("tags: [cloud, security, management, audit]" +"\r\n")
    f.write("---" +"\r\n")

    f.write("\r\n")
    f.write("<!-- At https://github.com/bomonike/fullest-stack/blob/main/python/caiq-yaml-gen/ -->\r\n")
    f.write("\r\n")

    f.write("## Categories in the CAIQ\r\n")
    f.write("\r\n")

# Output Category summary:
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
for key, value in caiq_categories.items():
    print_line="1. <a href=\"#"+ key +"-\"><tt>"+ key +"</tt></a> = "+ value
    if bool_output_console == True :
        print(f'{print_line}')
    if bool_output_file == True :
        f.write(f'{print_line} \r\n')

if bool_output_console == True :
    print("\r\n---------")
if bool_output_file == True :
    f.write("\r\n<hr />\r\n")


# Output yaml heading:
if bool_output_file == True :
    f.write("\r\n")
    f.write("## "+ run_stats_line +" in the CAIQ "+ file_subject_text +" (by Category)\r\n")
    f.write("\r\n")
    if bool_output_table == True :
        f.write('<table border="1" cellpadding="4" cellspacing="0">\r\n')
        f.write('<tr valign="bottom"><th> CAIQ Item & Title </th><th> Question </th><th>Imp?</th><th> Answer </th></tr>\r\n')
        f.write("\r\n")

with open(file_to_open, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    caiq_rows_read = 0
    caiq_rows_printed = 0
    prev_first_qid_chars=""
    
    category_lines_out=0
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

            # TODO: Instead Lookup CategoryText & CCM from csv file?
            # Lookup CategoryText from in-code table:
            if print_categories == True :
                if first_qid_chars != prev_first_qid_chars :

                    # For GitHub Markdown weirdness:
                    if category_lines_out == 0 :  # Except first line 
                        category_prefix=""       # for GitHub Markdown weirdness
                    else:
                        category_prefix=line_prefix

                    category_text = caiq_categories[first_qid_chars]  # not work
                    category_line="<a name=\""+ first_qid_chars +"-\"></a>"
                    if bool_output_console == True :
                        print(category_prefix+category_line+"\r\n")
                    if bool_output_file == True :
                        if bool_output_table == True :
                            f.write('\r\n<tr valign="top"><td colspan="4">' + category_prefix+category_line )
                        else:
                            f.write(category_prefix+category_line)

                    if category_format == "bold" :
                        category_display = line_prefix+"<strong>"+ first_qid_chars +" = "+ category_text + "</strong>"
                    else:
                        category_display = category_prefix+"### "+ first_qid_chars +" = "+ category_text

                    category_line="\r\n"+ category_display +"<br /><br />\r\n \r\n"
                    if bool_output_console == True :
                        print(category_line)
                    if bool_output_file == True :
                        if bool_output_table == True :
                            f.write("<bold>"+ first_qid_chars +" = "+ category_text + '</bold></td></tr>\r\n')
                        else:
                            f.write(category_line)

                    category_lines_out += 1
                    prev_first_qid_chars=first_qid_chars  # for next row.
                    #   <a name="AIS-"></a>
                    #   ### AIS = Application & Interface Security  <- based on lookup of text for caiq-categories

            # If no title, get from previous row:
            if len(row["_Title"]) == 0 :
                caiq_title=prev_title
            else :
                caiq_title=row["_Title"]
            # Mix of ' and " works?
            title_line='1. <a href="#'+ row["_QID"] +'"></a>'+ row["_QID"] +" - "+ caiq_title +"\r\n \r\n"
            if bool_output_console == True :
                print(title_line)
            if bool_output_file == True :
                if bool_output_table == True :
                    f.write('<tr valign="top"><td>'+ str(caiq_rows_printed) +'. <a href="#'+ row["_QID"] +'"></a>'+ row["_QID"] +" - "+ caiq_title )
                else:
                    f.write(title_line)

            if print_questions == True :
                question_text=line_prefix+ row["_Question"] +"\r\n"
                if bool_output_console == True :
                    print(question_text)
                if bool_output_file == True :
                    if bool_output_table == True :
                        f.write("</td><td> " + row["_Question"] )
                    else:
                        f.write(question_text)

            if bool_output_table == True :
                f.write("</td><td> Y ")

            if print_answers == True :
                if len(row["_Answer_ID"]) != 0 :  # blank value
                    answer_text=row["_Answer_ID"] + " : "+ row["_Answer"]
                else :
                    answer_text=": "+ row["_Answer"]
                answer_line=line_prefix+ "ANSWER "+ answer_text +"\r\n  \r\n"
                if bool_output_console == True :
                    print(answer_line)
                if bool_output_file == True :
                    if bool_output_table == True :
                        f.write("</td><td> " + row["_Answer"] )
                    else:
                        f.write(answer_line)

            if bool_output_table == True :
                f.write('\r\n</td></tr>\r\n')

        caiq_rows_read += 1
        if len(row["_Title"]) > 0 :
           prev_title=row["_Title"]  # Save for next row if title is blank

    last_stats_line=str(caiq_rows_read) +" rows read, "+ str(category_lines_out) +" categories, "+ str(caiq_rows_printed) +" rows printed."
    if bool_output_console == True :
        print("*** "+ last_stats_line)
    if bool_output_file == True :
        if bool_output_table == True :
            f.write('</table>')
            f.write("\r\n")
        f.write("<-- "+ last_stats_line +" -->")

    # TODO: Display elapsed time for run:
    # from dateutil import relativedelta
    # relativedelta.relativedelta(end_time,start_time).seconds

    f.close()