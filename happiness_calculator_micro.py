import streamlit as st

def calculate_happiness(set_point, life_circumstances, voluntary_activities):
    # Happiness weighting criteria
    set_point_weight = 0.5
    life_circumstances_weight = 0.1
    voluntary_activities_weight = 0.4
    
    # Calculate happiness based on the weighting criteria and user input
    happiness = (
        set_point * set_point_weight +
        life_circumstances * life_circumstances_weight +
        voluntary_activities * voluntary_activities_weight
    )
    
    return happiness

def main():
    st.title("Happiness Calculator")
    
    st.sidebar.subheader("Set Point")
    
    # Checkbox questions for genetic predisposition and weight gain
    genetic_predisposition = st.sidebar.checkbox("1. Genetic predisposition towards happiness")
    weight_gain = st.sidebar.checkbox("2. Experienced weight gain")
    
    # Calculate set point based on checkbox values
    set_point = 5.0  # Default set point
    if genetic_predisposition:
        set_point -= 0.5
    if weight_gain:
        set_point -= 0.5

    with st.container():
        st.subheader("Life Circumstances")
        
        # Sliders for different life circumstances
        good_health = st.slider("Good health", 0.0, 10.0, 5.0)
        stable_relationship = st.slider("Stable and supportive marriage or long-term relationship", 0.0, 10.0, 5.0)
        fulfilling_job = st.slider("Fulfilling job/career", 0.0, 10.0, 5.0)
        decent_income = st.slider("Decent income that meets basic needs", 0.0, 10.0, 5.0)
        comfortable_income = st.slider("Comfortable income", 0.0, 10.0, 5.0)
        safe_environment = st.slider("Living in a safe and pleasant environment", 0.0, 10.0, 5.0)
        social_support = st.slider("Strong social support", 0.0, 10.0, 5.0)
        engagement_social = st.slider("Engagement in social activities", 0.0, 10.0, 5.0)
    
    with st.sidebar:
        st.subheader("Voluntary Activities")
        
        # Sliders for different voluntary activities
        past_thoughts = st.slider("Past thoughts", 0.0, 10.0, 5.0)
        gratitude = st.slider("Gratitude", 0.0, 10.0, 5.0)
        forgiveness = st.slider("Forgiveness", 0.0, 10.0, 5.0)
        transgression = st.slider("Transgression", 0.0, 10.0, 5.0)
        motivation = st.slider("Motivation", 0.0, 10.0, 5.0)
        perception_life = st.slider("Perception of life in love", 0.0, 10.0, 5.0)
        perception_profession = st.slider("Perception of life in profession", 0.0, 10.0, 5.0)
        perception_finances = st.slider("Perception of life in finances", 0.0, 10.0, 5.0)
        perception_play = st.slider("Perception of life in play", 0.0, 10.0, 5.0)
        perception_friends = st.slider("Perception of life in friends", 0.0, 10.0, 5.0)
        perception_health = st.slider("Perception of life in health", 0.0, 10.0, 5.0)
        perception_generativity = st.slider("Perception of life in generativity", 0.0, 10.0, 5.0)
    
    with st.container():
        st.subheader("Positive Emotions")
        
        # Sliders for positive emotions (past, present, future)
        past_positive_emotions = {
            "Serenity": st.slider("Past Serenity", 0.0, 10.0, 5.0),
            "Fulfillment": st.slider("Past Fulfillment", 0.0, 10.0, 5.0),
            "Pride": st.slider("Past Pride", 0.0, 10.0, 5.0),
            "Satisfaction": st.slider("Past Satisfaction", 0.0, 10.0, 5.0)
        }
        
        present_positive_emotions = {
            "Pleasure": st.slider("Present Pleasure", 0.0, 10.0, 5.0),
            "Ecstasy": st.slider("Present Ecstasy", 0.0, 10.0, 5.0),
            "Joy": st.slider("Present Joy", 0.0, 10.0, 5.0),
            "Calm": st.slider("Present Calm", 0.0, 10.0, 5.0),
            "Ebullience": st.slider("Present Ebullience", 0.0, 10.0, 5.0)
        }
        
        future_positive_emotions = {
            "Faith": st.slider("Future Faith", 0.0, 10.0, 5.0),
            "Trust": st.slider("Future Trust", 0.0, 10.0, 5.0),
            "Hope": st.slider("Future Hope", 0.0, 10.0, 5.0),
            "Optimism": st.slider("Future Optimism", 0.0, 10.0, 5.0)
        }
        
    with st.container():
        st.subheader("Social Relationships")
        
        # Slider for social relationships with friends and family
        social_relationships = st.slider("Social Relationships (Friends and Family)", 0.0, 10.0, 5.0)
    
    with st.container():
        st.subheader("Found Meaning and Purpose")
        
        # Slider for "Found Meaning and Purpose"
        meaning_purpose = st.slider("Found Meaning and Purpose", 0.0, 10.0, 5.0)
    
    with st.container():
        st.subheader("Engagement in Meaningful Activities and Hobbies")
        
        # Slider for "Engagement in meaningful activities and hobbies"
        engagement_activities = st.slider("Engagement in Meaningful Activities and Hobbies", 0.0, 10.0, 5.0)
    
    # Calculate happiness based on user input
    happiness = calculate_happiness(set_point, life_circumstances, voluntary_activities)
    
    # Display the calculated happiness
    st.write("Your Happiness Score:", happiness)

if __name__ == "__main__":
    main()
