# first install the tuya-IOT-python-sdk package
# open a terminal window and run 'pip3 install tuya-iot-py-sdk'

# open a new file on your IDE

# import the tuyaOpenAPI

from tuya_iot import TuyaOpenAPI

# go to your Tuya account for cloud project authorization info
# enter your access id, access key, API_endpoint
# you need to have an account on tuya to get access id & access key
# API_endpoint is based on your location for more info visit the developer.tuya.com

ACCESS_ID = 'jxk74kykayeemnw52cd4'
ACCESS_KEY = '199ff36d03f142aead0a5d122012c86c'

ENDPOINT = "https://openapi.tuyain.com"

# project configuration
USERNAME = 'conquerjee101@gmail.com'
PASSWORD = '123456789'

# enter your device id

DEVICE_ID = 'vdevo163263242733263'

# Initialization of Tuya openapi

openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.login(USERNAME, PASSWORD)

# after login you will need to have your location which can be obtained from your ip address , to get the ip address go to 'whatismyipaddress website'
# send a get request to get the longitude and latitude
# use get method to obtain the location which will be in nested dictionary
location = openapi.get('/v1.0/iot-03/locations/ip?ip=111.223.29.251')
location = location['result']
latitude, longitude = location['latitude'], location['longitude']

# send a get request to get the temperature
weather_url = f'/v2.0/iot-03/weather/current?lat={latitude}&lon={longitude}'
weather = openapi.get(weather_url)
temperature = weather['result']['current_weather']['temp']

# if the temperature is above 25 °C we turn the device on
if float(temperature) >= 25:
    commands = {'commands': [{'code': 'switch', 'value': True}]}
    request = openapi.post(
        f'/v1.0/iot-03/devices/{DEVICE_ID}/commands', commands)
