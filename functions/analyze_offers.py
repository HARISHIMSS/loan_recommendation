import pandas as pd
import numpy as np

def initiate_dataframe(offers):
    df = pd.DataFrame(offers)
    return df
def reformat_dataframe(df):
    df = df.astype({
        'settlement_amount':float,
        'price':float,
        'application_fee':float,
        'interest_rate_conversion_charge':float,
        'principal': float,
        'interest': float,
        'processing_fee': float,
        'other_upfront_charges': float,
        'insurance_charges':float,
        'other_charges':float,
        'net_disbursed_amount':float
    })
    return df