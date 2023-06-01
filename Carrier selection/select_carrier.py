import math

def calculate_pallets(packages, pallet_length, pallet_width, pallet_height):
    total_volume = 0
    for package in packages:
        total_volume += package["length"] * package["width"] * package["height"] * package["quantity"]

    pallet_volume = pallet_length * pallet_width * pallet_height
    return math.ceil(total_volume / pallet_volume)

def calculate_shipping_cost(num_pallets, carrier_rates):
    min_cost = float("inf")
    best_carrier = None
    for carrier, rate_info in carrier_rates.items():
        rate_per_pallet = rate_info["rate_per_pallet"]
        graduated_prices = rate_info.get("graduated_prices", {})
        
        # Check if graduated prices apply
        for threshold, price in graduated_prices.items():
            if num_pallets >= threshold:
                rate_per_pallet = price
                break
        
        cost = rate_per_pallet * num_pallets
        if cost < min_cost:
            min_cost = cost
            best_carrier = carrier
    return best_carrier, min_cost

# Example usage
packages = [
    {"length": 10, "width": 10, "height": 10, "quantity": 2},
    {"length": 20, "width": 20, "height": 10, "quantity": 5},
    {"length": 30, "width": 10, "height": 10, "quantity": 3},
]
pallet_length = 100
pallet_width = 100
pallet_height = 120

num_pallets = calculate_pallets(packages, pallet_length, pallet_width, pallet_height)

carrier_rates = {
    "Carrier A": {
        "rate_per_pallet": 50,  # Rate per pallet
        "graduated_prices": {
            5: 45,  # $45 per pallet for 5 or more pallets
            10: 40,  # $40 per pallet for 10 or more pallets
        }
    },
    "Carrier B": {
        "rate_per_pallet": 60,
        "graduated_prices": {
            5: 55,
            10: 50,
        }
    },
    "Carrier C": {
        "rate_per_pallet": 55,
        "graduated_prices": {
            5: 50,
            10: 45,
        }
    },
}

best_carrier, shipping_cost = calculate_shipping_cost(num_pallets, carrier_rates)

print("Number of pallets needed:", num_pallets)
print("Best carrier option:", best_carrier)
print("Shipping cost:", shipping_cost)
