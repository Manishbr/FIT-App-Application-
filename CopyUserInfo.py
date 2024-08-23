import os
import pandas as pd

data_paper_path = os.path.expanduser("~/Desktop/DataPaper/")
output_dir = os.path.expanduser("~/Desktop/ID/")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# List all CSV files in the DataPaper folder
csv_files = [f for f in os.listdir(data_paper_path) if f.endswith('.csv')]

# Process each CSV file... FUN right!!!
for csv_file in csv_files:
    input_file_path = os.path.join(data_paper_path, csv_file)
    output_file_path = os.path.join(output_dir, csv_file)
    df = pd.read_csv(input_file_path)
    print(f"Processing {csv_file}")
    print(df.head())
    df.to_csv(output_file_path, index=False)

print("Processing complete. Files saved in the 'ID' folder on your desktop.")
