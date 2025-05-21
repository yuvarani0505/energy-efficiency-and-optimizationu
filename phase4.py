import random
import matplotlib.pyplot as plt
# Simulated smart home device data
devices = {
    'Air Conditioner': {'usage_hours': 5, 'power_kw': 1.5},
    'Heater': {'usage_hours': 4, 'power_kw': 2.0},
    'Washing Machine': {'usage_hours': 1, 'power_kw': 0.5},
    'Refrigerator': {'usage_hours': 24, 'power_kw': 0.15},
    'Television': {'usage_hours': 3, 'power_kw': 0.1},
    'Computer': {'usage_hours': 6, 'power_kw': 0.2}
}
# Threshold (in kWh) beyond which usage is considered high
threshold = 3.0
# Calculate and display energy consumption
total_energy = 0
overconsuming_devices = []
print("Device-wise Energy Consumption:")
for device, data in devices.items():
    usage = data['usage_hours'] * data['power_kw']
    total_energy += usage
    print(f"- {device}: {usage:.2f} kWh")
    if usage > threshold:
        overconsuming_devices.append((device, usage))
# Suggest optimizations
print("\nSuggestions for Optimization:")
if overconsuming_devices:
    for device, usage in overconsuming_devices:
        print(f"* {device} uses {usage:.2f} kWh. Consider reducing usage time or upgrading to a more efficient model.")
else:
    print("All devices are within optimal energy consumption limits.")

print(f"\nTotal Energy Consumption: {total_energy:.2f} kWh")
# Visualization
labels = list(devices.keys())
usage_values = [v['usage_hours'] * v['power_kw'] for v in devices.values()]

plt.figure(figsize=(10, 5))
plt.bar(labels, usage_values, color='skyblue')
plt.axhline(y=threshold, color='r', linestyle='--', label='Threshold')
plt.title("Device-wise Energy Usage")
plt.ylabel("Energy (kWh)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

