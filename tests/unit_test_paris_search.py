import sys
sys.path.append('C:/Users/Zyr/OneDrive/Documents/Cours/EMA/3A/Intégration Continue et Containérisation/TP/TP_noté/SuiviPrecipitation')

from Weather import Weather
from GPS import GPS

api_key = "d62c1a3f25d595fdad7c00363298ba2f"

def testGPS_forParisCity_returnGPSValue():
    ##Arrange phase
    gps =  GPS("Paris", api_key)
    
    ##Act phase
    latitude = gps.latitude()
    longitude = gps.longitude()
    
    ##Assert phase
    gps_value = str(latitude)+" "+str(longitude)
    return (gps_value)


def testCurrentWeatherCloud_forParisCity_returnCloudString():
    ##Arrange phase
    weather = Weather("Paris", api_key)
    
    ##Act phase
    wcloud = weather.current_weather_cloud()
    
    ##Assert phase
    return (wcloud)
    
def testCurrentWeatherDegree_forParisCity_returnDegreeValue():
    ##Arrange phase
    weather = Weather("Paris", api_key)
    
    ##Act phase
    wdegree = weather.current_weather_degree()
    
    ##Assert phase
    return (wdegree)

print("GPS: ", testGPS_forParisCity_returnGPSValue())
print("Cloud: ", testCurrentWeatherCloud_forParisCity_returnCloudString())
print("Degree: ", testCurrentWeatherDegree_forParisCity_returnDegreeValue())