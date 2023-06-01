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
    for carrier, rate in carrier_rates.items():
        cost = rate * num_pallets
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
    "Carrier A": 50,  # Rate per pallet
    "Carrier B": 60,
    "Carrier C": 55,
}

best_carrier, shipping_cost = calculate_shipping_cost(num_pallets, carrier_rates)

print("Number of pallets needed:", num_pallets)
print("Best carrier option:", best_carrier)
print("Shipping cost:", shipping_cost)
