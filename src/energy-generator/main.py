import csv
import json
import os  

# This function reads the energy data from the CSV file
def read_energy_data():
    # The path to CSV File
    csv_path = '../../data/sample_energy_data.csv'

    # Checks if the CSV file exists
    if not os.path.exists(csv_path):
        # Show an error and stop execution if file doesn't exist
        raise FileNotFoundError(f" The CSV file was not found at: {csv_path}")

    # Open the CSV file and read its contents
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        return data

# Main function
def main():
    try:
        # Call the function to read data from CSV
        data = read_energy_data()

        # Save the data into a JSON file
        with open('../../data/output1.json', 'w') as json_file:
            json.dump(data, json_file, indent=2) 

        print("Container 1: Generated", len(data), "records.")

    except FileNotFoundError as e:
        # Catch the error and print it
        print(e)

# This makes sure the main function runs when the script is executed
if __name__ == "__main__":
    main()