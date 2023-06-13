import streamlit as st

def calculate_friendship(proximity, duration, frequency, intensity):
    score = proximity + duration + frequency + intensity
    if proximity <= 2 and duration <= 2 and frequency <= 2 and intensity <= 2:
        return "Strangers"
    elif proximity <= 4 and duration <= 4 and frequency <= 4 and intensity <= 4:
        return "Acquaintance"
    elif proximity <= 6 and duration <= 6 and frequency <= 6 and intensity <= 6:
        return "Close Friends"
    else:
        return "Significant Other"

def main():
    st.title("Friendship Calculator")

    proximity = st.slider("Proximity", 0, 10, 5)
    duration = st.slider("Duration", 0, 10, 5)
    frequency = st.slider("Frequency", 0, 10, 5)
    intensity = st.slider("Intensity", 0, 10, 5)

    
    if st.sidebar.button("Calculate Friendship Level"):
        result = calculate_friendship(proximity, duration, frequency, intensity)
        st.sidebar.write("Based on the given values, your friendship level is:", result)

if __name__ == "__main__":
    main()
