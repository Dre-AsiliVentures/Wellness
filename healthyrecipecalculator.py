import pandas as pd
import streamlit as st
import re

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

    # Initialize the dictionary to store ingredient data
    ingredient_data = {}

    for category in selected_categories:
        # Filter ingredients based on the selected categories
        filtered_df = df[df['Category'] == category]

        # Get unique ingredient values for the selected category
        ingredients = filtered_df['Name of Ingredient'].unique()

        # Display the dropdown menu for ingredient selection
        selected_ingredient = st.selectbox(f'Select Ingredient in {category}', ingredients)

        # Add the ingredient to the selected ingredients list
        if selected_ingredient not in selected_ingredients:
            selected_ingredients.append(selected_ingredient)

        # Get the ingredient data based on the selected ingredient
        ingredient_data[selected_ingredient] = filtered_df[filtered_df['Name of Ingredient'] == selected_ingredient].iloc[0]

    # Calculate recipe cost
    total_cost = 0
    for ingredient in selected_ingredients:
        amount_purchased_key = f'amount_{ingredient}'
        recipe_units_used_key = f'units_{ingredient}'

        # Retrieve the previously entered values from the ingredient data dictionary
        amount_purchased = ingredient_data[ingredient].get(amount_purchased_key, 0)
        recipe_units_used = ingredient_data[ingredient].get(recipe_units_used_key, 0)

        # Display the input fields and update the ingredient data dictionary
        amount_purchased = st.number_input(f'Amount purchased for {ingredient}', min_value=0.0, step=1.0,
                                           value=float(amount_purchased), key=amount_purchased_key)
        ingredient_data[ingredient][amount_purchased_key] = amount_purchased

        recipe_units_used = st.slider(f'Recipe units used for {ingredient}', min_value=0.0, max_value=10000.0,
                                      value=float(recipe_units_used), key=recipe_units_used_key)
        ingredient_data[ingredient][recipe_units_used_key] = recipe_units_used

        # Calculate the ingredient cost
        if amount_purchased != 0:
            row = ingredient_data[ingredient]
            edible_portion_yield = 0.0

            # Check the data type of 'Edible Portion Yield' column and convert accordingly
            if isinstance(row['Edible Portion Yield'], str):
                edible_portion_yield = float(re.sub('[%]', '', row['Edible Portion Yield'])) / 100
            elif isinstance(row['Edible Portion Yield'], int) or isinstance(row['Edible Portion Yield'], float):
                edible_portion_yield = float(row['Edible Portion Yield']) / 100

            ingredient_cost = (recipe_units_used / amount_purchased) * edible_portion_yield * float(row['Unit Cost'])
        else:
            ingredient_cost = 0  # Set the ingredient cost to 0 if amount_purchased is 0

        # Add the ingredient cost to the total cost
        total_cost += ingredient_cost

    # Display the recipe cost
    st.write(f'Recipe Cost: ${total_cost:.2f}')


if __name__ == '__main__':
    main()
