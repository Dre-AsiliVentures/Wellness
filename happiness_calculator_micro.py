import streamlit as st

def calculate_happiness(set_point, life_circumstances, voluntary_activities):
    # Define the Happiness equation based on your interpretation of Martin Seligman's work
    happiness = set_point + life_circumstances + voluntary_activities
    return happiness

def main():
    st.title("Happiness Calculator")
    
    # Input fields for set point, life circumstances, and voluntary activities
    set_point = st.number_input("Set Point", min_value=0.0, max_value=10.0, step=0.1, value=5.0)
    life_circumstances = st.number_input("Life Circumstances", min_value=0.0, max_value=10.0, step=0.1, value=5.0)
    voluntary_activities = st.number_input("Voluntary Activities", min_value=0.0, max_value=10.0, step=0.1, value=5.0)
    
    # Calculate happiness based on user input
    happiness = calculate_happiness(set_point, life_circumstances, voluntary_activities)
    
    # Display the calculated happiness
    st.write("Your Happiness Score:", happiness)

if __name__ == "__main__":
    main()
