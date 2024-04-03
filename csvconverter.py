import csv

class CSVFormatter:

    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename

    def transform_to_csv(self):
        with open(self.input_filename, 'r') as infile:
            with open(self.output_filename, 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                for line in infile:
                    line = line.replace("\n", "")
                    if len(line) == 0:
                        continue
                    if "-+-" in line:
                        continue
                    if " rows)" in line:
                        continue
                    # Split each line using pipe (|) as separator
                    columns = line.strip().split('|')
                    # Remove any leading/trailing spaces in each column and write to CSV
                    writer.writerow([column.strip() for column in columns])
    
if __name__ == "__main__":
    input_file = input("Enter input file name: ")
    output_file = input("Enter output file name: ")

    formatter = CSVFormatter(input_file, output_file)
    formatter.transform_to_csv()
    print("Conversion complete.")

