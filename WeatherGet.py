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


@click.command()
@click.argument('latitude', type=float)
@click.argument('longitude', type=float)
@click.argument('save_file', type=str)
def main(latitude, longitude, save_file):
    
    resp = get_weather(latitude, longitude, save_file)
    
    if resp.ok:
        save_weather(resp.json(), save_file)
        
if __name__ == "__main__":
    main()