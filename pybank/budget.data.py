# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:50:15 2021

@author: memeg
"""

import csv


import os
# Store the file path associated with the file (note the backslash may be OS specific)
file =  os.path.join("Resources","budget_data.csv")


# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    # This stores a reference to a file stream
    print(text)

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    # Print the contents of the text file
    print(lines)
    
# Create a Python script for analyzing the financial records of your company.
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv).
# The dataset is composed of two columns: `Date` and `Profit/Losses)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period


# variables 
months = []

profit_loss_changes = []

count_months = 0

net_profit_loss = 0

previous_month_profit_loss = 0

current_month_profit_loss = 0

profit_loss_change = 0

#change directory of current script and folder to collect data

#os.chdir(os.path.dirname(__file__))

budget_data_csv_path = os.path.join(file)

# Open the CSV
with open(budget_data_csv_path, newline="") as csvfile:


    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvfile)

    # This prints Header: Date, Profit/Losses
    print(f"Header: {csv_header}")
    
             
    # Read through each row of data after the header
    for row in csv_reader:


    # Count of months
        count_months += 1


    # Net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss


        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue


        else:


     # Compute change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss


     # Append each month to the months[]
            months.append(row[0])


     # Append each profit_loss_change to the profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)


     # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss


    #sum and average of the changes in "Profit/Losses" over the entire period
        sum_profit_loss = sum(profit_loss_changes)
        average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)


    # highest and lowest changes in "Profit/Losses" over the entire period
        highest_change = max(profit_loss_changes)
        lowest_change = min(profit_loss_changes)


    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
        highest_month_index = profit_loss_changes.index(highest_change)
        lowest_month_index = profit_loss_changes.index(lowest_change)


    # Assign best and worst month
        best_month = months[highest_month_index]
        worst_month = months[lowest_month_index]


# Print analysis
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months:  {count_months}")
    print(f"Total:  ${net_profit_loss}")
    print(f"Average Change:  ${average_profit_loss}")
    print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
    print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


budget_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as outfile:


    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")

