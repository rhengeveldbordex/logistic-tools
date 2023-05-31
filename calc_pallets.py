import math

def calculate_pallets(packages, pallet_length, pallet_width, pallet_height):
    total_volume = 0
    for package in packages:
        total_volume += package["length"] * package["width"] * package["height"] * package["quantity"]

    pallet_volume = pallet_length * pallet_width * pallet_height
    return math.ceil(total_volume / pallet_volume)

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
print("Number of pallets needed:", num_pallets)
