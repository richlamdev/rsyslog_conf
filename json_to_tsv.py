#!/bin/usr/python

# Richard Lam, September 2019
#
# Script to convert rsyslog lookup table JSON format file to TSV format
#
# Reference:
# https://www.rsyslog.com/doc/master/configuration/lookup_tables.html


import sys
import json
import csv

argc = len(sys.argv)

if argc < 2:
    print ("usage: python json_to_tsv.py <name of input file>")
    sys.exit();
else:
    in_file = sys.argv[1]

with open(in_file, 'r') as jsonfile:
    readjson = jsonfile.readlines()

# remove top four lines - rsyslog header lookup table info
# and bottom line - closing brace of rsyslog header
tempbuff1 = readjson[4:]
tempbuff2 = tempbuff1[:-1]

# write to file as json without rsyslog info
with open(in_file + ".txt", 'w') as jsonfile:
    jsonfile.writelines(tempbuff2)

# read back as json data via json.load
with open(in_file + ".txt", 'r') as jsonfile:
    jsondata = json.load(jsonfile)    

# write data to file as TSV
with open(in_file + ".txt", 'w') as tsvfile:
    tsvwrite = csv.DictWriter(tsvfile, sorted(jsondata[0].keys()), delimiter='\t', lineterminator='\n')
    tsvwrite.writeheader()
    tsvwrite.writerows(jsondata)

print ("output file is:" + in_file + ".txt")
