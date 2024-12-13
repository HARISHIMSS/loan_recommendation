from fastapi import FastAPI
# from starlette import status as HttpStatus
from functions.analyze_offers import initiate_dataframe, reformat_dataframe
from functions.calculate_normalized_score import calculate_normalized_score
from functions.compare_with_providers import compare_with_providers
from functions.get_output_dict import get_output_dict
from helpers.constants.priority_filter import PriorityFilterEnum
from helpers.pydantic_models import OffersDto

app = FastAPI(
    title = "Loan Recommendation Engine",
    summary = "Loan Recommendation Engine",
    description = "Loan Recommendation Engine",
    version="0.0.1",
    docs_url="/docs",
    openapi_url="/loan-recommendation/api/v1/openapi.json",
    root_path="/api/v1"
)

@app.get("/get_priority_filters")
def get_priority_filters():
    return {"data":[{"key":filter.name,"value":filter.value} for filter in PriorityFilterEnum]}

@app.post("/analyze_offers")
async def analyze_offers_api(body:OffersDto):
    jsonBody = body.model_dump()
    offersBody =jsonBody["offers"]
    priorityProvidersArray = jsonBody["priority_providers"]
    priorityFilterValue = jsonBody["priority_filter"]
    df = initiate_dataframe(offersBody)
    df = reformat_dataframe(df)
    rdf = calculate_normalized_score(df,priorityFilterValue)
    rdf_sorted = rdf.sort_values('comprehensive_score',ascending=False)
    results = get_output_dict(rdf_sorted)
    extractedPriorityProvidersArray = [item['id'] for item in priorityProvidersArray]
    providers_comparision = compare_with_providers(rdf,extractedPriorityProvidersArray)
    response = {
        "data":results,
        "comparision":providers_comparision
    }
    return response