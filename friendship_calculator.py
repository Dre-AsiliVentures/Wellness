import streamlit as st

def calculate_friendship(proximity, duration, frequency, intensity):
    score = proximity + duration + frequency + intensity
    
    if score <= 4:
        return "Strangers"
    elif score <= 8:
        return "Acquaintance"
    elif score <= 12:
        return "Close Friends"
    else:
        return "Significant Other"

def main():
    st.title("Friendship Calculator")

    st.sidebar.title("Friendship Calculator")

    proximity = st.sidebar.slider("Proximity", 0, 10, 5)
    duration = st.sidebar.slider("Duration", 0, 10, 5)
    frequency = st.sidebar.slider("Frequency", 0, 10, 5)
    intensity = st.sidebar.slider("Intensity", 0, 10, 5)

    result = calculate_friendship(proximity, duration, frequency, intensity)

    st.write("Based on the given values, your friendship level is:", result)

if __name__ == "__main__":
    main()
