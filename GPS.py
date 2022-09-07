import requests


class GPS:

    def __init__(self, city_name):
        self.gps_api_key = "d62c1a3f25d595fdad7c00363298ba2f"
        self.gps_api_url = "http://api.positionstack.com/v1/forward?access_key=" + self.gps_api_key + "&query="+city_name
        self.gps_request = requests.get(self.gps_api_url)
        self.gps_json = self.gps_request.json()

    def latitude(self):
        return float(self.gps_json["data"][0]["latitude"])

    def longitude(self):
        return float(self.gps_json["data"][0]["longitude"])
