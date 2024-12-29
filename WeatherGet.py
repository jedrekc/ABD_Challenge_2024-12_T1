import requests
import click
import json


URL_WEATHER_CURRENT = f"https://api.open-meteo.com/v1/forecast"
URL_WEATHER_ARCHIVE = f"https://api.open-meteo.com/v1/archive"

def get_weather(latitude, longitude):
    url = rf"{URL_WEATHER_CURRENT}?{latitude=}&{longitude=}"
    
    resp = requests.get(url)

    return resp


def save_weather (data_to_save, save_file):
    with open(save_file, "w", encoding="utf-8") as file:
        json.dump(data_to_save, file, indent=4, ensure_ascii=False)


CITIES = {
    "Bydgoszcz": (53.1235, 18.0076),
    "Czestochowa": (50.7965, 19.1241),
    "Daugavpils": (55.875, 26.535),
    "Gdansk": (54.352, 18.6466),
    "Gniezno": (52.5342, 17.5826),
    "Gorzow Wielkopolski": (52.7368, 15.2288),
    "Grudziadz": (53.484, 18.7533),
    "Krakow": (50.0647, 19.945),
    "Krosno": (49.6886, 21.7703),
    "Landshut": (48.5442, 12.1469),
    "Leszno": (51.8414, 16.5749),
    "Lublin": (51.2465, 22.5684),
    "Lodz": (51.7592, 19.456),
    "Opole": (50.6751, 17.9213),
    "Ostrow Wielkopolski": (51.655, 17.8066),
    "Pila": (53.1519, 16.738),
    "Poznan": (52.4064, 16.9252),
    "Rawicz": (51.609, 16.8583),
    "Rybnik": (50.0971, 18.5417),
    "Rzeszow": (50.0413, 21.999),
    "Swietochlowice": (50.297, 18.9178),
    "Tarnow": (50.0138, 20.986),
    "Torun": (53.0138, 18.5984),
    "Warsaw": (52.2297, 21.0122),
    "Wroclaw": (51.1079, 17.0385),
    "Zielona Gora": (51.9356, 15.5062)
}


def get_city_coordinates(city_name: str) -> tuple[float, float]:
    """
    Retrieve coordinates for a given city name.

    :param city_name: Name of the city.
    :return: Tuple containing latitude and longitude.
    """
    return CITIES[city_name]


def get_city_coordinates(city_name: str, latitude: float, longitude: float) -> tuple[float, float]:
    """
    Retrieve coordinates for a given city name.

    :param city_name: Name of the city.
    :return: Tuple containing latitude and longitude.
    """
    result = (None, None)
    if None not in (latitude, longitude):
        result = CITIES[city_name]
    else:
        result = (latitude, longitude)

    return result  


#@click.option('city', type=str)
#@click.argument('latitude', type=float)
#@click.argument('longitude', type=float)


@click.command()
@click.option('--city', type=str, default=None, help='City')
@click.option('--latitude', type=float, default=None, help='Latitude')
@click.option('--longitude', type=float, default=None, help='Longitude')
@click.argument('save_file', type=str)
def main(city, latitude, longitude, save_file):
    
    # TODO city lub współrzędne muszą być niepuste
    
    (latitude, longitude) = get_city_coordinates(city, latitude, longitude)

    resp = get_weather(latitude, longitude)
    
    if resp.ok:
        save_weather(resp.json(), save_file)


if __name__ == "__main__":
    main()