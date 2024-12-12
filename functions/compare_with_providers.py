def analyze_provider_strengths(provider_offer, df):
    strengths = []

    # Interest Rate
    if provider_offer['interest_rate_norm'] > df['interest_rate_norm'].mean():
        strengths.append({
            'metric': 'Interest Rate',
            'value': provider_offer['interest_rate'],
            'comparision': f"Better than market average of {df['interest_rate'].str.rstrip('%').astype(float).mean():.2f}%"
        })
    # Net Disbursed Amount
    if provider_offer['net_disbursed_amount'] < df['net_disbursed_amount'].mean():
        strengths.append({
            'metric': 'Net Disbursed Amount',
            'value': f"{provider_offer['net_disbursed_amount']:,.2f}",
            'comparision': f"Lower than market average of {df['net_disbursed_amount'].mean():,.2f}"
        })

    # Term
    term_value = int(provider_offer['term'].split()[0])
    if term_value < df['term'].str.split().str[0].astype(int).mean():
        strengths.append({
            'metric': 'Loan Term',
            'value': provider_offer['term'],
            'comparision': f"Shorter than market average of {df['term'].str.split().str[0].astype(int).mean():.1f} months"
        })
    # Other Penalty Fee
    other_penalty_fee_value = float(provider_offer['other_penalty_fee'].rstrip('%'))
    mean_other_penalty_fee_value = df['other_penalty_fee'].str.rstrip('%').astype(float).mean()
    if other_penalty_fee_value < mean_other_penalty_fee_value:
        strengths.append({
            'metric': 'Other Penalty Fee',
            'value': f"{other_penalty_fee_value:,.2f}",
            'comparision': f"Lower than market average of {mean_other_penalty_fee_value:,.2f}%"
        })

    # Delay Penalty Fee
    delay_penalty_fee_value = float(provider_offer['delay_penalty_fee'].rstrip('%'))
    mean_delay_penalty_fee_value = df['delay_penalty_fee'].str.rstrip('%').astype(float).mean()
    if delay_penalty_fee_value < mean_delay_penalty_fee_value:
        strengths.append({
            'metric': 'Delay Penalty Fee',
            'value': f"{delay_penalty_fee_value:,.2f}",
            'comparision': f"Lower than market average of {mean_delay_penalty_fee_value:,.2f}%"
        })
    # Foreclosure Fee
    foreclosure_fee_value = float(provider_offer['foreclosure_fee'].rstrip('%'))
    mean_foreclosure_fee_value = df['foreclosure_fee'].str.rstrip('%').astype(float).mean()
    if foreclosure_fee_value < mean_foreclosure_fee_value:
        strengths.append({
            'metric': 'Foreclosure Fee',
            'value': f"{foreclosure_fee_value:,.2f}",
            'comparision': f"Lower than market average of {mean_foreclosure_fee_value:,.2f}%"
        })
    # Interest Rate Conversion Charge
    if provider_offer['interest_rate_conversion_charge'] < df['interest_rate_conversion_charge'].mean():
        strengths.append({
            'metric': 'Interest Rate Conversion Charge',
            'value': f"{provider_offer['interest_rate_conversion_charge']:,.2f}",
            'comparision': f"Lower than market average of {df['interest_rate_conversion_charge'].mean():,.2f}"
        })

    return strengths


