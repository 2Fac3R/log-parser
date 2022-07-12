import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["API_KEY"]


def get_ip_geolocation(ip):
    """IP Geolocation API provides real-time and accurate geolocation."""
    return requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip}").json()
