import csv
import pandas

# pandas reads the csv file and organizes it in rows and columns with an index of the rows and a total count display.

result = pandas.read_csv('Sample500.csv')

"""
# Prints all results
print(result)

# Select specfic cell [row, column] using .iloc function
sr = result.iloc[100, 1]
print (sr)

# Select specfic rows using .iloc function
sr = result.iloc[100]
print (sr)

######################################
# Opens the csv file

with open('Sample500.csv', 'r') as csv_file:

    # Reads the csv file.

    reader = csv.reader(csv_file)

    # loop that reads each line/row and prints its contents one row at a time
    for row in reader:
        print(row) 
        
        
### 
# pandas basic importing functions 
# pd.read_csv(filename) | From a CSV file
# pd.read_table(filename) | From a delimited text file (like TSV)
# pd.read_excel(filename) | From an Excel file
# pd.read_sql(query, connection_object) | Read from a SQL table/database
# pd.read_json(json_string) | Read from a JSON formatted string, URL or file.
# pd.read_html(url) | Parses an html URL, string or file and extracts tables to a list of dataframes
# pd.read_clipboard() | Takes the contents of your clipboard and passes it to read_table()
# pd.DataFrame(dict) | From a dict, keys for columns names, values for data as lists        
      
        
        
        """