def analyze_provider_weaknesses(provider_offer, df):
    weaknesses = []

    # Interest Rate
    if provider_offer['interest_rate_norm'] < df['interest_rate_norm'].mean():
        weaknesses.append({
            'metric': 'Interest Rate',
            'value': provider_offer['interest_rate'],
            'comparision': f"Higher than market average of {df['interest_rate'].str.rstrip('%').astype(float).mean():.2f}%"
        })
    # Net Disbursed Amount
    if provider_offer['net_disbursed_amount'] > df['net_disbursed_amount'].mean():
        weaknesses.append({
            'metric': 'Net Disbursed Amount',
            'value': f"{provider_offer['net_disbursed_amount']:,.2f}",
            'comparision': f"Higher than market average of {df['net_disbursed_amount'].mean():,.2f}"
        })

    # Term
    term_value = int(provider_offer['term'].split()[0])
    if term_value > df['term'].str.split().str[0].astype(int).mean():
        weaknesses.append({
            'metric': 'Loan Term',
            'value': provider_offer['term'],
            'comparision': f"Longer than market average of {df['term'].str.split().str[0].astype(int).mean():.1f} months"
        })
    # Other Penalty Fee
    other_penalty_fee_value = float(provider_offer['other_penalty_fee'].rstrip('%'))
    mean_other_penalty_fee_value = df['other_penalty_fee'].str.rstrip('%').astype(float).mean()
    if other_penalty_fee_value > mean_other_penalty_fee_value:
        weaknesses.append({
            'metric': 'Other Penalty Fee',
            'value': f"{other_penalty_fee_value:,.2f}",
            'comparision': f"Higher than market average of {mean_other_penalty_fee_value:,.2f}%"
        })

    # Delay Penalty Fee
    delay_penalty_fee_value = float(provider_offer['delay_penalty_fee'].rstrip('%'))
    mean_delay_penalty_fee_value = df['delay_penalty_fee'].str.rstrip('%').astype(float).mean()
    if other_penalty_fee_value > mean_other_penalty_fee_value:
        weaknesses.append({
            'metric': 'Delay Penalty Fee',
            'value': f"{delay_penalty_fee_value:,.2f}",
            'comparision': f"Higher than market average of {mean_delay_penalty_fee_value:,.2f}%"
        })
    # Foreclosure Fee
    foreclosure_fee_value = float(provider_offer['foreclosure_fee'].rstrip('%'))
    mean_foreclosure_fee_value = df['foreclosure_fee'].str.rstrip('%').astype(float).mean()
    if foreclosure_fee_value > mean_foreclosure_fee_value:
        weaknesses.append({
            'metric': 'Foreclosure Fee',
            'value': f"{foreclosure_fee_value:,.2f}",
            'comparision': f"Higher than market average of {mean_foreclosure_fee_value:,.2f}%"
        })
    # Interest Rate Conversion Charge
    if provider_offer['interest_rate_conversion_charge'] > df['interest_rate_conversion_charge'].mean():
        weaknesses.append({
            'metric': 'Interest Rate Conversion Charge',
            'value': f"{provider_offer['interest_rate_conversion_charge']:,.2f}",
            'comparision': f"Higher than market average of {df['interest_rate_conversion_charge'].mean():,.2f}"
        })

    return weaknesses


def compare_with_providers(df, partner_bpp_ids):
    comparisions = {}
    for provider_id in partner_bpp_ids:
        provider_offer = df[df['bpp_id'] == provider_id]
        if provider_offer.empty:
            comparisions[provider_id] = {"error": f"Provider {provider_id} not found in the offers"}
            continue

        provider_offer = provider_offer.iloc[0]

        comparision = {
            "provider_id": provider_offer['bpp_id'],
            "provider_offer_details": {
                "id": provider_offer['id'],
                "settlement_amount": f"{provider_offer['settlement_amount']:,.2f}",
                'net_disbursed_amount': f"{provider_offer['net_disbursed_amount']:,.2f}",
                "interest_rate": provider_offer['interest_rate'],
                "annual_percentage_rate": provider_offer['annual_percentage_rate'],
                "term": provider_offer["term"],
                "repayment_frequency": provider_offer['repayment_frequency'],
                "comprehensive_score": f"{provider_offer['comprehensive_score']:.4f}"
            },
            'market_comparision': {
                'avg_net_disbursement_amount': f"{df['net_disbursed_amount'].mean():,.2f}",
                'avg_interest_rate': f"{df["interest_rate"].str.rstrip('%').astype(float).mean():.2f}%",
                'avg_other_penalty_fee': f"{df["other_penalty_fee"].str.rstrip('%').astype(float).mean():.2f}%",
                'avg_delay_penalty_fee': f"{df["delay_penalty_fee"].str.rstrip('%').astype(float).mean():.2f}%",
                'avg_foreclosure_fee': f"{df["foreclosure_fee"].str.rstrip('%').astype(float).mean():.2f}%",
                'avg_annual_percentage_rate': f"{df['annual_percentage_rate'].str.rstrip('%').astype(float).mean():.2f}%",
                'avg_interest_rate_conversion_charge': f"{df['interest_rate_conversion_charge'].mean():.4f}",
                'avg_comprehensive_score': f"{df['comprehensive_score'].mean():.4f}"
            },
            'provider_ranking': list(df.sort_values('comprehensive_score', ascending=False).index).index(
                provider_offer.name) + 1,
            'competitive_analysis': {
                'better_than_market_in': analyze_provider_strengths(provider_offer, df),
                'lower_than_market_in': analyze_provider_weaknesses(provider_offer, df)
            }
        }
        comparisions[provider_id] = comparision
    return comparisions