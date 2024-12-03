# Combine all the data into a single prompt
import json
import streamlit as st

import openai
from openai import OpenAI

from staticVariables import bond_data, market_conventions, yield_curve


def generate_prompt(isin):
    bond_details = bond_data  # Get bond details based on ISIN (here we just use the sample)
    currency =  bond_details["Currency"]

    # Get market conventions and yield curve based on currency
    market_convention = market_conventions.get(currency, {})
    yield_curve_data = yield_curve.get(currency, {})

    # Create a detailed prompt for GPT-4
    prompt = f"""
    You are an expert financial assistant. A user has provided a bond with the following details:
    - ISIN: {isin}
    - Coupon Rate: {bond_details['Coupon Rate']}%
    - Coupon Frequency: {bond_details['Coupon Frequency']}
    - Face Value: {bond_details['Face Value']} {currency}
    - Issue Date: {bond_details['Issue Date']}
    - Maturity Date: {bond_details['Maturity Date']}
    - Currency: {currency}

    The market conventions for {currency} are as follows:
    - Day Count Convention: {market_convention.get('Day Count Convention', 'N/A')}
    - Discounting Method: {market_convention.get('Discounting Method', 'N/A')}
    - Interest Calculation Method: {market_convention.get('Interest Calculation Method', 'N/A')}
    - Compounding Frequency: {market_convention.get('Compounding Frequency', 'N/A')}

    The yield curve for {currency} as of today is:
    {json.dumps(yield_curve_data)}

    Using the above data, please calculate the bond price, Yield to Maturity (YTM), next coupon date, and any other relevant metrics.
    Provide the results in a bullet-point format.
    """

    return prompt


# Function to call GPT-4 API
def get_bond_valuation(isin):
    prompt = generate_prompt(isin)
    client = OpenAI(api_key=openai.api_key)
    st.session_state['messages'].append({'role': 'user', 'content': prompt})

    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=st.session_state['messages'],
            temperature=0,
        )

        # Extract and print the response
        return completion

    except Exception as e:
        return f"Error occurred: {e}"