import os, json, yaml
import pandas as pd
from datetime import datetime

with open("config.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

NAME = cfg["name"]
CREATOR = cfg["creator"]
INITIAL_CREATION_DATE = cfg["initial-creation-date"]

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Read the CSV files from the "raw" folder
df = pd.read_csv(os.path.join(script_dir, "input", "trailblazer.csv"))

# Convert the 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")

# Sort the dataframe by date in ascending order
df = df.sort_values("Date", ascending=True)

json_entries = []  # List to store JSON entries

for index, row in df.iterrows():
    # Convert the date format to ISO format
    date_iso = row["Date"].isoformat() + "Z"

    entry = {
        "category": row["Content Pillar"],
        "date": date_iso,
        "title": row["Event"],
        "link": row["Social Media Link"],
    }
    json_entries.append(entry)

current_date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

# Check if the {NAME}.json file exists in the output folder
if os.path.exists(os.path.join(script_dir, "output", f"{NAME}.json")):
    # Read the output/trailblazer.json file
    with open(os.path.join(script_dir, "output", f"{NAME}.json")) as file:
        current_trailblazer = json.load(file)
else:
    current_trailblazer = {"data": ""}

# Check if current_trailblazer["data"] is different from json_entries
if current_trailblazer["data"] == json_entries:
    print("No changes detected.")
else:
    json_data = {
        "data_stream": {
            "name": NAME,
            "creator": CREATOR,
            "created_on": INITIAL_CREATION_DATE,
            "last_modified_on": current_date,
        },
        "data": json_entries,
    }

    # Convert JSON data to a string
    json_string = json.dumps(json_data)

    # Define the output file path in the script's directory
    output_file = os.path.join(script_dir, f"output/{NAME}.json")

    # Write JSON data to file
    with open(output_file, "w") as file:
        json.dump(json_data, file, indent=4)

    print(f"JSON file created: {output_file}")
