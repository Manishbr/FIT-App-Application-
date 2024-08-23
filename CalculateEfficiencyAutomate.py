import pandas as pd

# Here we have defined the scoreing system.
scoring_system = {
    1: 50,   # Sleeping
    2: 25,   # Laying Down
    3: -5,   # Sitting
    4: 20,   # Light Movement
    5: 30,   # Medium Movement
    6: -20,  # Heavy Movement
    7: 20,   # Eating
    8: -20,  # Small Screen Usage
    9: -10,  # Large Screen Usage
    10: -5,  # Caffeinated Drink Consumption
    11: -50, # Smoking
    12: -35  # Alcohol Consumption
}

# calculate the efficiency for an activity
def calculate_efficiency(activity_type, duration_minutes):
    base_score = scoring_system.get(activity_type, 0)
    if duration_minutes <= 15:
        multiplier = 1
    else:
        multiplier = 1 + ((duration_minutes - 1) // 15) * 0.25
    total_score = base_score * multiplier
    return total_score

def main():
    df = pd.read_csv('test.csv')
    print("Activity Efficiency Calculator")
    total_recovery_score = 0
    total_damage_score = 0

    for index, row in df.iterrows():
        activity_type = row['Activity Type']
        duration = row['Duration (minutes)']
        score = calculate_efficiency(activity_type, duration)
        if score > 0:
            total_recovery_score += score
        else:
            total_damage_score += score
        print(f"Score for activity type {activity_type} ({duration} minutes): {score:.2f}")

    total_score = total_recovery_score + abs(total_damage_score)
    efficiency_percentage = (total_recovery_score / total_score) * 100 if total_score != 0 else 0

    print("\nFinal Results:")
    print(f"Total Recovery Score: {total_recovery_score:.2f}")
    print(f"Total Damage Score: {total_damage_score:.2f}")
    print(f"Overall Efficiency: {efficiency_percentage:.2f}%")

if __name__ == "__main__":
    main()
