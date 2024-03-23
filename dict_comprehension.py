


weather = {'New York': "Snowing",'Boston':"Sunny",'Los angeles':"Sunny",'Chicago':"Cloudy"}

sunny_weather = {key : value for (key,value) in weather.items() if value=="Sunny" }
print(sunny_weather)