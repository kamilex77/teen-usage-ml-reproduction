import pandas as pd
import numpy as np
from pathlib import Path

file_id = "1mJ-iLbHWiaPLHltrnIwjfNcbtW_4u8fd"
url = f"https://drive.google.com/uc?export=download&id={file_id}"
df = pd.read_csv(url)

N_NEW = 500

def generate_synthetic_data(df, n_samples):
    synthetic_rows = []

    for _ in range(n_samples):
        row = {}

        row["Gender"] = np.random.choice(df["Gender"])
        row["School_Grade"] = np.random.choice(df["School_Grade"])
        row["Phone_Usage_Purpose"] = np.random.choice(df["Phone_Usage_Purpose"])
        row["Location"] = np.random.choice(df["Location"])

        # Age - generated with noise, clipped to 12-19
        row["Age"] = int(np.clip(np.random.normal(df["Age"].mean(), df["Age"].std()), 12, 19))

        # Generation of numeric columns with noise
        def noisy(col):
            return float(np.clip(
                np.random.normal(df[col].mean(), df[col].std()),
                df[col].min(),
                df[col].max()
            ))

        # Numeric columns - generated with noise
        numeric_cols = [
            'Daily_Usage_Hours', 'Sleep_Hours', 'Academic_Performance',
            'Social_Interactions', 'Exercise_Hours', 'Anxiety_Level',
            'Depression_Level', 'Self_Esteem', 'Parental_Control',
            'Screen_Time_Before_Bed', 'Phone_Checks_Per_Day',
            'Apps_Used_Daily', 'Time_on_Social_Media',
            'Time_on_Gaming', 'Time_on_Education',
            'Family_Communication', 'Weekend_Usage_Hours'
        ]

        for col in numeric_cols:
            row[col] = noisy(col)

        # Additction_Level - calculated based on a combination of factors + noise
        row["Addiction_Level"] = float(
            0.4 * row["Daily_Usage_Hours"] +
            0.3 * row["Phone_Checks_Per_Day"] / 50 +
            0.3 * row["Time_on_Social_Media"] +
            np.random.normal(0, 0.5)
        )

        row["Addiction_Level"] = np.clip(row["Addiction_Level"], 0, 10)

        synthetic_rows.append(row)

    return pd.DataFrame(synthetic_rows)


# Generation of synthetic data
synthetic_df = generate_synthetic_data(df, N_NEW)

# Adding synthetic IDs and Names
synthetic_df["ID"] = range(len(df) + 1, len(df) + len(synthetic_df) + 1)
synthetic_df["Name"] = ["Synthetic_" + str(i) for i in synthetic_df["ID"]]

# Merging original and synthetic data
synthetic_df = synthetic_df.round(1)

output_path = Path(__file__).resolve().parent / "new_records.csv"
synthetic_df.to_csv(output_path, index=False)

print(f"Completed! New records saved to {output_path}")
