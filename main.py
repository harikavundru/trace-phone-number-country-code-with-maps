import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

from myphone import number

# Parse phone number
pepnumber = phonenumbers.parse(number)

# Get location
location = geocoder.description_for_number(pepnumber, "en")

# Print location with proper encoding
print("Location:", location.encode('utf-8', 'ignore').decode('utf-8'))

# Get carrier information
service_pro = phonenumbers.parse(number)
print("Carrier:", carrier.name_for_number(service_pro, "en"))

# Geocode using OpenCage
key = 'bd475d5d4d104e8a80bc3a00786d2a27'
geocoder = OpenCageGeocode(key)

# Convert location to string for geocoding
query = str(location)

# Handle encoding issues during geocoding result printing
results = geocoder.geocode(query)
for result in results:
    formatted_result = result.get('formatted', '')
    print("Geocoding Result:", formatted_result.encode('utf-8', 'ignore').decode('utf-8'))

    # Extract and print latitude and longitude
    geometry = result.get('geometry', {})
    lat = geometry.get('lat', '')
    lng = geometry.get('lng', '')
    print("Latitude:", lat)
    print("Longitude:", lng)

    # Break out of the loop after processing the first result
    break

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")