import requests
import click
import json


URL_WEATHER_CURRENT = f"https://api.open-meteo.com/v1/forecast"
URL_WEATHER_ARCHIVE = f"https://api.open-meteo.com/v1/archive"

def get_weather(latitude, longitude, saveFile):
    url = rf"{URL_WEATHER_CURRENT}?{latitude=}&{longitude=}"
    # print(rf"{url=}")
    
    resp = requests.get(url)

    # print(f'{type(resp)}d=')
    # print(f'{type(resp.json())=}')
    # print(f'{resp.ok =}')

    return resp


def saveWeather (dataToSave, saveFile):
    with open(saveFile, "w", encoding="utf-8") as file:
        json.dump(dataToSave, file, indent=4, ensure_ascii=False)

    # print(f"Zapisano dane w pliku {saveFile}.")


@click.command()
@click.argument('latitude', type=float)
@click.argument('longitude', type=float)
@click.argument('savefile', type=str)
def WeatherGet(latitude, longitude, savefile):
    # latitude = 53.0677
    # longitude = 17.8315
    
    resp = get_weather(latitude, longitude, savefile)
    
    # print(f"{resp.ok=}")   
    if resp.ok:
        saveWeather(resp.json(), savefile)
        
if __name__ == "__main__":
    WeatherGet()