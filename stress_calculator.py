import streamlit as st

# Title and description
st.title("Stress Calculator")
st.write("Calculate your stress level on a scale of 1-10")

# Factor weights (adjust as needed)
weights = {
    "Work-related": 0.3,
    "Personal": 0.2,
    "Environmental": 0.1,
    "Coping Resources": 0.1,
    "Emotional": 0.1,
    "Lifestyle": 0.1,
    "Cognitive": 0.05,
    "Physiological": 0.05,
    "Life Satisfaction": 0.1
}

# Input form
st.header("Factors")

# Work-related factors
st.subheader("Work-related")
workload = st.slider("Workload", 1, 10)
job_demands = st.slider("Job Demands", 1, 10)
# Add more work-related factors as needed

# Personal factors
st.subheader("Personal")
financial_concerns = st.slider("Financial Concerns", 1, 10)
family_issues = st.slider("Family Issues", 1, 10)
# Add more personal factors as needed

# Environmental factors
st.subheader("Environmental")
noise_levels = st.slider("Noise Levels", 1, 10)
temperature = st.slider("Temperature", 1, 10)
# Add more environmental factors as needed

# Coping resources
st.subheader("Coping Resources")
social_support = st.slider("Social Support", 1, 10)
relaxation_techniques = st.slider("Access to Relaxation Techniques", 1, 10)
# Add more coping resources as needed

# Emotional factors
st.subheader("Emotional")
anxiety = st.slider("Anxiety", 1, 10)
depression = st.slider("Depression", 1, 10)
# Add more emotional factors as needed

# Lifestyle factors
st.subheader("Lifestyle")
exercise_habits = st.slider("Exercise Habits", 1, 10)
sleep_quality = st.slider("Sleep Quality", 1, 10)
# Add more lifestyle factors as needed

# Cognitive factors
st.subheader("Cognitive")
negative_self_talk = st.slider("Negative Self-Talk", 1, 10)
perfectionism = st.slider("Perfectionism", 1, 10)
# Add more cognitive factors as needed

# Physiological factors
st.subheader("Physiological")
heart_rate = st.slider("Heart Rate", 1, 10)
blood_pressure = st.slider("Blood Pressure", 1, 10)
# Add more physiological factors as needed

# Life satisfaction
st.subheader("Life Satisfaction")
happiness = st.slider("Happiness", 1, 10)
fulfillment = st.slider("Fulfillment", 1, 10)
# Add more life satisfaction factors as needed

# Calculate stress level
stress_score = (
    weights["Work-related"] * (workload + job_demands) +
    weights["Personal"] * (financial_concerns + family_issues) +
    weights["Environmental"] * (noise_levels + temperature) +
    weights["Coping Resources"] * (social_support + relaxation_techniques) +
    weights["Emotional"] * (anxiety + depression) +
    weights["Lifestyle"] * (exercise_habits + sleep_quality) +
    weights["Cognitive"] * (negative_self_talk + perfectionism) +
    weights["Physiological"] * (heart_rate + blood_pressure) +
    weights["Life Satisfaction"] * (happiness + fulfillment)
)

stress_level = round(stress_score, 1)

# Display stress level
st.header("Stress Level")
st.write(f"Your stress level is: {stress_level}/10")
