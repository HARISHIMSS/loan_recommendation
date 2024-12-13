from functions.adjust_weights_on_priority import adjust_weights_on_priority
from helpers.data.weights import original_weights

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def weight_calculation(field,df,weights):
    return df[field] * weights[field]

def calculate_normalized_score(dataFrame,priority):
    df = dataFrame.copy()

    # Normalize interest rate (lower is better)
    df['interest_rate_norm'] = 1 - (
                df['interest_rate'].str.rstrip('%').astype(float) / df['interest_rate'].str.rstrip('%').astype(
            float).max())

    # Normalize foreclosure fee (lower is better)
    df['foreclosure_fee_norm'] = 1 - (
                df['foreclosure_fee'].str.rstrip('%').astype(float) / df['foreclosure_fee'].str.rstrip('%').astype(
            float).max())

    # Normalize delay penalty fee (lower is better)
    df['delay_penalty_fee_norm'] = 1 - (
                df['delay_penalty_fee'].str.rstrip('%').astype(float) / df['delay_penalty_fee'].str.rstrip('%').astype(
            float).max())

    # Normalize delay other penalty fee (lower is better)
    df['other_penalty_fee_norm'] = 1 - (
                df['other_penalty_fee'].str.rstrip('%').astype(float) / df['delay_penalty_fee'].str.rstrip('%').astype(
            float).max())

    # Normalize APR (lower is better)
    df['apr_norm'] = 1 - (
                df['annual_percentage_rate'].str.rstrip('%').astype(float) / df['annual_percentage_rate'].str.rstrip(
            '%').astype(float).max())

    # Normalize application fee (lower is better)
    df['application_fee_norm'] = 1 - (df['application_fee'] / df['application_fee'].max())

    # Normalize application fee (lower is better)
    df['interest_rate_conversion_charge_norm'] = 1 - (
                df['interest_rate_conversion_charge'] / df['interest_rate_conversion_charge'].max())

    # Normalize total cost (lower is better)
    df['total_cost'] = df['price']
    df['total_cost_norm'] = 1 - (df['total_cost'] / df['total_cost'].max())

    # Normalize term (shorter is generally better)
    df['term_norm'] = 1 - (df['term'].str.split().str[0].astype(int) / df['term'].str.split().str[0].astype(int).max())

    extracted_weights = original_weights if priority is None else adjust_weights_on_priority(original_weights,priority.value)

    print("adjusted weights",extracted_weights)

    keys = list(extracted_weights.keys())

    comprehensive_score = sum(weight_calculation(key,df,extracted_weights) for key in keys)

    df['comprehensive_score'] = comprehensive_score

    return df