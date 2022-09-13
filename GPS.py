import requests


class GPS:

    def __init__(self, city_name, api_key):
        self.gps_api_key = api_key
        self.gps_api_url = "http://api.positionstack.com/v1/forward?access_key=" + self.gps_api_key + "&query="+city_name
        try:
            self.gps_request = requests.get(self.gps_api_url)
            self.gps_request.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        self.gps_json = self.gps_request.json()

    def latitude(self):
        return float(self.gps_json["data"][0]["latitude"])

    def longitude(self):
        return float(self.gps_json["data"][0]["longitude"])
