import os
import pandas as pd

main_dir = os.path.expanduser("~/Desktop/DataPaper")
output_dir = os.path.expanduser("~/Desktop/SleepData")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process each user's sleep.csv file
for user_num in range(1, 23):
    user_file = f"sleep_data_{user_num}.csv"
    user_path = os.path.join(main_dir, user_file)

    if os.path.isfile(user_path):
        df = pd.read_csv(user_path)
        extracted_df = df[['In Bed Time', 'Efficiency', 'Total Minutes in Bed', 'Number of Awakenings']].copy()
        extracted_df['Efficiency'] = extracted_df['Efficiency'].round()
        extracted_df.insert(1, 'Day', extracted_df['In Bed Time'].apply(lambda x: 2 if 1 == 1 else 1))
        output_file_path = os.path.join(output_dir, user_file)
        extracted_df.to_csv(output_file_path, index=False)

print("Processing complete. Files saved in the 'SleepData' folder on your desktop.")
