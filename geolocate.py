import requests

def get_geo_from_ip(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()

        if "bogon" in data:
            print("Invalid or private IP address.")
            return

        print("\n--- Geolocation Info ---")
        print(f"IP       : {data.get('ip')}")
        print(f"City     : {data.get('city')}")
        print(f"Region   : {data.get('region')}")
        print(f"Country  : {data.get('country')}")
        print(f"Location : {data.get('loc')}")  # latitude,longitude
        print(f"Org      : {data.get('org')}")
        print(f"Timezone : {data.get('timezone')}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    ip = input("Enter an IP address: ").strip()
    if ip:
        get_geo_from_ip(ip)
    else:
        print("No IP address entered.")

if __name__ == "__main__":
    main()
