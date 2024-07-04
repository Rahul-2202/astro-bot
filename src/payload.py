import json
from src.get_lat_long import get_lat_long
#   import get_lat_long from "./get_lat_long.py"

def prepare_api_payload(api_ep_name, dob, time_of_birth, place_of_birth):
    # url = "https://json.freeastrologyapi.com/navamsa-chart-info"

    # example input pattern
    # dob = "1990-01-01"
    # time_of_birth = "12:00"
    # place_of_birth = "New York"

    # Get latitude and longitude
    latitude, longitude,timezone = get_lat_long(place_of_birth)

    # Parse date and time
    year, month, date = map(int, dob.split('-'))
    hours, minutes = map(int, time_of_birth.split(':'))

    print(type(year))

    if api_ep_name == "Rasi" or api_ep_name == "Navamsa":
        payload = json.dumps({
            "year": year,
            "month": month,
            "date": date,
            "hours": hours,
            "minutes": minutes,
            "seconds": 0,
            "latitude": latitude,
            "longitude": longitude,
            "timezone": 5.5,
            "settings": {
                "observation_point": "topocentric",
                "ayanamsha": "lahiri"
            }
        })
    else:
      payload = json.dumps({
            "year": year,
            "month": month,
            "date": date,
            "hours": hours,
            "minutes": minutes,
            "seconds": 0,
            "latitude": latitude,
            "longitude": longitude,
            "timezone": 5.5,
            "config": {
                "observation_point": "topocentric",
                "ayanamsha": "lahiri"
            }
        })
    print(payload)
    return payload