import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from src.recommend import recommend

st.set_page_config(page_title="Elective Recommendation System", layout="centered")

# Load model & encoder (cached)
@st.cache_resource
def load_artifacts():
    model = joblib.load("models/elective_recommendation_model.pkl")
    encoder = joblib.load("models/label_encoder.pkl")
    return model, encoder

model, encoder = load_artifacts()

st.title("Elective Recommendation System")
st.markdown("**AI‑based elective recommendation using academic performance and student interests.**")

st.header("1. Student Academic Scores")
col1, col2 = st.columns(2)
with col1:
    programming_score = st.slider("Programming Score", 0, 100, 70)
    mathematics_score = st.slider("Mathematics Score", 0, 100, 70)
    database_score = st.slider("Database Score", 0, 100, 65)
    ai_score = st.slider("AI Score", 0, 100, 60)
with col2:
    ml_score = st.slider("ML Score", 0, 100, 60)
    web_score = st.slider("Web Score", 0, 100, 65)
    data_science_score = st.slider("Data Science Score", 0, 100, 60)

st.header("2. Student Interests (1‑5)")
col3, col4 = st.columns(2)
with col3:
    interest_ai = st.slider("AI Interest", 1, 5, 3)
    interest_web = st.slider("Web Development Interest", 1, 5, 3)
    interest_data = st.slider("Data Science Interest", 1, 5, 3)
    interest_programming = st.slider("Programming Interest", 1, 5, 3)
with col4:
    interest_cloud = st.slider("Cloud Computing Interest", 1, 5, 3)
    interest_security = st.slider("Cyber Security Interest", 1, 5, 3)

if st.button("Recommend Elective"):
    student = {
        "programming_score": programming_score,
        "mathematics_score": mathematics_score,
        "database_score": database_score,
        "ai_score": ai_score,
        "ml_score": ml_score,
        "web_score": web_score,
        "data_science_score": data_science_score,
        "interest_ai": interest_ai,
        "interest_web": interest_web,
        "interest_data": interest_data,
        "interest_programming": interest_programming,
        "interest_cloud": interest_cloud,
        "interest_security": interest_security
    }

    result = recommend(student)

    st.header("3. Recommendation Result")
    st.success(f"**Recommended Elective:** {result['top_elective']}")
    st.info(f"**Confidence:** {result['confidence']}%")

    st.subheader("Top 3 Recommendations")
    for i, (cls, prob) in enumerate(result["top3"], 1):
        st.write(f"{i}. **{cls}** — {prob}%")

    # Visualization
    st.subheader("Recommendation Probabilities")
    prob_df = pd.DataFrame({
        "Elective": list(result["all_probs"].keys()),
        "Probability (%)": list(result["all_probs"].values())
    }).sort_values("Probability (%)", ascending=True)

    fig = px.bar(prob_df, x="Probability (%)", y="Elective", orientation='h',
                 color="Probability (%)", color_continuous_scale="Blues")
    fig.update_layout(height=350, margin=dict(l=10, r=10, t=30, b=10))
    st.plotly_chart(fig, use_container_width=True)

    # Student Profile Summary
    st.header("4. Student Profile Summary")
    profile_df = pd.DataFrame({
        "Attribute": [
            "Programming Score", "Mathematics Score", "Database Score", "AI Score",
            "ML Score", "Web Score", "Data Science Score",
            "AI Interest", "Web Development Interest", "Data Science Interest",
            "Programming Interest", "Cloud Computing Interest", "Cyber Security Interest"
        ],
        "Value": [
            programming_score, mathematics_score, database_score, ai_score,
            ml_score, web_score, data_science_score,
            interest_ai, interest_web, interest_data,
            interest_programming, interest_cloud, interest_security
        ]
    })
    st.table(profile_df.set_index("Attribute"))

st.markdown("---")
st.caption("Elective Recommendation System • Synthetic dataset • Not a substitute for academic advising")