def check_temp(value):
    if value >= 60:
        return "Hot"
    elif 69 >= value >= 40:
        return "Warm"
    else:
        return "Cold"

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities)
