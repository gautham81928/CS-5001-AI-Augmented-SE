import os
import streamlit as st
import requests

def get_weather_data(city: str) -> dict:
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        raise ValueError("OPENWEATHERMAP_API_KEY environment variable not set")

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()

def main():
    st.title("Weather App")

    city = st.text_input("Enter city name:")

    if city:
        try:
            weather_data = get_weather_data(city)
            st.write(f"Weather in {city}:")
            st.write(f"Temperature: {weather_data['main']['temp']}°C")
            st.write(f"Humidity: {weather_data['main']['humidity']}%")
            st.write(f"Description: {weather_data['weather'][0]['description']}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching weather data: {e}")
        except KeyError:
            st.error("Invalid city name or API response format")
        except ValueError as e:
            st.error(f"Configuration error: {e}")

if __name__ == "__main__":
    main()
