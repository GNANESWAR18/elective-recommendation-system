import numpy as np
import pandas as pd

def generate_dataset(n_samples=1000, random_state=42):
    rng = np.random.default_rng(random_state)

    # Generate base academic scores (0-100)
    programming_score = rng.normal(70, 15, n_samples).clip(0, 100)
    mathematics_score = rng.normal(70, 15, n_samples).clip(0, 100)
    database_score = rng.normal(65, 15, n_samples).clip(0, 100)
    ai_score = rng.normal(60, 20, n_samples).clip(0, 100)
    ml_score = rng.normal(60, 20, n_samples).clip(0, 100)
    web_score = rng.normal(65, 15, n_samples).clip(0, 100)
    data_science_score = rng.normal(60, 20, n_samples).clip(0, 100)

    # Interests 1-5
    interest_ai = rng.integers(1, 6, n_samples)
    interest_web = rng.integers(1, 6, n_samples)
    interest_data = rng.integers(1, 6, n_samples)
    interest_programming = rng.integers(1, 6, n_samples)
    interest_cloud = rng.integers(1, 6, n_samples)
    interest_security = rng.integers(1, 6, n_samples)

    # Compute propensity scores for each elective
    # Higher propensity -> more likely chosen
    prop = {}

    # Artificial Intelligence
    prop['Artificial Intelligence'] = (
        0.35 * (ai_score / 100) +
        0.25 * (ml_score / 100) +
        0.20 * (mathematics_score / 100) +
        0.15 * (interest_ai / 5) +
        0.05 * rng.normal(0, 0.1, n_samples)
    )

    # Machine Learning
    prop['Machine Learning'] = (
        0.35 * (ml_score / 100) +
        0.25 * (programming_score / 100) +
        0.20 * (mathematics_score / 100) +
        0.10 * (interest_ai / 5) +
        0.10 * (interest_programming / 5) +
        0.05 * rng.normal(0, 0.1, n_samples)
    )

    # Data Science
    prop['Data Science'] = (
        0.35 * (data_science_score / 100) +
        0.25 * (mathematics_score / 100) +
        0.20 * (database_score / 100) +
        0.15 * (interest_data / 5) +
        0.05 * rng.normal(0, 0.1, n_samples)
    )

    # Web Development
    prop['Web Development'] = (
        0.40 * (web_score / 100) +
        0.30 * (programming_score / 100) +
        0.20 * (interest_web / 5) +
        0.10 * (interest_programming / 5) +
        0.05 * rng.normal(0, 0.1, n_samples)
    )

    # Cloud Computing
    prop['Cloud Computing'] = (
        0.35 * (programming_score / 100) +
        0.30 * (interest_cloud / 5) +
        0.20 * (database_score / 100) +
        0.10 * (web_score / 100) +
        0.05 * rng.normal(0, 0.1, n_samples)
    )

    # Cyber Security
    prop['Cyber Security'] = (
        0.35 * (programming_score / 100) +
        0.30 * (interest_security / 5) +
        0.20 * (database_score / 100) +
        0.10 * (mathematics_score / 100) +
        0.05 * rng.normal(0, 0.1, n_samples)
    )

    # Convert prop dict to DataFrame
    prop_df = pd.DataFrame(prop)

    # Choose elective with highest propensity
    preferred = prop_df.idxmax(axis=1)

    # Build final DataFrame
    df = pd.DataFrame({
        'student_id': [f"S{str(i+1).zfill(4)}" for i in range(n_samples)],
        'programming_score': programming_score.round(1),
        'mathematics_score': mathematics_score.round(1),
        'database_score': database_score.round(1),
        'ai_score': ai_score.round(1),
        'ml_score': ml_score.round(1),
        'web_score': web_score.round(1),
        'data_science_score': data_science_score.round(1),
        'interest_ai': interest_ai,
        'interest_web': interest_web,
        'interest_data': interest_data,
        'interest_programming': interest_programming,
        'interest_cloud': interest_cloud,
        'interest_security': interest_security,
        'preferred_elective': preferred
    })

    return df


if __name__ == "__main__":
    df = generate_dataset()
    df.to_csv("data/elective_recommendation_students.csv", index=False)
    print(f"Generated {len(df)} records and saved to data/elective_recommendation_students.csv")
    print(df['preferred_elective'].value_counts())