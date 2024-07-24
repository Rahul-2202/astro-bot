# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
from src.genai import get_gemini_response
import json
from src.fireGen import converse

initialize_app()
#
#
@https_fn.on_request()
def on_request_example(req: https_fn.Request) -> https_fn.Response:
    return https_fn.Response("Hello world!")

@https_fn.on_request()
def get_astro_data(req: https_fn.Request) -> https_fn.Response:
    from src.payload import prepare_api_payload
    from src.astro_api import get_astrology_data
    from src.format_output import structure_chart_output

    

    # data = req.get_json()
    # api_name = data.get("api_name")
    # dob = data.get("dob")
    # time_of_birth = data.get("time_of_birth")
    # place_of_birth = data.get("place_of_birth")

    # dob(year-month-day)
    dob = "2002-02-22"
    time_of_birth = "19:00"
    place_of_birth = "Kanpur, Uttar Pradesh, India"
    api_name = "Rasi"

    payload = prepare_api_payload(api_name, dob, time_of_birth, place_of_birth)
    response = get_astrology_data(api_name, payload)
    if api_name == "Rasi" : 
        data=response['output'][0]
    else:
        data=response['output']
    formatted_output = structure_chart_output(api_name,data )

    return https_fn.Response(json.dumps(formatted_output))


@https_fn.on_request()
def get_geminiai_response(req: https_fn.Request) -> https_fn.Response:
    return https_fn.Response(json.dumps(get_gemini_response(req)))