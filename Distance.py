#There is a library named geopy that has cities information 
import geopy
#import the open source satelite ( map) , geocoder- where Normandim is import
from geopy.geocoders import Nominatim
#we need swuare root for distance formula between 2 points
from math import sqrt
#Define Nominatim as our "google maps" user_agent = city or country
geolocator = Nominatim(user_agent="Specify_your_app_name_here")
#Define a function called distance
def distance(city1, city2):
    #Find city1 and city2 locations
    location1 = geolocator.geocode(city1)
    location2 = geolocator.geocode(city2)
    #find coordinates (latitude and longitude)
    x1, y1 = location1.latitude, location1.longitude
    x2, y2 = location2.latitude, location2.longitude
    #Distancia entre 2 pontos formula 
    distance = sqrt(((x1-x2) ** 2) + ((y1-y2) ** 2))
    print(distance * 100)
#call function 
distance(str(input("Enter city1: ")), str(input("Enter city2: ")))

