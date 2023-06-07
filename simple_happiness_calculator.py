import streamlit as st

# Function to calculate happiness using the provided formula
def calculate_happiness(alpha, beta, income, age, education, sleep_duration, error_terms):
    # Normalize the input variables
    normalized_income = income / 1000000
    normalized_age = age / 100
    normalized_education = education / 100
    normalized_sleep_duration = sleep_duration / 24

    # Calculate the product
    product = normalized_income * normalized_age * normalized_education * normalized_sleep_duration

    # Calculate the happiness value
    age_multiplier = 1.0 if normalized_age > 0.5 else 1.5  # Youthful age multiplier
    happiness = alpha + beta * product * age_multiplier + sum(error_terms)

    # Normalize the happiness value between 0 and 1
    min_happiness = -100
    max_happiness = 100
    normalized_happiness = (happiness - min_happiness) / (max_happiness - min_happiness)

    return normalized_happiness

# Function to normalize the error variables
def normalize_error(error, min_value, max_value):
    # Normalize the error value
    normalized_error = (error - min_value) / (max_value - min_value)

    return normalized_error

# Streamlit application
def main():
    # Title and description
    st.title("Happiness Calculator")
    st.write("Calculate happiness using the provided formula.")

    # Sliders for variables
    st.title("Input Variables")
    alpha = st.slider("How happy are your parent(s)/guardian", 0, 100, 50)
    beta = st.slider("How well do you believe in love", 0.0, 1.0, 0.5)
    income = st.slider("Income", 0, 1000000, 50000)
    age = st.slider("Age", 7, 100, 7)
    education = st.slider("How Educated are you", 0, 100, 10)
    sleep_duration = st.slider("What your last Sleep Duration (hours)", 0, 24, 8)

    # Error terms
    st.title("Personality and Life choices")
    error1 = st.slider("Rate your Optimism in Life", -10, 10, 0)
    error2 = st.selectbox("Any involvement in Drugs, Crime, or Infidelity", ["No", "Medium", "Yes"])
    error3 = st.checkbox("I believe in: Charity, Resilience, Moderation or Hard work")

    # Normalize the error variables
    normalized_error1 = normalize_error(error1, -10, 10)
    normalized_error2 = normalize_error(0 if error2 == "No" else -10 if error2 == "Medium" else -15, -15, 0)
    normalized_error3 = 1 if error3 else 0

    error_terms = [normalized_error1, normalized_error2, normalized_error3]

    # Calculate happiness
    happiness = calculate_happiness(alpha, beta, income, age, education, sleep_duration, error_terms)

    # Normalize happiness between 0 and 1
    normalized_happiness = happiness if happiness <= 1.0 else 1.0

    # Display happiness
    st.sidebar.write("")
    if st.sidebar.button('Calculate my Happiness'):
        st.sidebar.subheader("Happiness Score:")
        st.sidebar.write(normalized_happiness)
        st.sidebar.subheader("My Happiness as a Percentage:")
        st.sidebar.write(round(normalized_happiness * 100, 2))

# Run the Streamlit application
if __name__ == '__main__':
    main()
