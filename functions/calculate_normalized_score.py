def calculate_normalized_score(dataFrame):
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

    comprehensive_score = df['interest_rate_norm'] * 1 + df['total_cost_norm'] * 1 + df['term_norm'] * 0.9 + df[
        'other_penalty_fee_norm'] * 0.9 + df['apr_norm'] * 0.8 + df['delay_penalty_fee_norm'] * 0.7 + df[
                              'foreclosure_fee_norm'] * 0.3 + df['application_fee_norm'] * 0.2 + df[
                              'interest_rate_conversion_charge_norm'] * 0.1

    df['comprehensive_score'] = comprehensive_score

    return df