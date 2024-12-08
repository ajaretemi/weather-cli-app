import requests  # Import the requests library to make HTTP requests


# Function to fetch weather data from OpenWeatherMap
def fetch_weather(api_key, city_name):
    """
    Fetch weather data from OpenWeatherMap using the provided API key and city name.

    Args:
        api_key (str): Your unique OpenWeatherMap API key.
        city_name (str): The name of the city to fetch weather information for.

    Returns:
        dict: JSON response from OpenWeatherMap if successful, None otherwise.
    """
    # Base URL for OpenWeatherMap's weather endpoint
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Parameters for the request
    params = {
        "q": city_name,            # City name entered by the user
        "appid": api_key,          # API key for authentication
        "units": "metric",         # Units set to metric for temperature in °C; change to 'imperial' for °F
    }

    try:
        # Make the GET request to OpenWeatherMap
        response = requests.get(base_url, params=params)

        # Raise an exception if the response status is not 200 (OK)
        response.raise_for_status()

        # Return the parsed JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        print("Error while making request:", e)
        return None  # Return None if the request fails


# Function to display weather data to the user
def display_weather(data):
    """
    Display weather information from the fetched data.

    Args:
        data (dict): Parsed JSON data from the OpenWeatherMap API response.
    """
    if data:  # If data is available
        # Display location, temperature, weather description, humidity, and wind speed
        print(f"\nWeather in {data['name']}, {data['sys']['country']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:  # If no data is available
        print("Could not fetch weather data. Please check your connection or try again later.")


# Main application loop
def main():
    """
    Main function to handle user input, fetch data, and display results.
    """
    # Set your OpenWeatherMap API key here
    api_key = "36032bc0808783c2b949fc3d30a07ddc" 

    # Prompt user to input the name of the city
    city_name = input("Enter city name to get the weather forecast: ")

    # Fetch weather data using the entered city name
    weather_data = fetch_weather(api_key, city_name)

    # Display the weather data to the user
    display_weather(weather_data)


# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()
