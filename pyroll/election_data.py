# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:41:33 2021

@author: memeg
"""

import csv


import os
# Store the file path associated with the file (note the backslash may be OS specific)
file = 'election_data.csv'


# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    # This stores a reference to a file stream
    print(text)

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)
    
    
    
os.chdir(os.path.dirname(__file__))

election_data_csv_path = os.path.join("election_data.csv")

# Open the CSV
with open(election_data_csv_path, newline="") as csvfile:


    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvfile)

    # This prints Header: Date, Profit/Losses
    print(f"Header: {csv_header}")
    
    
             


        