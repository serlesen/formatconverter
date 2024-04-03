import csv
import os
import shutil
import sys

class CSVColumnSwap:

    def __init__(self, input_filename, output_filename, first_column, second_column):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.first_column = first_column
        self.second_column = second_column

    def swap_columns(self):
        print(f"from {self.input_filename} to {self.output_filename}")
        with open(self.input_filename, 'r') as infile, open(self.output_filename, 'w', newline='') as outfile:
            reader = csv.DictReader(infile, delimiter=";")
            headers = reader.fieldnames
            if column1_name not in headers or column2_name not in headers:
                print("One or both of the specified column names not found.")
                return
            new_headers = headers[:]
            index1 = new_headers.index(self.first_column)
            index2 = new_headers.index(self.second_column)
            new_headers[index1], new_headers[index2] = new_headers[index2], new_headers[index1]
            writer = csv.DictWriter(outfile, delimiter=";", fieldnames=new_headers)
            writer.writeheader()
            for row in reader:
#                row[self.first_column], row[self.second_column] = row[self.second_column], row[self.first_column]
                writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py input_file column1_name column2_name")
        sys.exit(1)
    output_file = sys.argv[1]
    input_file = output_file + "-tmp"
    column1_name = sys.argv[2]
    column2_name = sys.argv[3]

    shutil.copyfile(output_file, input_file)

    #input_file = 'input.csv'  # Change this to your input CSV file path
    #output_file = 'output.csv'  # Change this to your output CSV file path
    #column1_name = 'Column1'  # Change this to the name of the first column to swap
    #column2_name = 'Column2'  # Change this to the name of the second column to swap

    swapper = CSVColumnSwap(input_file, output_file, column1_name, column2_name)
    swapper.swap_columns()

    os.remove(input_file)

    print("Columns and headers swapped successfully.")

