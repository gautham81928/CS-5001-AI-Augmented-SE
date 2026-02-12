import streamlit as st
import requests
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

# Constants
API_KEY = "YOUR_API_KEY"  # Replace with actual API key
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_API_URL = "https://api.openweathermap.org/data/2.5/forecast"

# Cache API responses to avoid repeated calls
@st.cache_data(ttl=3600)
def get_weather_data(location: str, api_key: str) -> Optional[Dict[str, Any]]:
    """Fetch weather data from OpenWeatherMap API."""
    try:
        params = {
            "q": location,
            "appid": api_key,
            "units": "metric"
        }
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching weather data: {e}")
        return None

@st.cache_data(ttl=3600)
def get_forecast_data(location: str, api_key: str) -> Optional[Dict[str, Any]]:
    """Fetch forecast data from OpenWeatherMap API."""
    try:
        params = {
            "q": location,
            "appid": api_key,
            "units": "metric"
        }
        response = requests.get(FORECAST_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching forecast data: {e}")
        return None

def display_weather_data(weather_data: Dict[str, Any]) -> None:
    """Display weather data in a user-friendly format."""
    if not weather_data:
        return

    location = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    st.subheader(f"Current Weather in {location}")
    st.write(f"Temperature: {temperature}°C")
    st.write(f"Condition: {description}")
    st.write(f"Humidity: {humidity}%")
    st.write(f"Wind Speed: {wind_speed} m/s")

def display_forecast_data(forecast_data: Dict[str, Any]) -> None:
    """Display forecast data in a timeline format."""
    if not forecast_data or "list" not in forecast_data:
        return

    st.subheader("5-Day Forecast")
    for item in forecast_data["list"][:5]:  # Show first 5 forecast items
        date = datetime.fromtimestamp(item["dt"]).strftime("%Y-%m-%d %H:%M")
        temp = item["main"]["temp"]
        desc = item["weather"][0]["description"]
        st.write(f"{date}: {temp}°C, {desc}")

def main() -> None:
    """Main function to run the Streamlit app."""
    st.title("Weather App")
    st.write("Get current weather and forecast for any location")

    # Location input
    location = st.text_input("Enter location:", "London")

    # Date selection (not used in current implementation but kept for future use)
    selected_date = st.date_input("Select date:", datetime.now())

    # Fetch and display weather data
    if st.button("Get Weather"):
        weather_data = get_weather_data(location, API_KEY)
        if weather_data:
            display_weather_data(weather_data)

            # Fetch and display forecast data
            forecast_data = get_forecast_data(location, API_KEY)
            if forecast_data:
                display_forecast_data(forecast_data)

    # Refresh button
    if st.button("Refresh"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
