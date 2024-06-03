import requests

def fetch_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
        }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None

def display_weather_data(weather_data):
    if weather_data:
        city = weather_data.get('name')
        country = weather_data['sys'].get('country')
        temp = weather_data['main'].get('temp')
        weather_desc = weather_data['weather'][0].get('description')
        humidity = weather_data['main'].get('humidity')
        wind_speed = weather_data['wind'].get('speed')

        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed}m/s")
    else:

        print("Could not retrieve weather data.")

def get_user_input():
    city = input("Enter the city name: ")
    return city

def main():
    api_key = 'b3c4deb376ec83864d38c2c82d8781ae'
    while True:
        city = get_user_input()
        if city.lower() == 'exit':
            break
        weather_data = fetch_weather_data(city, api_key)
        display_weather_data(weather_data)

if __name__ == "__main__":
    main()
