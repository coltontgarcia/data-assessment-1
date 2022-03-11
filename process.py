log_file = open("um-server-01.txt") # opens the file "um-server-01.txt"


def sales_reports(log_file): # makes a function with log-file as the parameter
    for line in log_file: # essentially a for loop
        line = line.rstrip() # removes line ending in string
        day = line[0:3] # takes the first three characters of the line
        if day == "Mon": # checks the first three chars, and if they are equal to a certain value
            print(line) # console.log for python

sales_reports(log_file) # Calls the function defined above passing through the log_file var set on line 1.
