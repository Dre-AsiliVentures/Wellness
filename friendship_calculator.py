import streamlit as st

def calculate_friendship(proximity, duration, frequency, intensity):
    score = proximity + duration + frequency + intensity
    
    if proximity <= 2:
        return "Strangers"
    elif score <= 8:
        return "Acquaintance"
    elif intensity >3 and score <= 12:
        return "Close Friends"
    elif intensity>=4 and duration>3 and proximity>=3:
        return "Significant Other"
    else: 
        return ""

def main():
    st.title("Friendship Calculator")

    proximity = st.slider("Proximity", 0, 10, 5)
    duration = st.slider("Duration", 0, 10, 5)
    frequency = st.slider("Frequency", 0, 10, 5)
    intensity = st.slider("Intensity", 0, 10, 5)

    result = calculate_friendship(proximity, duration, frequency, intensity)

    st.write("Based on the given values, your friendship level is:", result)

if __name__ == "__main__":
    main()
