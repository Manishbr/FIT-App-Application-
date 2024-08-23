import os
import pandas as pd
from sklearn.model_selection import train_test_split

main_dir = os.path.expanduser("~/Desktop/DataPaper")
output_dir_train = os.path.expanduser("~/Desktop/ActivityScore/Train")
output_dir_test = os.path.expanduser("~/Desktop/ActivityScore/Test")

if not os.path.exists(output_dir_train):
    os.makedirs(output_dir_train)
if not os.path.exists(output_dir_test):
    os.makedirs(output_dir_test)

if not os.path.exists(main_dir):
    print(f"The directory {main_dir} does not exist.")
else:
    print(f"Files in {main_dir}:")
    for file_name in os.listdir(main_dir):
        print(file_name)

# Here we have defined the scoreing system.
scoring_system = {
    1: 50,  # Sleeping
    2: 25,  # Laying Down
    3: -5,  # Sitting
    4: 20,  # Light Movement
    5: 30,  # Medium Movement
    6: -20,  # Heavy Movement
    7: 20,  # Eating
    8: -20,  # Small Screen Usage
    9: -10,  # Large Screen Usage
    10: -5,  # Caffeinated Drink Consumption
    11: -50,  # Smoking
    12: -35  # Alcohol Consumption
}

activity_descriptions = {
    1: "Sleeping",
    2: "Laying Down",
    3: "Sitting",
    4: "Light Movement",
    5: "Medium Movement",
    6: "Heavy Movement",
    7: "Eating",
    8: "Small Screen Usage",
    9: "Large Screen Usage",
    10: "Caffeinated Drink Consumption",
    11: "Smoking",
    12: "Alcohol Consumption"
}

def calculate_duration_and_multiplier(row):
    try:
        duration_in_minutes = (pd.to_datetime(row['End']) - pd.to_datetime(row['Start'])).seconds / 60
        if duration_in_minutes <= 15:
            multiplier = 1
        else:
            multiplier = 1 + ((duration_in_minutes - 1) // 15) * 0.25
        return duration_in_minutes, multiplier
    except:
        return None, None

for user_num in range(1, 23):
    user_file = f"user_{user_num}_A.csv"
    user_path = os.path.join(main_dir, user_file)

    if os.path.isfile(user_path):
        df = pd.read_csv(user_path)

        df['Activity Description'] = df['Activity'].map(activity_descriptions)
        df['Scoring'] = df['Activity'].map(scoring_system)
        df[['Duration (mins)', 'Multiplier']] = df.apply(calculate_duration_and_multiplier, axis=1, result_type='expand')
        df.dropna(subset=['Duration (mins)', 'Multiplier'], inplace=True)
        df['Base Score (50 to -50)'] = df['Scoring']
        df['Total Score'] = df['Base Score (50 to -50)'] * df['Multiplier']
        df['Recovery'] = df['Total Score'].apply(lambda x: x if x > 0 else 0)
        df['Training/Health Damage'] = df['Total Score'].apply(lambda x: x if x < 0 else 0)
        if 'Index' not in df.columns:
            df.insert(0, 'Index', range(1, len(df) + 1))
        df = df[['Index', 'Activity', 'Scoring', 'Activity Description', 'Start', 'End', 'Day',
                 'Duration (mins)', 'Multiplier', 'Base Score (50 to -50)',
                 'Recovery', 'Training/Health Damage', 'Total Score']]
        totals_by_day = df.groupby('Day').agg({
            'Total Score': 'sum',
            'Recovery': 'sum',
            'Training/Health Damage': 'sum'
        }).reset_index()
        totals_by_day['Efficiency'] = ((totals_by_day['Recovery'] /
                                        (totals_by_day['Recovery'] - totals_by_day[
                                            'Training/Health Damage'])) * 100).fillna(0).round()
        totals = []
        for index, row in totals_by_day.iterrows():
            totals.append(pd.DataFrame({
                'Index': [f"Day {int(row['Day'])} Total", f"Day {int(row['Day'])} Efficiency"],
                'Total Score': [row['Total Score'], row['Efficiency']],
                'Recovery': [row['Recovery'], ''],
                'Training/Health Damage': [row['Training/Health Damage'], ''],
                'Multiplier': ['', ''],
                'Activity': ['', ''],
                'Scoring': ['', ''],
                'Activity Description': ['', ''],
                'Duration (mins)': ['', ''],
                'Base Score (50 to -50)': ['', '']
            }))
        df = pd.concat([df] + totals, ignore_index=True)
        train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
        output_file_path_train = os.path.join(output_dir_train, f"{user_file}_train.csv")
        train_df.to_csv(output_file_path_train, index=False)
        output_file_path_test = os.path.join(output_dir_test, f"{user_file}_test.csv")
        test_df.to_csv(output_file_path_test, index=False)

print("Processing complete. Training and testing files saved in the 'ActivityScore/Train' and 'ActivityScore/Test' folders on your desktop.")
