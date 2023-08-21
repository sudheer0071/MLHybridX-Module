import sys
import csv

def check_file(file_name):
     try:
            with open(f'{file_name}') as file:
                read_data = list(csv.DictReader(file))
                return read_data 
     except FileNotFoundError:
        return False
