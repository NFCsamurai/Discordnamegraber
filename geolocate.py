import requests

def get_geolocation():
    try:
        # Get your public IP
        ip_response = requests.get('https://api.ipify.org?format=json')
        ip = ip_response.json()['ip']
        print(f"Your Public IP: {ip}")

        # Get geo info using IP
        geo_response = requests.get(f'https://ipinfo.io/{ip}/json')
        data = geo_response.json()

        print("\n--- Geolocation Info ---")
        print(f"IP       : {data.get('ip')}")
        print(f"City     : {data.get('city')}")
        print(f"Region   : {data.get('region')}")
        print(f"Country  : {data.get('country')}")
        print(f"Location : {data.get('loc')}")  # lat,long
        print(f"Org      : {data.get('org')}")
        print(f"Timezone : {data.get('timezone')}")
    except Exception as e:
        print(f"Error: {e}")

get_geolocation()
