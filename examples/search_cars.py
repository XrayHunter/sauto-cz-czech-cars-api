"""
Search for cars on Sauto.cz with filters.

Usage:
    pip install requests
    python search_cars.py

Get your API key at: https://rapidapi.com/XrayHunter-F8lHMI9me/api/sauto-cz-czech-cars-api
"""

import requests

API_KEY = "YOUR_API_KEY"  # Replace with your RapidAPI key
BASE_URL = "https://sauto-cz-czech-cars-api.p.rapidapi.com"
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "sauto-cz-czech-cars-api.p.rapidapi.com",
}


def search(params: dict) -> dict:
    response = requests.get(f"{BASE_URL}/search", headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()


def main():
    # Example 1: Search for used Skoda Octavia diesel
    print("=== Used Skoda Octavia Diesel ===")
    data = search({
        "make": "skoda",
        "model": "octavia",
        "fuel": "diesel",
        "condition": "used",
        "per_page": 5,
    })
    print(f"Found {data['total_count']} cars\n")
    for car in data["results"]:
        print(f"  {car['make']} {car['model']} ({car['year_manufactured']})")
        print(f"    Price: {car['price']:,} CZK | Mileage: {car['mileage_km']:,} km")
        print(f"    Fuel: {car['fuel']} | Gearbox: {car['gearbox']}")
        print()

    # Example 2: Electric cars under 500K CZK
    print("=== Electric Cars Under 500K CZK ===")
    data = search({
        "fuel": "electric",
        "price_max": 500000,
        "per_page": 5,
    })
    print(f"Found {data['total_count']} cars\n")
    for car in data["results"]:
        print(f"  {car['make']} {car['model']} ({car['year_manufactured']}) | {car['price']:,} CZK")

    print()

    # Example 3: BMW automatic 4x4 with low mileage
    print("=== BMW Automatic 4x4, Under 100K km ===")
    data = search({
        "make": "bmw",
        "gearbox": "automatic",
        "drive": "4x4",
        "mileage_max": 100000,
        "per_page": 5,
    })
    print(f"Found {data['total_count']} cars\n")
    for car in data["results"]:
        print(f"  {car['make']} {car['model']} ({car['year_manufactured']}) | {car['price']:,} CZK | {car['mileage_km']:,} km")


if __name__ == "__main__":
    main()
