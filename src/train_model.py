import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# ============================================================
# LOAD DATASET
# ============================================================
df = pd.read_csv("data/elective_recommendation_students.csv")

# ============================================================
# FEATURES
# ============================================================
feature_columns = [
    "programming_score",
    "mathematics_score",
    "database_score",
    "ai_score",
    "ml_score",
    "web_score",
    "data_science_score",
    "interest_ai",
    "interest_web",
    "interest_data",
    "interest_programming",
    "interest_cloud",
    "interest_security"
]

X = df[feature_columns]

# ============================================================
# TARGET
# ============================================================
y = df["preferred_elective"]

# ============================================================
# ENCODE TARGET
# ============================================================
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# ============================================================
# TRAIN / TEST SPLIT
# ============================================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)

# ============================================================
# MODEL DEFINITIONS
# ============================================================
models = {
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=2000, random_state=42))
    ]),
    "Random Forest": RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42)
}

results = {}

print("=" * 80)
print("MODEL TRAINING & EVALUATION")
print("=" * 80)

for name, model in models.items():
    print(f"\nTraining {name} ...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average='macro', zero_division=0)
    rec = recall_score(y_test, y_pred, average='macro', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='macro', zero_division=0)

    results[name] = {
        "model": model,
        "accuracy": acc,
        "precision": prec,
        "recall": rec,
        "f1": f1,
        "predictions": y_pred
    }

    print(f"{name} -> Accuracy: {acc:.4f}  Precision: {prec:.4f}  Recall: {rec:.4f}  F1: {f1:.4f}")

# ============================================================
# COMPARISON TABLE
# ============================================================
print("\n" + "=" * 80)
print("MODEL COMPARISON")
print("=" * 80)
print(f"{'Model':<22} {'Accuracy':>10} {'Precision':>10} {'Recall':>10} {'F1':>10}")
print("-" * 80)
for name, metrics in results.items():
    print(f"{name:<22} {metrics['accuracy']:>10.4f} {metrics['precision']:>10.4f} {metrics['recall']:>10.4f} {metrics['f1']:>10.4f}")

# ============================================================
# SELECT BEST MODEL (by macro F1)
# ============================================================
best_name = max(results, key=lambda k: results[k]['f1'])
best_model = results[best_name]['model']
print(f"\nBest model (macro F1): {best_name}")

# ============================================================
# DETAILED REPORT FOR BEST MODEL
# ============================================================
print("\n" + "=" * 80)
print(f"DETAILED CLASSIFICATION REPORT - {best_name}")
print("=" * 80)
print(classification_report(
    y_test,
    results[best_name]['predictions'],
    target_names=label_encoder.classes_,
    zero_division=0
))

# ============================================================
# FEATURE IMPORTANCE / COEFFICIENTS
# ============================================================
print("\n" + "=" * 80)
print("FEATURE IMPORTANCE / COEFFICIENTS")
print("=" * 80)

if hasattr(best_model, "named_steps"):
    # Pipeline case (Logistic Regression)
    clf = best_model.named_steps.get('clf', None)
    scaler = best_model.named_steps.get('scaler', None)
    if clf is not None and hasattr(clf, "coef_"):
        coef_df = pd.DataFrame(clf.coef_, columns=feature_columns, index=label_encoder.classes_)
        print("Logistic Regression coefficients (per class):")
        print(coef_df.round(4))
elif hasattr(best_model, "feature_importances_"):
    # Tree based
    importances = pd.Series(best_model.feature_importances_, index=feature_columns).sort_values(ascending=False)
    print("Feature importances:")
    print(importances.round(4))
else:
    print("No feature importance available for this model.")

# ============================================================
# SAVE BEST MODEL & ENCODER
# ============================================================
joblib.dump(best_model, "models/elective_recommendation_model.pkl")
joblib.dump(label_encoder, "models/label_encoder.pkl")
print("\nSaved best model to models/elective_recommendation_model.pkl")
print("Saved label encoder to models/label_encoder.pkl")
print("\nTraining completed successfully.")