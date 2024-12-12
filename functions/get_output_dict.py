def get_output_dict(dataFrame):
    results = []
    for _, offer in dataFrame.iterrows():
        result = {
            'id': offer['id'],
            'bpp_id': offer['bpp_id'],
            'settlement_amount': f"{offer['settlement_amount']:,.2f}",
            'net_disbursed_amount': f"{offer['net_disbursed_amount']:,.2f}",
            'interest_rate': offer['interest_rate'],
            'annual_percentage_rate': offer['annual_percentage_rate'],
            'term': offer['term'],
            'repayment_frequency': offer['repayment_frequency'],
            'comprehensive_score': f"{offer['comprehensive_score']:.4f}",
            'detailed_breakdown': {
                "interest_rate_score": f"{offer['interest_rate_norm']:.4f}",
                "total_cost_score": f"{offer['total_cost_norm']:.4f}",
                "term_score": f"{offer['term_norm']:.4f}",
                "other_penalty_fee_score": f"{offer['other_penalty_fee_norm']:.4f}",
                "apr_score": f"{offer['apr_norm']:.4f}",
                "delay_penalty_fee_score": f"{offer['delay_penalty_fee_norm']:.4f}",
                "foreclosure_fee_score": f"{offer['foreclosure_fee_norm']:.4f}",
                "application_fee_score": f"{offer['application_fee_norm']:.4f}",
                "interest_rate_conversion_charge_score": f"{offer['interest_rate_conversion_charge_norm']:.4f}"
            }

        }
        results.append(result)
    return results