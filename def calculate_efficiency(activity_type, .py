def calculate_efficiency(activity_type, duration_minutes):

    scoring_system = {
        'Sleeping': 50,
        'Laying Down': 25,
        'Sitting': -5,
        'Light Movement': 20,
        'Medium Movement': 30,
        'Heavy Movement': -20,
        'Eating': 20,
        'Small Screen Usage': -20,
        'Large Screen Usage': -10,
        'Caffeinated Drink Consumption': -5,
        'Smoking': -50,
        'Alcohol Consumption': -35
    }

    base_score = scoring_system.get(activity_type, 0)
    multiplier = 1 + (duration_minutes - 1) // 15 * 0.25
    total_score = base_score * multiplier
    return total_score

def main():
    print("Activity Efficiency Calculator")
    total_recovery_score = 0
    total_damage_score = 0

    while True:
        activity_type = input("Enter the activity type (or 'done' to finish): ")
        if activity_type.lower() == 'done':
            break

        duration = int(input("Enter the duration in minutes: "))
        score = calculate_efficiency(activity_type, duration)
        if score > 0:
            total_recovery_score += score
        else:
            total_damage_score += score

        print(f"Score for {activity_type} ({duration} minutes): {score:.2f}")
    total_score = total_recovery_score + total_damage_score
    efficiency_percentage = (total_recovery_score / total_score) * 100 if total_score != 0 else 0
    
    print("\nFinal Results:")
    print(f"Total Recovery Score: {total_recovery_score:.2f}")
    print(f"Total Damage Score: {total_damage_score:.2f}")
    print(f"Overall Efficiency: {efficiency_percentage:.2f}%")

if __name__ == "__main__":
    main()
