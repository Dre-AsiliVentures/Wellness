import streamlit as st

def calculate_calories(age, gender, weight, height, activity_level, goal):
    # Calorie calculation logic goes here
    # Replace this with your own calculation algorithm
    
    # Placeholder calculation based on the provided elements
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    
    if activity_level == "Sedentary":
        tdee = bmr * 1.2
    elif activity_level == "Lightly Active":
        tdee = bmr * 1.375
    elif activity_level == "Moderately Active":
        tdee = bmr * 1.55
    elif activity_level == "Very Active":
        tdee = bmr * 1.725
    else:
        tdee = bmr * 1.9
    
    if goal == "Weight Loss":
        calories = tdee - 500
    elif goal == "Weight Maintenance":
        calories = tdee
    elif goal == "Muscle Gain":
        calories = tdee + 500
    else:
        calories = 0
    
    return calories

# Streamlit app UI
st.title("Calorie Calculator")

# User input elements
age = st.slider("Age", 1, 100, 30)
gender = st.selectbox("Gender", ("Male", "Female"))
weight = st.number_input("Weight (kg)")
height = st.number_input("Height (cm)")
activity_level = st.selectbox("Activity Level", ("Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"))
goal = st.selectbox("Goal", ("Weight Loss", "Weight Maintenance", "Muscle Gain"))

# Calculate calories on button click
if st.button("Calculate"):
    calories = calculate_calories(age, gender, weight, height, activity_level, goal)
    st.success(f"You need to consume {calories} calories per day.")

