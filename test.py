import pyowm
owm = pyowm.OWM('e6bfa133d68b3b9cf9547e4b7bf7f35d')

observation = owm.weather_at_place('Waterloo,CA')
w = observation.get_weather()

humidity = w.get_humidity()
temperature = w.get_temperature('fahrenheit')

print "humdity: ", humidity
print "temperature: ", temperature
