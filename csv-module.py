# The `csv` module in Python provides functionality to read from and write to CSV (Comma Separated Values) files.
# CSV is a common format for storing tabular data, where each line represents a row of data, and values within the row are separated by commas.

# Let's go through a basic tutorial on using the `csv` module:

### Reading CSV Files:

import csv

# Specify the path to your CSV file
csv_file_path = 'example.csv'

# Open the CSV file for reading
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Each 'row' is a list of values in that row
        print(row)


#### Reading with DictReader:
# If your CSV file has a header row (the first row with column names), you can use `DictReader` to read the data into dictionaries, where keys are column names:
# This method is my favourite

import csv
csv_file_path = 'example.csv'
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object using DictReader
    csv_reader = csv.DictReader(file)

    # Iterate through each row as a dictionary
    for row in csv_reader:
        # Access values using column names
        print(row['Column1'], row['Column2'])


### Writing to CSV Files:


import csv

# Specify the path to your CSV file for writing
csv_file_path = 'output.csv'

# Sample data to be written
data_to_write = [
    ['Name', 'Age', 'City'],
    ['John', 25, 'New York'],
    ['Jane', 30, 'San Francisco'],
    ['Bob', 22, 'Los Angeles']
]

# Open the CSV file for writing
with open(csv_file_path, 'w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)

    # Write data to the CSV file
    csv_writer.writerows(data_to_write)

# NOTE: If a file already contains some data that data will be overwritten when you use the 'w' flag so ... 
# ... if you wish to keep existing data while adding new data it is best to use the 'a' flag

#### Writing with DictWriter:
import csv
csv_file_path = 'output_dict.csv'

# Sample data to be written
data_to_write = [
    {'Name': 'John', 'Age': 25, 'City': 'New York'},
    {'Name': 'Jane', 'Age': 30, 'City': 'San Francisco'},
    {'Name': 'Bob', 'Age': 22, 'City': 'Los Angeles'}
]

# Specify field names (column names)
field_names = ['Name', 'Age', 'City']

with open(csv_file_path, 'w', newline='') as file:
    # Create a CSV writer object using DictWriter
    csv_writer = csv.DictWriter(file, fieldnames=field_names)

    # Write the header
    csv_writer.writeheader()

    # Write data to the CSV file
    csv_writer.writerows(data_to_write)


# Remember to replace the file paths and sample data with your actual data. The `newline=''` argument in `open()` is important for cross-platform compatibility.
# It ensures that newline characters are handled correctly when writing to the file.
