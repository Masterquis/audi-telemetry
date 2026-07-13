import random
import time


vehicle_speed_mph: int = 0
coolant_temperature_f: int = 190
battery_voltage: float = 12.6

while True:
    engine_rpm: int = random.randint(750, 900)
    print("=== Audi Telemetry Snapshot ===")
    print()

    print(f"Engine RPM: {engine_rpm} RPM")
    print(f"Vehicle Speed: {vehicle_speed_mph} mph")
    print(f"Coolant Temperature: {coolant_temperature_f} °F")
    print(f"Battery Voltage: {battery_voltage} V")
    print()

    time.sleep(1)
