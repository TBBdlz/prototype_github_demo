import googlemaps

# get envrioment variable in .env file
API_KEY = "YOUR_API_KEY"

# Replace 'YOUR_API_KEY' with your actual API key
gmaps = googlemaps.Client(key=API_KEY)

# Replace these with your latitude and longitude
latitude = 37.4219999
longitude = -122.0840575

# Perform reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))

# Print the result
print(reverse_geocode_result)




