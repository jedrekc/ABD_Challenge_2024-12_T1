import requests
import click
import json


URL_WEATHER_CURRENT = f"https://api.open-meteo.com/v1/forecast"
URL_WEATHER_ARCHIVE = f"https://api.open-meteo.com/v1/archive"

def get_weather(latitude, longitude, saveFile):
    url = rf"{URL_WEATHER_CURRENT}?{latitude=}&{longitude=}"
    print(rf"{url=}")
    
    resp = requests.get(url)

    print('type(resp) =', type(resp))

    print('resp.ok =', resp.ok)

    return resp

def saveWeather(savefile)
@click.command()
@click.argument('latitude', type=float)
@click.argument('longitude', type=float)
@click.argument('saveFile')
def WeatherGet(latitude, longitude, saveFile):
    # latitude = 53.0677
    # longitude = 17.8315
    
    resp = get_weather(latitude, longitude, saveFile)
    
    print(f"{resp.ok=}")   
    if resp.ok:
        print('TODO')
        
if __name__ == "__main__":
    WeatherGet()