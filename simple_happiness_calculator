import streamlit as st

# Function to calculate happiness using the provided formula
def calculate_happiness(alpha, beta, income, age, education, sleep_duration, error_terms):
    product = income * age * education * sleep_duration
    happiness = alpha + beta * product + sum(error_terms)
    return happiness

# Streamlit application
def main():
    # Title and description
    st.title("Happiness Calculator")
    st.write("Calculate happiness using the provided formula.")

    # Sliders for variables
    st.sidebar.title("Input Variables")
    alpha = st.sidebar.slider("Alpha", 0, 100, 50)
    beta = st.sidebar.slider("Beta", 0.0, 1.0, 0.5)
    income = st.sidebar.slider("Income", 0, 100000, 50000)
    age = st.sidebar.slider("Age", 18, 100, 30)
    education = st.sidebar.slider("Education Level", 0, 20, 10)
    sleep_duration = st.sidebar.slider("Sleep Duration (hours)", 0, 12, 8)

    # Error terms
    st.sidebar.title("Error Terms")
    error1 = st.sidebar.slider("Error 1", -10, 10, 0)
    error2 = st.sidebar.selectbox("Error 2", ["Low", "Medium", "High"])
    error3 = st.sidebar.checkbox("Error 3")

    error_terms = [error1]
    if error2 == "Low":
        error_terms.append(-5)
    elif error2 == "Medium":
        error_terms.append(0)
    elif error2 == "High":
        error_terms.append(5)

    if error3:
        error_terms.append(10)

    # Calculate happiness
    happiness = calculate_happiness(alpha, beta, income, age, education, sleep_duration, error_terms)

    # Display happiness
    st.write("")
    st.subheader("Happiness Score:")
    st.write(happiness)

# Run the Streamlit application
if __name__ == '__main__':
    main()
