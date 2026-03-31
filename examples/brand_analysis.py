"""
Compare average car prices across different brands.
Useful for market research and price benchmarking.

Usage:
    pip install requests
    python brand_analysis.py

Get your API key at: https://rapidapi.com/XrayHunter-F8lHMI9me/api/sauto-cz-czech-cars-api
"""

import requests

API_KEY = "YOUR_API_KEY"  # Replace with your RapidAPI key
BASE_URL = "https://sauto-cz-czech-cars-api.p.rapidapi.com"
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "sauto-cz-czech-cars-api.p.rapidapi.com",
}


def analyze_brand(make: str) -> dict:
    """Get price statistics for a brand."""
    response = requests.get(
        f"{BASE_URL}/search",
        headers=HEADERS,
        params={"make": make, "condition": "used", "per_page": 50},
    )
    data = response.json()

    prices = [r["price"] for r in data["results"] if r["price"]]
    mileages = [r["mileage_km"] for r in data["results"] if r["mileage_km"]]

    return {
        "make": make,
        "total_listings": data["total_count"],
        "avg_price": sum(prices) // len(prices) if prices else 0,
        "min_price": min(prices) if prices else 0,
        "max_price": max(prices) if prices else 0,
        "avg_mileage": sum(mileages) // len(mileages) if mileages else 0,
    }


def main():
    brands = [
        "skoda", "volkswagen", "bmw", "audi", "mercedes-benz",
        "toyota", "hyundai", "kia", "ford", "peugeot",
    ]

    print(f"{'Brand':<16} {'Listings':>8} {'Avg Price':>12} {'Min Price':>12} {'Max Price':>12} {'Avg Mileage':>12}")
    print("-" * 76)

    results = []
    for brand in brands:
        stats = analyze_brand(brand)
        results.append(stats)
        print(
            f"{stats['make']:<16} "
            f"{stats['total_listings']:>8,} "
            f"{stats['avg_price']:>11,} CZK"
            f"{stats['min_price']:>11,} CZK"
            f"{stats['max_price']:>11,} CZK"
            f"{stats['avg_mileage']:>10,} km"
        )

    # Summary
    print(f"\n{'='*60}")
    cheapest = min(results, key=lambda x: x["avg_price"])
    most_listed = max(results, key=lambda x: x["total_listings"])
    print(f"Cheapest brand (avg):   {cheapest['make']} ({cheapest['avg_price']:,} CZK)")
    print(f"Most listings:          {most_listed['make']} ({most_listed['total_listings']:,})")


if __name__ == "__main__":
    main()
