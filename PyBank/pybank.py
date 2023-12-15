import os
import csv

#setting the path
csvpath = os.path.join("Resources", "budget_data.csv")

#reading the csvfile 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader) #skip the header line
    
    #initialize the variables 
    count=0
    total=0
    date_list = []
    profit_loss_list = []
    change_list = []

    #read each row of the csv one by one
    for row in csvreader:
        date_list.append(row[0]) #append column 1 information into the date_list list
        profit_loss_list.append(row[1]) #append column 2 information into the profit_loss_list list
        count = count + 1 #increment the count everytime to get the total months
        total = total + int(row[1]) #get the total profit/loss amount
        
    change_list.append(0) #list to get the change from one month to the next, adding a 0 to the beginning because we want to keep the rows consistent
    for i in range(count - 1): # loop through 0 to count - 1 rows (count is the total number of rows in the csv)
        if int(profit_loss_list[i+1]) < int(profit_loss_list[i]): #check to see if the next element in the list is less than the current element. If its less, then its a loss and the difference should be negative
            change_temp = abs(int(profit_loss_list[i + 1]) - int(profit_loss_list[i]))
            change = 0 - change_temp #change the number to negative 
        else:
            change = abs(int(profit_loss_list[i + 1]) - int(profit_loss_list[i]))
        change_list.append(change)
            
    lengthChangeList = int(len(change_list)) 
    change_total = 0
    for change in change_list:
        change_total = change + change_total #get the total change for the profit/loss 
    average = change_total / (lengthChangeList - 1) # get the average change for each month. using length - 1 here because there is no change for the first month. We just added the 0 to keep the rows consistent
    
    budget_data_with_profit_loss_changes = zip(date_list, profit_loss_list, change_list) # zip all the lists together 
    
    #intialize the variables again for the greatest increase/decrease
    greatest_decrease = 0 
    greatest_decrease_list = []
    greatest_increase = 0
    greatest_increase_list = []
    for change in budget_data_with_profit_loss_changes:
            if int(change[2]) > greatest_increase: #figure out the greatest increase - set greatest_increase everytime we find a new elemetn that's greater than the previous
                greatest_increase = change[2]
                greatest_increase_list.append(change) #append everything to the greatest_increase_list (this grabs information from all 3 columns) 
            if int(change[2]) < greatest_decrease: #do the same for the greatest decrease - set greatest_decrese everytime we find a new leemetn that's less than the previous
                greatest_decrease = change[2]
                greatest_decrease_list.append(change) #append everything to the greatest_decrease_list (this grabs information from all 3 columns)
    lengthGreatestIncreaseList = len(greatest_increase_list) # get the length for the greatest_increase_list
    lengthGreatestDecreaseList = len(greatest_decrease_list) # get lenght for the greatest_decrease_list
    
    #opening the analysis text file and printing the results to the file
with open ("analysis/pybank_analysis.txt", 'w') as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------\n")
    text.write(f"Total Months: {count}\n") #total months 
    text.write(f"Total: ${total}\n")  #total profit/loss
    text.write(f"Average Change: ${round(average,2)}\n") #total average profit/loss 
    text.write(f"Greatest Increase in Profits: {greatest_increase_list[lengthGreatestIncreaseList - 1][0]} (${greatest_increase_list[lengthGreatestIncreaseList - 1][2]})\n") #greatest increase we print the last element in the list, because that's the greatest value for increase
    text.write(f"Greatest Increase in Profits: {greatest_decrease_list[lengthGreatestDecreaseList - 1][0]} (${greatest_decrease_list[lengthGreatestDecreaseList - 1][2]})\n") #greatest decrease we print the last element in the list, because that's the least value for decrease. 
text.close() # close the text file we write to 
csvfile.close() #close the csv file we read from 