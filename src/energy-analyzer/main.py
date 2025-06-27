import json
import os

# Defining the input and Ouput file path
INPUT_FILE = '../../data/output1.json'
OUTPUT_FILE = '../../data/output2.json'

#Updates the input file to new list with additional fields
def analyze_energy_data(data):
    results = []
    for row in data:
        try:
            power = float(row["power_consumption"])
            voltage = float(row["voltage"])
            current = float(row["current"])

            efficiency = (power / (voltage * current)) * 100
            status = "high_usage" if power > 5.0 else "normal"
            anomaly_detected = power > 5.0

            processed_entry = {
                "timestamp": row["timestamp"],
                "household_id": row["household_id"],
                "power": power,
                "efficiency": round(efficiency, 3),
                "status": status,
                "anomaly_detected": anomaly_detected
            }

            results.append(processed_entry)

        except Exception as e:
            # Stop and raise a clear error if the data is missing or wrong
            raise RuntimeError(f"Error while processing row: {row}\nDetails: {e}")

    return results

# This is the main function that the container will run
def main():
    # First, check if the input file actually exists
    if not os.path.exists(INPUT_FILE):
        print(f"Input file not found: {INPUT_FILE}")
        return  # Exit the function early if no input file

    # Open and read the JSON input file
    with open(INPUT_FILE, "r") as infile:
        raw_data = json.load(infile)  # This will be a list of dictionaries

    # Process the data using our custom function
    processed_data = analyze_energy_data(raw_data)

    # Open the output file for writing the processed data
    with open(OUTPUT_FILE, "w") as outfile:
        json.dump(processed_data, outfile, indent=2)  # Save as pretty-printed JSON

    # Print confirmation message
    print(f"Container 2: Processed {len(processed_data)} records")

# Python will call main() automatically when this script is run directly
if __name__ == "__main__":
    main()