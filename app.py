from fastapi import FastAPI
# from starlette import status as HttpStatus
from functions.analyze_offers import initiate_dataframe, reformat_dataframe
from functions.calculate_normalized_score import calculate_normalized_score
from functions.compare_with_providers import compare_with_providers
from functions.get_output_dict import get_output_dict
from functions.sorted_df import sorted_df
from helpers.constants.priority_filter import PriorityFilterEnum
from helpers.pydantic_models import OffersDto

app = FastAPI(
    title = "Loan Recommendation Engine",
    summary = "Loan Recommendation Engine",
    description = "Loan Recommendation Engine",
    version="0.0.1",
    root_path="/api/v1"
)

@app.get("/get_priority_filters")
def get_priority_filters():
    return {"data":[{"key":filter.name,"value":filter.value} for filter in PriorityFilterEnum]}

@app.post("/analyze_offers")
async def analyze_offers_api(body:OffersDto):
    json_body = body.model_dump()
    offers_body =json_body["offers"]
    priority_providers_array = json_body["priority_providers"]
    priority_filter_value = json_body["priority_filter"]
    df = initiate_dataframe(offers_body)
    df = reformat_dataframe(df)
    rdf = calculate_normalized_score(df,priority_filter_value)
    rdf_sorted = sorted_df(rdf,priority_filter_value)
    results = get_output_dict(rdf_sorted)
    extracted_priority_providers_array = [item['id'] for item in priority_providers_array]
    providers_comparision = compare_with_providers(rdf,extracted_priority_providers_array)
    response = {
        "data":results,
        "comparision":providers_comparision
    }
    return response