"""
Joseph Prince: There is Hope in the Grace of God | Praise on TBN
"""
import streamlit as st
import pandas as pd

# Load the Excel file
#df = pd.read_excel('folder/text.xlsx')
df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/06/JosephPrince_There_is_Hope_in_God.xlsx')

# Get unique chapters
chapters = df['Chapter'].unique()

# Create a container for each unique chapter
for chapter in chapters:
    chapter_questions = df[df['Chapter'] == chapter]
    
    # Display the chapter name as a header
    st.header(chapter)
    
    # List all the questions for the chapter
    for index, question in chapter_questions.iterrows():
        st.subheader(f"Q{index+1}: {question['Question']}")
        
        # Display the options as radio buttons
        choice = st.radio("Choose an option:",
                          (question['Option A'], question['Option B'], question['Option C'], question['Option D']))
        
        # Check if the selected option matches the correct answer
        if choice == question['Correct Answer']:
            st.write("Correct!")
            # Update the score accordingly
            # Update the score accordingly
            score = st.session_state.get('score', 0)
            st.session_state['score'] = score + 1
        else:
            st.write("Incorrect!")
        
        # Add an option to choose the word hint
        if st.button("Word Hint"):
            st.write(f"Hint: {question['Word Hint']}")
        
        # Add an option to choose the time hint
        if st.button("Time Hint"):
            st.write(f"Hint: {question['Time Hint']}")
        
        st.write("---")

# Display the final score
score = st.session_state.get('score', 0)
st.write(f"Final Score: {score}/{len(df)}")
