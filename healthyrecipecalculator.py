import pandas as pd
import streamlit as st
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server

# Load the Excel file into a DataFrame
url = 'https://asiliventures.com/wp-content/uploads/2023/06/Healthy-Food-Recipe-Calculator.xlsx'
df = pd.read_excel(url)

# Get unique category values
categories = df['Category'].unique()


# Create a SessionState class to store the widget values
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


# Get the current session state
def get_session():
    session_id = get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id)
    if session_info is None:
        return None
    if "session_state" not in session_info:
        session_info["session_state"] = SessionState()
    return session_info["session_state"]


# Create the Streamlit application
def main():
    # Create a sidebar for category selection
    selected_categories = st.sidebar.multiselect('Select Categories', categories)

    # Filter ingredients based on the selected categories
    filtered_df = df[df['Category'].isin(selected_categories)]

    # Get the current session state
    session_state = get_session()

    # Restore previously selected ingredients from the session state
    if not hasattr(session_state, 'selected_ingredients'):
        session_state.selected_ingredients = []

    # Allow ingredient selection
    selected_ingredients = st.multiselect('Select Ingredients', filtered_df['Name of Ingredient'],
                                          default=session_state.selected_ingredients)

    # Store the selected ingredients in the session state
    session_state.selected_ingredients = selected_ingredients

    # Convert units
    unit_conversion_factors = {
        'lb': 453.592,  # Conversion factor from pounds to grams
        'gallon': 3785.41,  # Conversion factor from gallons to milliliters
        'pound': 453.592  # Conversion factor from pounds to grams (alternative)
    }
    convert_units = st.checkbox('Convert to Metric Units')
    if convert_units:
        filtered_df['Unit Cost'] = filtered_df.apply(lambda row: convert_unit_cost(row['Unit'], row['Unit Cost'],
                                                                                   unit_conversion_factors), axis=1)

    # Compute recipe cost button
    if st.button('Compute Recipe Cost'):
        # Calculate recipe cost
        total_cost = 0
        for ingredient in selected_ingredients:
            row = filtered_df[filtered_df['Name of Ingredient'] == ingredient].iloc[0]
            amount_purchased_key = f'amount_{ingredient}'
            recipe_units_used_key = f'units_{ingredient}'

            # Retrieve the previously entered values from the session state
            amount_purchased = session_state.__dict__.get(amount_purchased_key, 0)
            recipe_units_used = session_state.__dict__.get(recipe_units_used_key, 0)

            # Display the input fields and update the session state
            amount_purchased = st.number_input(f'Amount purchased for {ingredient}', min_value=0, step=1,
                                               value=amount_purchased, key=amount_purchased_key)
            session_state.__dict__[amount_purchased_key] = amount_purchased

            recipe_units_used = st.slider(f'Recipe units used for {ingredient}', min_value=0, max_value=10000,
                                          value=recipe_units_used, key=recipe_units_used_key)
            session_state.__dict__[recipe_units_used_key] = recipe_units_used

            if amount_purchased != 0:
                ingredient_cost = (recipe_units_used / amount_purchased) * row['Edible Portion Yield'] * row[
                    'Unit Cost']
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
