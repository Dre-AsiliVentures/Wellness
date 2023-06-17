import streamlit as st

def calculate_bmi(weight, height, unit):
    if unit == "Metric":
        bmi = weight / (height / 100) ** 2
    else:
        bmi = (weight / (height ** 2)) * 703
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
    if unit == "Metric":
        min_weight = 18.5 * (height / 100) ** 2
        max_weight = 24.9 * (height / 100) ** 2
    else:
        min_weight = 18.5 * height ** 2 / 703
        max_weight = 24.9 * height ** 2 / 703
    return f"Recommended weight range: {min_weight:.1f} - {max_weight:.1f} kg"

st.title("BMI Calculator")

unit = st.selectbox("Select unit of measurement:", ["Metric", "Imperial"])
if unit == "Metric":
    weight = st.number_input("Enter your weight (kg):")
    height = st.number_input("Enter your height (cm):")
else:
    weight = st.number_input("Enter your weight (lb):")
    feet = st.number_input("Enter your height (ft):")
    inches = st.number_input("Enter your height (in):")
    height = feet * 12 + inches

if st.sidebar.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height, unit)
    classification = classify_bmi(bmi)
    st.sidebar.write(f"Your BMI: {bmi:.2f}")
    st.sidebar.write("Classification:", classification)
    st.sidebar.write(recommend_weight_range(height, unit))
