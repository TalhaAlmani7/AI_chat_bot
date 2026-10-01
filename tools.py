import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


# CALCULATOR TOOLS

def calculate(a: int, b: int) -> int:
    """Add two numbers together."""
    return int(a) + int(b)


def multiply(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return int(a) * int(b)


def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return int(a) - int(b)


def divide(a: float, b: float) -> float:
    """Divide a by b."""

    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


def calculate_percentage(
    value: float,
    percentage: float
) -> float:
    """Calculate a percentage of a value."""

    return (value * percentage) / 100


# DATE / TIME

def get_current_datetime() -> str:
    """Get the current date and time."""

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# UNIT CONVERSION

def convert_units(
    value: float,
    from_unit: str,
    to_unit: str
) -> float:
    """Convert between supported units."""

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    conversions = {
        ("km", "miles"): value * 0.621371,
        ("miles", "km"): value * 1.60934,

        ("kg", "lb"): value * 2.20462,
        ("lb", "kg"): value * 0.453592,

        ("meters", "feet"): value * 3.28084,
        ("feet", "meters"): value * 0.3048,

        ("celsius", "fahrenheit"): (value * 9 / 5) + 32,
        ("fahrenheit", "celsius"): (value - 32) * 5 / 9,
    }

    conversion = conversions.get(
        (from_unit, to_unit)
    )

    if conversion is None:
        raise ValueError(
            f"Unsupported conversion: {from_unit} → {to_unit}"
        )

    return round(conversion, 2)


# WEATHER TOOL

def get_weather(city: str) -> str:
    """
    Get current weather for a city.

    Uses Open-Meteo geocoding and weather APIs.
    """


    # 1. Convert city name → latitude/longitude


    geocoding_url = (
        "https://geocoding-api.open-meteo.com/v1/search"
    )

    geo_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json",
    }

    geo_response = requests.get(
        geocoding_url,
        params=geo_params,
        timeout=10,
    )

    geo_response.raise_for_status()

    geo_data = geo_response.json()

    if not geo_data.get("results"):
        raise ValueError(
            f"Could not find location: {city}"
        )

    location = geo_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]
    location_name = location["name"]
    country = location.get("country", "")

    # 2. Get current weather

    weather_url = (
        "https://api.open-meteo.com/v1/forecast"
    )

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "precipitation,"
            "weather_code,"
            "wind_speed_10m"
        ),
        "timezone": "auto",
    }

    weather_response = requests.get(
        weather_url,
        params=weather_params,
        timeout=10,
    )

    weather_response.raise_for_status()

    weather_data = weather_response.json()

    current = weather_data["current"]

    return (
        f"Weather in {location_name}, {country}: "
        f"Temperature {current['temperature_2m']}°C, "
        f"Feels like {current['apparent_temperature']}°C, "
        f"Humidity {current['relative_humidity_2m']}%, "
        f"Wind {current['wind_speed_10m']} km/h, "
        f"Precipitation {current['precipitation']} mm."
    )


# WEB SEARCH TOOL

def web_search(query: str) -> str:
    """
    Search the web using Tavily.
    """

    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise ValueError(
            "TAVILY_API_KEY is not configured."
        )

    url = "https://api.tavily.com/search"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "query": query,
        "search_depth": "basic",
        "max_results": 5,
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=20,
    )

    response.raise_for_status()

    data = response.json()

    results = data.get("results", [])

    if not results:
        return "No search results found."

    formatted_results = []

    for result in results:

        title = result.get("title", "")
        content = result.get("content", "")
        url = result.get("url", "")

        formatted_results.append(
            f"Title: {title}\n"
            f"Content: {content}\n"
            f"URL: {url}"
        )

    return "\n\n".join(formatted_results)