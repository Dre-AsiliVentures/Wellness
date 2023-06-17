import streamlit as st

def calculate_bmi(weight, height, unit):
    if unit == "Imperial":
        bmi = (weight / (height * height)) * 703
    else:
        bmi = weight / (height * height)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def recommend_weight_range(height, unit):
    if unit == "Imperial":
        height_cm = height * 2.54
    else:
        height_cm = height
    min_weight = 18.5 * (height_cm * height_cm) / 10000
    max_weight = 24.9 * (height_cm * height_cm) / 10000
    return f"Recommended weight range: {min_weight:.1f} - {max_weight:.1f} kg"

st.title("BMI Calculator")

unit = st.selectbox("Select unit of measurement:", ["Imperial", "Metric"])
weight = st.number_input(f"Enter your weight ({unit}):")
height = st.number_input(f"Enter your height ({unit}):")

if st.sidebar.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height, unit)
    classification = classify_bmi(bmi)
    st.sidebar.write(f"Your BMI: {bmi:.2f}")
    st.sidebar.write("Classification:", classification)
    st.sidebar.write(recommend_weight_range(height, unit))
