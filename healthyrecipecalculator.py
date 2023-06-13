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

    # Filter ingredients based on the selected categories
    filtered_df = df[df['Category'].isin(selected_categories)]

    # Allow ingredient selection
    selected_ingredients = st.multiselect('Select Ingredients', filtered_df['Name of Ingredient'])

    # Convert units
    unit_conversion_factors = {
        'lb': 453.592,  # Conversion factor from pounds to grams
        'gallon': 3785.41,  # Conversion factor from gallons to milliliters
        'pound': 453.592  # Conversion factor from pounds to grams (alternative)
    }
    convert_units = st.checkbox('Convert to Metric Units')
    if convert_units:
        filtered_df['Unit Cost'] = filtered_df.apply(lambda row: convert_unit_cost(row['Unit'], row['Unit Cost'], unit_conversion_factors), axis=1)

    # Compute recipe cost button
    if st.button('Compute Recipe Cost'):
        # Calculate recipe cost
        total_cost = 0
        for ingredient in selected_ingredients:
            row = filtered_df[filtered_df['Name of Ingredient'] == ingredient].iloc[0]
            amount_purchased = st.number_input(f'Amount purchased for {ingredient}', min_value=0, step=1)
            recipe_units_used = st.slider(f'Recipe units used for {ingredient}', min_value=0, max_value=10000)
            if amount_purchased != 0:
                ingredient_cost = (recipe_units_used / amount_purchased) * row['Edible Portion Yield'] * row['Unit Cost']
            else:
                ingredient_cost = 0  # Set the ingredient cost to 0 if amount_purchased is 0

            total_cost += ingredient_cost

        # Display the recipe cost
        st.write(f'Recipe Cost: ${total_cost:.2f}')


def convert_unit_cost(unit, cost, conversion_factors):
    if unit in conversion_factors:
        return cost / conversion_factors[unit]
    return cost


if __name__ == '__main__':
    main()
