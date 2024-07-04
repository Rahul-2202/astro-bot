import requests

def get_astrology_data(api_name, payload):
    base_url = "https://json.freeastrologyapi.com/"
    # api_key = "api_key"

    api_endpoints = {
        "Rasi": "planets",
        "Navamsa": "navamsa-chart-info",
        "Hora": "d2-chart-info",
        "Drekkana":"d3-chart-info",
        "Chaturthamsa": "d4-chart-info",
        "Panchamsa":"d5-chart-info",
        "Shasthamsa": "d6-chart-info",
        "Saptamsa":"d7-chart-info",
        "Ashtamsa": "d8-chart-info",
        "Dasamsa": "d10-chart-info",
        "Rudramsa":"d11-chart-info",
        "Dwadasamsa": "d12-chart-info",
        "Shodasamsa":"d16-chart-info",
        "Vimsamsa": "d20-chart-info",
        "Siddhamsa":"d24-chart-info",
        "Nakshatramsa": "d27-chart-info",
        "Nakshatramsa":"d30-chart-info",
        "Trimsamsa": "d40-chart-info",
        "Khavedamsa":"d45-chart-info",
        "Shashtyamsa": "d60-chart-info"
    }

    if api_name in api_endpoints:
        endpoint = api_endpoints[api_name]
        url = f"{base_url}{endpoint}"
        print(url)

        headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'api-key'
        }
        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return f"Error: {response.status_code} - {response.text}"
    else:
        return "Invalid API name. Available options are: " + ", ".join(api_endpoints.keys())