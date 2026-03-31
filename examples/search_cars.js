/**
 * Search for cars on Sauto.cz with filters (Node.js example).
 *
 * Usage:
 *   npm install axios
 *   node search_cars.js
 *
 * Get your API key at: https://rapidapi.com/XrayHunter-F8lHMI9me/api/sauto-cz-czech-cars-api
 */

const axios = require('axios');

const API_KEY = 'YOUR_API_KEY'; // Replace with your RapidAPI key
const BASE_URL = 'https://sauto-cz-czech-cars-api.p.rapidapi.com';
const HEADERS = {
    'X-RapidAPI-Key': API_KEY,
    'X-RapidAPI-Host': 'sauto-cz-czech-cars-api.p.rapidapi.com',
};

async function search(params) {
    const { data } = await axios.get(`${BASE_URL}/search`, { headers: HEADERS, params });
    return data;
}

async function getVehicle(id) {
    const { data } = await axios.get(`${BASE_URL}/vehicle/${id}`, { headers: HEADERS });
    return data;
}

async function main() {
    // Search for SUVs with automatic gearbox
    console.log('=== SUVs with Automatic Gearbox ===\n');
    const data = await search({
        gearbox: 'automatic',
        drive: '4x4',
        price_max: 800000,
        per_page: 5,
    });

    console.log(`Found ${data.total_count} cars\n`);
    for (const car of data.results) {
        console.log(`  ${car.make} ${car.model} (${car.year_manufactured})`);
        console.log(`    Price: ${car.price?.toLocaleString()} CZK | Mileage: ${car.mileage_km?.toLocaleString()} km`);
        console.log(`    Fuel: ${car.fuel} | Gearbox: ${car.gearbox}`);
        console.log();
    }

    // Get full detail for first result
    if (data.results.length > 0) {
        const id = data.results[0].id;
        console.log(`\n=== Full Detail for ID ${id} ===\n`);
        const detail = await getVehicle(id);

        console.log(`${detail.make} ${detail.model} (${detail.year_manufactured})`);
        console.log(`VIN: ${detail.vin}`);
        console.log(`Price: ${detail.pricing.price?.toLocaleString()} CZK`);
        console.log(`Engine: ${detail.engine_power_kw} kW (${detail.engine_power_hp} HP), ${detail.engine_volume_cc} cc`);
        console.log(`Equipment: ${detail.equipment.length} items`);
        console.log(`Photos: ${detail.images.length}`);
        console.log(`Seller: ${detail.seller.phone} (${detail.seller.type})`);
    }
}

main().catch(console.error);
