import streamlit as st

def calculate_happiness(alpha, beta, income, age, education, sleep_duration, error_terms):
    product = income * age * education * sleep_duration
    happiness = alpha + beta * product + sum(error_terms)
    # Normalize the happiness value between 0 and 100
    min_happiness = 0
    max_happiness = 100
    normalized_happiness = (happiness - min_happiness) / (max_happiness - min_happiness) * 100

    return normalized_happiness

# Function to normalize the happiness score between 0 and 1
def normalize_happiness(happiness):
    # Calculate the mean and standard deviation of happiness
    happiness_mean = 50  # Set the mean of happiness scores
    happiness_std = 20  # Set the standard deviation of happiness scores

    # Compute the z-score
    z_score = (happiness - happiness_mean) / happiness_std

    return z_score
    #return normalized_happiness

# Streamlit application
def main():
    # Title and description
    st.title("Happiness Calculator")
    st.write("Calculate happiness using the provided formula.")

    # Sliders for variables
    st.title("Input Variables")
    alpha = st.slider("How happy are your parent(s)/guardian", 0, 100, 50)
    beta = st.slider("How well do you believe in love", 0.0, 1.0, 0.5)
    income = st.slider("Income", 0, 1000000000, 50)
    age = st.slider("Age", 7, 100, 7)
    education = st.slider("How Educated are you", 0, 100, 10)
    sleep_duration = st.slider("What your last Sleep Duration (hours)", 0, 12, 8)

    # Error terms
    st.title("Personality and Life choices")
    error1 = st.slider("Rate your Optimism in Life", -10, 10, 0)
    error2 = st.selectbox("Any involvement in Drugs, Crime, or Infidelity", ["No", "Medium", "Yes"])
    error3 = st.checkbox("I believe in: Charity, Resilience, Moderation or Hard work")

    error_terms = [error1]
    if error2 == "No":
        error_terms.append(0)
    elif error2 == "Medium":
        error_terms.append(-10)
    elif error2 == "Yes":
        error_terms.append(-15)

    if error3:
        error_terms.append(10)

    # Calculate happiness
    happiness = calculate_happiness(alpha, beta, income, age, education, sleep_duration, error_terms)

    # Normalize happiness between 0 and 1
    normalized_happiness = normalize_happiness(happiness)

    # Display happiness
    st.sidebar.write("")
    if st.sidebar.button('Calculate my Happinesss'):
        st.sidebar.subheader("Happiness Score:")
        st.sidebar.write(normalized_happiness)

# Run the Streamlit application
if __name__ == '__main__':
    main()
