import csv

# Open the input CSV file
with open('./data/raw_close.csv', 'r') as input_file:
  # Create a CSV reader object
  reader = csv.reader(input_file)

  # Read the header row
  header = next(reader)

  # Find the index of the "code" column
  code_index = header.index("Code")

  # Sort the rows by the "code" column
  sorted_rows = sorted(reader, key=lambda row: row[code_index])

# Open the output CSV file
with open('./data/data_close.csv', 'w') as output_file:
  # Create a CSV writer object
  writer = csv.writer(output_file)

  # Write the header row
  writer.writerow(header)

  # Write the sorted rows
  writer.writerows(sorted_rows)
  
# EOF - Final
