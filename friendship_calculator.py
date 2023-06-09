import streamlit as st

def calculate_friendship(proximity, duration, frequency, intensity):
    score = proximity + duration + frequency + intensity
    if (proximity <= 2 or duration <= 2) and frequency <= 2 and intensity <= 2:
        return "Strangers"
    elif proximity <= 4 and (duration <= 4 or frequency <= 4) and intensity <= 4:
        return "Acquaintance"
    elif proximity <= 6 and duration <= 6 and frequency <= 6 and intensity <= 6:
        return "Close Friends"
    elif proximity >= 8 and duration >= 8 and frequency >= 8 and intensity >= 8:
        return "Significant Other"
    else:
        return "Lovers"

#     if proximity <= 2 or duration <= 2:
#         return "Strangers"
#     elif frequency <= 2 and intensity <= 2:
#         return "Strangers"
#     elif proximity <= 4 or duration <= 4:
#         return "Acquaintance"
#     elif frequency <= 4 and intensity <= 4:
#         return "Acquaintance"
#     elif proximity <= 6 and duration <= 6 and frequency <= 6 and intensity <= 6:
#         return "Close Friends"
#     elif proximity >= 8 and duration >= 8 and frequency >= 8 and intensity >= 8:
#         return "Significant Other"
#     else:
#         return "Friendship level not defined"

def main():
    st.title("Friendship Calculator")

    proximity = st.slider("Proximity", 0, 10, 5)
    duration = st.slider("Duration", 0, 10, 5)
    frequency = st.slider("Frequency", 0, 10, 5)
    intensity = st.slider("Intensity", 0, 10, 5)

    
    if st.sidebar.button("Calculate Friendship Level"):
        result = calculate_friendship(proximity, duration, frequency, intensity)
        st.sidebar.write("Based on the given values, your friendship level is:", result)
        if st.sidebar.button('Reset'):
            #st.caching.clear_cache()  # Clear the cache
            #Reset the slider values to their default values
            proximity = st.slider("Proximity", 0, 10, 5)
            duration = st.slider("Duration", 0, 10, 5)
            frequency = st.slider("Frequency", 0, 10, 5)
            intensity = st.slider("Intensity", 0, 10, 5)
#             proximity.value = 5
#             duration.value = 5
#             frequency.value = 5
#             intensity.value = 5
            st.experimental_rerun()  # Rerun the app

if __name__ == "__main__":
    main()
