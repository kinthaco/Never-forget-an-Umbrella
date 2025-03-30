# Never-forget-an-Umbrella
# Rain Checker: A Functional Approach to Weather Alerts

## Overview  
This project demonstrates my skills in **functional programming** using Python. It integrates the **Twilio API** for sending SMS notifications, **Requests** for interacting with a weather API, and **JSON** for reading and writing data. The script fetches weather forecasts, processes the data functionally, and sends an SMS alert if rain is expected.

## Features  
- **Weather Data Fetching**: Retrieves weather data for a specified location using OpenWeatherMap's API.  
- **Functional Programming**: Implements functions for time conversion, rain detection, and messaging.  
- **SMS Alerts with Twilio**: Sends a notification to my phone if rain is forecasted.  
- **JSON Handling**: Stores API responses in JSON format for further analysis.  

## Technologies Used  
- **Python**  
- **Requests** (for API communication)  
- **Twilio** (for SMS notifications)  
- **JSON** (for data storage and processing)  

## How It Works  
1. **Fetch Geolocation**: Uses OpenWeatherMap’s geolocation API to get latitude and longitude.  
2. **Get Weather Forecast**: Retrieves a short-term weather forecast.  
3. **Process Rain Data**: Converts timestamps, checks for rain conditions, and triggers an alert.  
4. **Send SMS Alert**: If rain is expected, a Twilio message is sent.  

## Setup  
### Prerequisites  
Ensure you have Python installed along with the required dependencies.


## Future Improvements  
- Enhance error handling for API requests.  
- Expand support for multiple locations.  
- Integrate a user-friendly interface.  
