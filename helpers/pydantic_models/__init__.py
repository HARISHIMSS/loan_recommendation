from pydantic import BaseModel,Field,field_validator,field_serializer
from datetime import datetime
from typing import List
import re
class OfferDto(BaseModel):
    id: str = Field(..., title="Offer ID")
    bpp_id: str = Field(..., title="BPP ID")
    settlement_amount: str = Field(..., title="Settlement Amount")
    price: str = Field(..., title="Price")
    interest_rate: str = Field(..., title="Interest Rate", description="Must be a percentage")
    term: str = Field(..., title="Term")
    interest_rate_type: str = Field(..., title="Interest Rate Type")
    application_fee: str = Field(..., title="Application Fee")
    foreclosure_fee: str = Field(..., title="Foreclosure Fee", description="Must be a percentage")
    interest_rate_conversion_charge: str = Field(..., title="Interest Rate Conversion Charge")
    delay_penalty_fee: str = Field(..., title="Delay Penalty Fee", description="Must be a percentage")
    other_penalty_fee: str = Field(..., title="Other Penalty Fee", description="Must be a percentage")
    annual_percentage_rate: str = Field(..., title="Annual Percentage Rate", description="Must be a percentage")
    repayment_frequency: str = Field(..., title="Repayment Frequency")
    number_of_installments_of_repayment: str = Field(..., title="Number of Installments of Repayment")
    cool_of_period: str = Field(..., title="Cool Off Period")
    installment_amount: str = Field(..., title="Installment Amount")
    principal: str = Field(..., title="Principal")
    interest: str = Field(..., title="Interest")
    processing_fee: str = Field(..., title="Processing Fee")
    other_upfront_charges: str = Field(..., title="Other Upfront Charges")
    insurance_charges: str = Field(..., title="Insurance Charges")
    net_disbursed_amount: str = Field(..., title="Net Disbursed Amount")
    other_charges: str = Field(..., title="Other Charges")

    @field_validator('settlement_amount', 'price', 'application_fee', 'interest_rate_conversion_charge',
               'installment_amount', 'principal', 'interest', 'processing_fee',
               'other_upfront_charges', 'insurance_charges', 'net_disbursed_amount',
               'other_charges')
    def validate_decimal(cls, v):
        if not re.match(r'^\d+(\.\d+)?$', v):
            raise ValueError('Must be a decimal number')
        return v

    @field_validator('interest_rate', 'foreclosure_fee', 'delay_penalty_fee', 'other_penalty_fee', 'annual_percentage_rate')
    def validate_percentage(cls, v):
        if not re.match(r'^\d+(\.\d+)?%$', v):
            raise ValueError('Must be a percentage')
        return v

    @field_validator('number_of_installments_of_repayment')
    def validate_integer_string(cls, v):
        if not v.isdigit():
            raise ValueError('Must be an integer string')
        return v

    @field_validator('cool_of_period')
    def validate_datetime(cls, v):
        try:
            return datetime.fromisoformat(v)
        except ValueError:
            raise ValueError('Must be a valid ISO format datetime string')
class priorityProvidersDto(BaseModel):
    id: str = Field(..., title="Provider Bpp ID")

class OffersDto(BaseModel):
    offers: List[OfferDto]
    priority_providers:List[priorityProvidersDto]