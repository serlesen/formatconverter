import csv
import sys

class SQLConverter:

    def __init__(self, input_filename, output_filename, table_name):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.table_name = table_name

    def read_csv_with_pipes(self):
        data = []
        with open(self.input_filename, 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                data.append([value.strip() for value in row])
        return data
    
    def generate_sql_insert(self, columns, values):
        sql = f"INSERT INTO {self.table_name} ({', '.join(columns)})\nVALUES\n"
        for value_set in values:
            formatted_values = ', '.join([f"'{value}'" for value in value_set])
            sql += f"({formatted_values}),\n"
        # Remove the trailing comma and add a semicolon
        sql = sql[:-2] + ';\n'
        return sql
    
    def convert(self):
        data = self.read_csv_with_pipes()
    
        header = data[0]
        values = data[2:-1]  # Exclude header, dashed line, and count
    
        sql_script = self.generate_sql_insert(header, values)
    
        with open(self.output_filename, 'w') as f:
            f.write(sql_script)
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py input_file table_name")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = input_file + ".sql"
    table_name = sys.argv[2]

    converter = SQLConverter(input_file, output_file, table_name)
    converter.convert()

    print("SQL script created successfully")
