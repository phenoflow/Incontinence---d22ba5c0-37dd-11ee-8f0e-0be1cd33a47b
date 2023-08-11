# Robert L Grant, Vari M Drennan, Greta Rait, Irene Petersen, Steve Iliffe, 2023.

import sys, csv, re

codes = [{"code":"8H7w.00","system":"readv2"},{"code":"8HR6.00","system":"readv2"},{"code":"8HTX.00","system":"readv2"},{"code":"ZL62400","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('incontinence-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["referral-incontinence---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["referral-incontinence---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["referral-incontinence---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)