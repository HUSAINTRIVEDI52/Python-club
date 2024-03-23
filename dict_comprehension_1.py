Cities_in_F = {'New York':32,'Boston':75,'Los angeles':100,'Chicago':50}
cities_in_C={key:round(values-32)*(5/9) for (key,values) in Cities_in_F.items()}
print(cities_in_C)