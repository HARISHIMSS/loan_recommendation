from enum import Enum

class PriorityFilterEnum(Enum):
    INTEREST_RATE = "interest_rate_norm"
    TOTAL_COST = "total_cost_norm"
    TERM = "term_norm"
    OTHER_PENALTY_FEE = "other_penalty_fee_norm"
    ANNUAL_PERCENTAGE_RATE = "apr_norm"
    DELAY_PENALTY_FEE = "delay_penalty_fee_norm"
    FORECLOSURE_FEE = "foreclosure_fee_norm"
    APPLICATION_FEE = "application_fee_norm"
    INTEREST_RATE_CONVERSION_CHARGE = "interest_rate_conversion_charge_norm"