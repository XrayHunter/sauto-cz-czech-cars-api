"""
Find the best car deals by comparing price/mileage ratio.
Lower ratio = better deal (less CZK per km driven).

Usage:
    pip install requests
    python find_best_deals.py

Get your API key at: https://rapidapi.com/XrayHunter-F8lHMI9me/api/sauto-cz-czech-cars-api
"""

import requests

API_KEY = "YOUR_API_KEY"  # Replace with your RapidAPI key
BASE_URL = "https://sauto-cz-czech-cars-api.p.rapidapi.com"
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "sauto-cz-czech-cars-api.p.rapidapi.com",
}


def find_deals(make: str, max_price: int = 400000, min_mileage: int = 10000):
    """Find best deals for a given make by price/mileage ratio."""
    response = requests.get(
        f"{BASE_URL}/search",
        headers=HEADERS,
        params={
            "make": make,
            "condition": "used",
            "price_max": max_price,
            "mileage_min": min_mileage,
            "per_page": 50,
        },
    )
    data = response.json()

    # Filter cars with valid price and mileage
    cars = [
        r for r in data["results"]
        if r["price"] and r["mileage_km"] and r["mileage_km"] > 0
    ]

    # Sort by price/mileage ratio (lower = better deal)
    cars.sort(key=lambda c: c["price"] / c["mileage_km"])

    return cars, data["total_count"]


def main():
    makes = ["skoda", "volkswagen", "ford", "hyundai", "toyota"]

    for make in makes:
        cars, total = find_deals(make, max_price=300000)
        print(f"\n{'='*60}")
        print(f"  {make.upper()} — {total} used cars under 300K CZK")
        print(f"{'='*60}")

        if not cars:
            print("  No cars with valid price/mileage found")
            continue

        print(f"  Top 5 best deals (lowest CZK per km):\n")
        for car in cars[:5]:
            ratio = car["price"] / car["mileage_km"]
            print(f"  {car['make']} {car['model']} ({car['year_manufactured']})")
            print(f"    Price: {car['price']:,} CZK")
            print(f"    Mileage: {car['mileage_km']:,} km")
            print(f"    Ratio: {ratio:.2f} CZK/km")
            print(f"    {car['fuel']} | {car['gearbox']}")
            print()


if __name__ == "__main__":
    main()
