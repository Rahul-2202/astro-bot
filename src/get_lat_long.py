import requests
from requests.structures import CaseInsensitiveDict

def get_lat_long(place_of_birth):
    url = f"https://api.geoapify.com/v1/geocode/search?text={place_of_birth}&apiKey=api-key"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    response = requests.get(url, headers=headers)


    if response.status_code == 200:
        data = response.json()
        if data['features']:
            coordinates = data['features'][0]['properties']
            latitude = coordinates['lat']
            longitude = coordinates['lon']
            timezone = coordinates['timezone']['offset_STD']
            print(coordinates)
            return latitude, longitude, timezone
        else:
            raise ValueError("No results found for the provided place.")
    else:
        raise ValueError(f"Error in geocoding place of birth: {response.status_code}")

get_lat_long("Kanpur, Uttar Pradesh, India")
# # Example usage
# latitude, longitude, timezone = get_lat_long(place_of_birth, api_key_geo)