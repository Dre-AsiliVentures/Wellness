import pandas as pd
import streamlit as st

# Load the Excel file into a DataFrame
url = 'https://asiliventures.com/wp-content/uploads/2023/06/Healthy-Food-Recipe-Calculator.xlsx'
df = pd.read_excel(url)

# Get unique category values
categories = df['Category'].unique()

# Create the Streamlit application
def main():
    # Create a sidebar for category selection
    selected_categories = st.sidebar.multiselect('Select Categories', categories)

    # Initialize the selected ingredients list
    selected_ingredients = []

    for category in selected_categories:
        # Filter ingredients based on the selected categories
        filtered_df = df[df['Category'] == category]

        # Get the current session state
        session_state = st.session_state

        # Get unique ingredient values for the selected category
        ingredients = filtered_df['Name of Ingredient'].unique()

        # Display the dropdown menu for ingredient selection
        selected_ingredient = st.selectbox(f'Select Ingredient in {category}', ingredients)

        # Add the ingredient to the selected ingredients list
        if selected_ingredient not in selected_ingredients:
            selected_ingredients.append(selected_ingredient)

        # Get the ingredient data based on the selected ingredient
        ingredient_data = filtered_df[filtered_df['Name of Ingredient'] == selected_ingredient].iloc[0]

        amount_purchased_key = f'amount_{selected_ingredient}'
        recipe_units_used_key = f'units_{selected_ingredient}'

        # Retrieve the previously entered values from the session state
        amount_purchased = session_state.get(amount_purchased_key, 0)
        recipe_units_used = session_state.get(recipe_units_used_key, 0)

        # Display the input fields and update the session state
        amount_purchased = st.number_input(f'Amount purchased for {selected_ingredient}', min_value=0, step=1,
                                           value=amount_purchased, key=amount_purchased_key)
        session_state[amount_purchased_key] = amount_purchased

        recipe_units_used = st.slider(f'Recipe units used for {selected_ingredient}', min_value=0, max_value=10000,
                                      value=recipe_units_used, key=recipe_units_used_key)
        session_state[recipe_units_used_key] = recipe_units_used

        # Calculate the ingredient cost
        if amount_purchased != 0:
            ingredient_cost = (recipe_units_used / amount_purchased) * ingredient_data['Edible Portion Yield'] * ingredient_data['Unit Cost']
        else:
            ingredient_cost = 0  # Set the ingredient cost to 0 if amount_purchased is 0

        # Add the ingredient cost to the total cost
        total_cost += ingredient_cost

    # Display the recipe cost
    st.write(f'Recipe Cost: ${total_cost:.2f}')


if __name__ == '__main__':
    main()
