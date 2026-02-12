import streamlit as st
import requests
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
import os
from functools import lru_cache

# Constants
API_KEY = os.getenv("WEATHER_API_KEY", "your_api_key_here")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"
DEFAULT_LOCATION = "London"
DEFAULT_UNITS = "metric"

def get_weather_data(location: str, units: str = DEFAULT_UNITS) -> Optional[Dict[str, Any]]:
    """Fetch current weather data from OpenWeatherMap API."""
    params = {
        "q": location,
        "appid": API_KEY,
        "units": units
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching weather data: {e}")
        return None

@lru_cache(maxsize=32)
def get_forecast_data(location: str, units: str = DEFAULT_UNITS) -> Optional[Dict[str, Any]]:
    """Fetch 5-day forecast data from OpenWeatherMap API with caching."""
    params = {
        "q": location,
        "appid": API_KEY,
        "units": units
    }
    try:
        response = requests.get(FORECAST_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching forecast data: {e}")
        return None

def display_weather_data(weather_data: Dict[str, Any]) -> None:
    """Display weather information in a user-friendly format."""
    if not weather_data:
        return

    location = weather_data.get("name", "Unknown")
    country = weather_data.get("sys", {}).get("country", "")
    temp = weather_data.get("main", {}).get("temp", 0)
    feels_like = weather_data.get("main", {}).get("feels_like", 0)
    humidity = weather_data.get("main", {}).get("humidity", 0)
    wind_speed = weather_data.get("wind", {}).get("speed", 0)
    description = weather_data.get("weather", [{}])[0].get("description", "").title()
    icon_code = weather_data.get("weather", [{}])[0].get("icon", "")

    # Display main weather info
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Temperature", f"{temp}°C", f"{feels_like}°C feels like")
        st.metric("Humidity", f"{humidity}%")
    with col2:
        st.metric("Wind Speed", f"{wind_speed} m/s")
        st.metric("Conditions", description)

    # Display weather icon
    if icon_code:
        st.image(f"https://openweathermap.org/img/wn/{icon_code}@2x.png", width=100)

def display_forecast(forecast_data: Dict[str, Any]) -> None:
    """Display 5-day forecast in a timeline format."""
    if not forecast_data or "list" not in forecast_data:
        return

    # Group forecast by day
    daily_forecasts = {}
    for item in forecast_data["list"]:
        dt = datetime.fromtimestamp(item["dt"])
        day = dt.strftime("%A")
        if day not in daily_forecasts:
            daily_forecasts[day] = []
        daily_forecasts[day].append(item)

    # Display each day's forecast
    for day, forecasts in daily_forecasts.items():
        with st.expander(f"{day}"):
            # Get average temperature for the day
            temps = [f["main"]["temp"] for f in forecasts]
            avg_temp = sum(temps) / len(temps)

            # Get weather description
            descriptions = [f["weather"][0]["description"] for f in forecasts]
            main_desc = descriptions[0] if descriptions else "Unknown"

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Avg Temp", f"{avg_temp:.1f}°C")
            with col2:
                st.metric("Conditions", main_desc.title())
            with col3:
                # Show time of highest temperature
                max_temp = max(temps)
                max_time = datetime.fromtimestamp(forecasts[temps.index(max_temp)]["dt"]).strftime("%H:%M")
                st.metric("Peak Time", max_time)

def main() -> None:
    """Main function to run the Streamlit weather app."""
    st.set_page_config(page_title="Weather App", page_icon="🌤️")

    # App title and description
    st.title("🌤️ Weather App")
    st.markdown("Get current weather and 5-day forecast for any location")

    # Sidebar for user inputs
    with st.sidebar:
        st.header("Settings")
        location = st.text_input("Location", value=DEFAULT_LOCATION)
        units = st.selectbox("Units", ["metric", "imperial"], index=0)
        refresh = st.button("🔄 Refresh Data")

    # Main content area
    if location:
        with st.spinner("Fetching weather data..."):
            weather_data = get_weather_data(location, units)
            forecast_data = get_forecast_data(location, units)

        if weather_data and forecast_data:
            st.subheader(f"Current Weather in {weather_data.get('name', location)}")
            display_weather_data(weather_data)

            st.subheader("5-Day Forecast")
            display_forecast(forecast_data)
        else:
            st.warning("Could not retrieve weather data. Please check the location and try again.")
    else:
        st.info("Please enter a location to see weather data")

if __name__ == "__main__":
    main()
