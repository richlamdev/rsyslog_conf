#!/bin/usr/python

# Richard Lam, September 2019
#
# Script to convert TSV format file to rsyslog lookup table JSON format 
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


header_data = '{ "version": 1,\n  "nomatch": "unknown",\n  "type": "string",\n  "table": \n' 
data=[]

# read in data and convert to JSON
with open(in_file,"r") as tsvfile, open(in_file+".json","w") as jsonfile:
    reader = csv.DictReader(tsvfile, dialect='excel-tab')
    for row in reader:
        data.append(row)
    jsonfile.write('[' +
                   ', \n'.join(json.dumps(i) for i in data) +
                   ']\n}\n')

# read in json data temporarily
with open(in_file + ".json","r") as jsonfile:
    readjson = jsonfile.read()

# concat the rsyslog header information with the json data and write to file
with open(in_file + ".json","w") as jsonfile:
    jsonfile.write(header_data) 
    jsonfile.write(readjson)

print ("Output file is: " + in_file + ".json")
