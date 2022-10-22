import sys, json, requests, time, pprint

API = "300b621fc00ca2825232e71d9829be51"

city = input('City: ')
state = input('State: ')
zip = 'zip'

geo = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},us&limit=1&appid={API}'

coordinates = requests.get(geo)
loc = coordinates.json()
location = dict(loc[0])
lat = location['lat']
lon = location['lon']
# print(lat)
# print(lon)

call = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={API}"

response = requests.get(call)
weather_report = response.json()
# pprint.pprint(weather_report)
feels_like = (round(weather_report['main']['feels_like']))
humidity = (round(weather_report['main']['humidity']))
temperature = (round(weather_report['main']['temp']))
the_sky = weather_report['weather']
the_sky = (dict(the_sky[0]))
print(the_sky)
sky_main = the_sky.get('main')
sky_description = the_sky.get('description')


print(f"Right now it feels like {feels_like} degrees \nWith a humidity of: {humidity}%\nThe temperature right now is {temperature} degrees with a {sky_description}")
