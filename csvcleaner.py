import csv
import os
import shutil
import sys

class CSVCleaner:

    def __init__(self, input_filename, output_filename, columns_to_remove):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.columns_to_remove = columns_to_remove

    def remove_columns(self):
        with open(self.input_filename, 'r') as infile, open(self.output_filename, 'w', newline='') as outfile:
            reader = csv.DictReader(infile, delimiter=";")
            headers = reader.fieldnames
            filtered_headers = [header for header in headers if header not in self.columns_to_remove]
            writer = csv.DictWriter(outfile, delimiter=";", fieldnames=filtered_headers, quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            for row in reader:
                filtered_row = {header: row[header] for header in filtered_headers}
                writer.writerow(filtered_row)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script_name.py input_file column1_name column2_name ...")
        sys.exit(1)
    output_file = sys.argv[1]
    input_file = output_file + "-tmp"
    columns_to_remove = sys.argv[2:]

    shutil.copyfile(output_file, input_file)

    #input_file = '/Users/sergio.lema/ekino/data/ws/hcp/scripts/dumps/skin_backup_backup.csv'
    #output_file = '/Users/sergio.lema/ekino/data/ws/hcp/scripts/dumps/skin_backup.csv'
    #columns_to_remove = ["tank_number", "container", "real_container"]

    cleaner = CSVCleaner(input_file, output_file, columns_to_remove)
    cleaner.remove_columns()

    os.remove(input_file)

    print("Columns removed successfully.")

