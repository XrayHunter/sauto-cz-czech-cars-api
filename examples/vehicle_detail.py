"""
Fetch full vehicle detail including VIN, equipment list, and seller info.

Usage:
    pip install requests
    python vehicle_detail.py

Get your API key at: https://rapidapi.com/XrayHunter-F8lHMI9me/api/sauto-cz-czech-cars-api
"""

import requests

API_KEY = "YOUR_API_KEY"  # Replace with your RapidAPI key
BASE_URL = "https://sauto-cz-czech-cars-api.p.rapidapi.com"
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "sauto-cz-czech-cars-api.p.rapidapi.com",
}


def get_vehicle(vehicle_id: int) -> dict:
    response = requests.get(f"{BASE_URL}/vehicle/{vehicle_id}", headers=HEADERS)
    response.raise_for_status()
    return response.json()


def main():
    # First, search for a car to get its ID
    search_resp = requests.get(
        f"{BASE_URL}/search",
        headers=HEADERS,
        params={"make": "skoda", "model": "octavia", "per_page": 1},
    )
    search_data = search_resp.json()

    if not search_data["results"]:
        print("No cars found")
        return

    vehicle_id = search_data["results"][0]["id"]
    print(f"Fetching detail for vehicle ID: {vehicle_id}\n")

    # Get full detail
    car = get_vehicle(vehicle_id)

    # Basic info
    print(f"{'='*60}")
    print(f"{car['make']} {car['model']} ({car['year_manufactured']})")
    print(f"{'='*60}")
    print(f"Condition:  {car['condition']}")
    print(f"VIN:        {car['vin']}")
    print(f"URL:        {car['url']}")

    # Pricing
    p = car["pricing"]
    print(f"\n--- Pricing ---")
    print(f"Price:      {p['price']:,} CZK" if p["price"] else "Price: N/A")
    if p.get("leasing_price"):
        print(f"Leasing:    {p['leasing_price']:,} CZK/month")
    if p.get("price_note"):
        print(f"Note:       {p['price_note']}")

    # Engine & drivetrain
    print(f"\n--- Engine ---")
    print(f"Power:      {car['engine_power_kw']} kW / {car['engine_power_hp']} HP")
    print(f"Displ.:     {car['engine_volume_cc']} cc")
    print(f"Fuel:       {car['fuel']}")
    print(f"Gearbox:    {car['gearbox']} ({car.get('gearbox_levels', 'N/A')})")
    print(f"Drive:      {car['drive']}")
    if car.get("average_fuel_consumption"):
        print(f"Fuel cons.: {car['average_fuel_consumption']} l/100km")

    # Body
    print(f"\n--- Body ---")
    print(f"Type:       {car['body_type']}")
    print(f"Doors:      {car['doors']}")
    print(f"Seats:      {car['seats']}")
    print(f"Color:      {car['color']} ({car.get('color_tone', '')})")

    # History
    print(f"\n--- History ---")
    print(f"Mileage:    {car['mileage_km']:,} km" if car["mileage_km"] else "Mileage: N/A")
    print(f"1st owner:  {car['first_owner']}")
    print(f"Crashed:    {car['crashed']}")
    print(f"Serv. book: {car['service_book']}")
    print(f"Origin:     {car['country_of_origin']}")
    print(f"EURO:       {car['euro_level']}")
    print(f"STK until:  {car['stk_date']}")
    if car.get("guarantee_date"):
        print(f"Warranty:   {car['guarantee_date']}")

    # Equipment
    print(f"\n--- Equipment ({len(car['equipment'])} items) ---")
    categories = {}
    for item in car["equipment"]:
        cat = item["category"]
        categories.setdefault(cat, []).append(item["name"])
    for cat, items in sorted(categories.items()):
        print(f"  [{cat}] {', '.join(items)}")

    # Media
    print(f"\n--- Media ---")
    print(f"Photos:     {len(car['images'])}")
    print(f"Videos:     {len(car['videos'])}")

    # Seller
    print(f"\n--- Seller ---")
    seller = car["seller"]
    print(f"Type:       {seller['type']}")
    print(f"Phone:      {seller['phone']}")
    if seller.get("premise_name"):
        print(f"Dealer:     {seller['premise_name']}")

    # Location
    loc = car["location"]
    print(f"\n--- Location ---")
    print(f"Region:     {loc['region']}")
    print(f"District:   {loc['district']}")
    if loc.get("city"):
        print(f"City:       {loc['city']}")


if __name__ == "__main__":
    main()
