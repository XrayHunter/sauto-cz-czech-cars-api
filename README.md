# Sauto.cz Czech Cars API

Real-time access to **100,000+ vehicle listings** from [Sauto.cz](https://www.sauto.cz) — the second largest automotive marketplace in the Czech Republic.

Search personal cars, motorcycles, trucks, RVs, and more. Get structured vehicle details including price, mileage, VIN, engine specs, full equipment list (up to 120 items), photos, and seller info.

**[Subscribe on RapidAPI](https://rapidapi.com/XrayHunter-F8lHMI9me/api/sauto-cz-czech-cars-api)** | **[API Documentation](https://rapidapi.com/XrayHunter-F8lHMI9me/api/sauto-cz-czech-cars-api)**

---

## Features

- **100K+ active listings** across 9 vehicle categories
- **171 car brands, 192 motorcycle brands**
- **VIN numbers** for vehicle history checks
- **Full equipment list** — up to 120 items per vehicle (ABS, ESP, navigation, heated seats, cameras...)
- **Powerful search filters** — make, model, fuel, gearbox, drive, condition, price range, mileage range, body type, color
- **Seller contact** — phone number, dealer/private flag, dealership name
- **Real-time data** — fetched directly from Sauto.cz
- **Fast response** — under 2 seconds, cached for performance

## Quick Start

### 1. Get your API key

Sign up at [RapidAPI](https://rapidapi.com/XrayHunter-F8lHMI9me/api/sauto-cz-czech-cars-api) and subscribe to a plan (free tier available — 50 requests/month).

### 2. Make your first request

**Python:**
```python
import requests

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "sauto-cz-czech-cars-api.p.rapidapi.com"
}

# Search for used Skoda Octavia diesel
response = requests.get(
    "https://sauto-cz-czech-cars-api.p.rapidapi.com/search",
    headers=headers,
    params={"make": "skoda", "model": "octavia", "fuel": "diesel", "per_page": 5}
)

data = response.json()
print(f"Found {data['total_count']} cars")
for car in data["results"]:
    print(f"  {car['make']} {car['model']} {car['year_manufactured']} | {car['price']:,} CZK | {car['mileage_km']:,} km")
```

**JavaScript:**
```javascript
const response = await fetch(
  'https://sauto-cz-czech-cars-api.p.rapidapi.com/search?make=skoda&model=octavia&fuel=diesel&per_page=5',
  {
    headers: {
      'X-RapidAPI-Key': 'YOUR_API_KEY',
      'X-RapidAPI-Host': 'sauto-cz-czech-cars-api.p.rapidapi.com'
    }
  }
);
const data = await response.json();
console.log(`Found ${data.total_count} cars`);
data.results.forEach(car => {
  console.log(`  ${car.make} ${car.model} ${car.year_manufactured} | ${car.price} CZK | ${car.mileage_km} km`);
});
```

**cURL:**
```bash
curl "https://sauto-cz-czech-cars-api.p.rapidapi.com/search?make=skoda&model=octavia&fuel=diesel&per_page=5" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: sauto-cz-czech-cars-api.p.rapidapi.com"
```

---

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/search` | Search vehicles with filters |
| GET | `/vehicle/{id}` | Full vehicle detail (VIN, equipment, photos...) |
| GET | `/brands` | List all available manufacturers |
| GET | `/filters` | Get available filter options |
| GET | `/health` | Health check |

---

## Search Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `make` | string | Manufacturer | `skoda`, `bmw`, `toyota` |
| `model` | string | Model (requires make) | `octavia`, `golf`, `corolla` |
| `category` | string | Vehicle type | `personal`, `motorcycle`, `truck`, `rv` |
| `condition` | string | Condition | `new`, `used`, `demo`, `damaged`, `veteran` |
| `fuel` | string | Fuel type | `petrol`, `diesel`, `electric`, `hybrid`, `lpg`, `cng` |
| `gearbox` | string | Transmission | `manual`, `automatic`, `semi-automatic` |
| `drive` | string | Drive type | `fwd`, `rwd`, `4x4` |
| `color` | string | Color (Czech SEO name) | `bila`, `cerna`, `modra`, `cervena` |
| `body_type` | integer | Body type code | Use `/filters` to get codes |
| `price_min` | integer | Min price (CZK) | `100000` |
| `price_max` | integer | Max price (CZK) | `500000` |
| `mileage_min` | integer | Min mileage (km) | `0` |
| `mileage_max` | integer | Max mileage (km) | `50000` |
| `page` | integer | Page number | `1` |
| `per_page` | integer | Results per page (max 100) | `20` |

---

## Vehicle Detail Response

The `/vehicle/{id}` endpoint returns comprehensive data:

| Section | Fields |
|---------|--------|
| **Basic** | make, model, year, condition, category, VIN |
| **Pricing** | price, original price, price without VAT, VAT deductible, leasing price, negotiable |
| **Engine** | power (kW + HP), displacement (cc), fuel, gearbox, gears count, drive, fuel consumption |
| **Body** | body type, doors, seats, color, color tone |
| **History** | first owner, crashed, service book, tuning, country of origin, EURO level |
| **Documents** | STK date (MOT), warranty date |
| **Equipment** | Up to 120 categorized items (safety, assist, systems, interior, exterior, seats, lights, security) |
| **Media** | All photo URLs, video URLs |
| **Seller** | name, phone, private/dealer, dealership name |
| **Location** | region, district, city |

---

## Examples

Check out the [`examples/`](./examples) directory for complete, runnable scripts:

| File | Description |
|------|-------------|
| [`search_cars.py`](./examples/search_cars.py) | Search with filters, display results |
| [`vehicle_detail.py`](./examples/vehicle_detail.py) | Fetch full vehicle detail with equipment |
| [`find_best_deals.py`](./examples/find_best_deals.py) | Find undervalued cars by price/mileage ratio |
| [`brand_analysis.py`](./examples/brand_analysis.py) | Compare average prices across brands |
| [`search_cars.js`](./examples/search_cars.js) | JavaScript/Node.js search example |

---

## Vehicle Categories

| Value | Description | Listings |
|-------|-------------|----------|
| `personal` | Cars (default) | ~98,000 |
| `commercial` | Vans, utility | ~7,000 |
| `truck` | Trucks | ~1,000 |
| `motorcycle` | Motorcycles | ~1,600 |
| `rv` | RVs / Campers | ~1,400 |
| `trailer` | Trailers | varies |
| `quad` | ATVs | varies |
| `bus` | Buses | varies |
| `machine` | Work machines | varies |

---

## Color Reference

| API value | English | Czech |
|-----------|---------|-------|
| `bila` | White | Bila |
| `cerna` | Black | Cerna |
| `seda` | Grey | Seda |
| `stribrna` | Silver | Stribrna |
| `modra` | Blue | Modra |
| `cervena` | Red | Cervena |
| `zelena` | Green | Zelena |
| `hneda` | Brown | Hneda |
| `zluta` | Yellow | Zluta |
| `oranzova` | Orange | Oranzova |

---

## Pricing

| Plan | Price | Requests/month |
|------|-------|----------------|
| Free | $0 | 50 |
| Basic | $9.99 | 1,000 |
| Pro | $29.99 | 10,000 |
| Ultra | $99.99 | 100,000 |

**[Subscribe on RapidAPI](https://rapidapi.com/XrayHunter-F8lHMI9me/api/sauto-cz-czech-cars-api)**

---

## Notes

- Prices are in **Czech Koruna (CZK)**. 1 EUR ~ 25 CZK, 1 USD ~ 23 CZK.
- **VIN numbers** can be used with Cebia, Carfax, or AutoDNA for vehicle history.
- **STK** = Czech vehicle inspection (like MOT in UK, TUV in Germany).
- **Cebia** = Czech equivalent of Carfax (vehicle history reports).
- Equipment names are in Czech. See the [full documentation](https://rapidapi.com/XrayHunter-F8lHMI9me/api/sauto-cz-czech-cars-api) for translations.

---

## Related

- **[Sreality.cz Czech Reality API](https://rapidapi.com/XrayHunter-F8lHMI9me/api/sreality-cz-czech-reality-api1)** — Czech real estate data from Sreality.cz

## License

MIT
