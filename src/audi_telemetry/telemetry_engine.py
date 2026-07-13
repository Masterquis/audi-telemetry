import random
import time

vehicle_speed_mph: int = 0
coolant_temperature_f: int = 190
battery_voltage: float = 12.6

def generate_telemetry() -> int: 
    engine_rpm: int = random.randint(750, 900)
    return engine_rpm

def display_telemetry(engine_rpm) -> None:
    print("=== Audi Telemetry Snapshot ===")
    print()

    print(f"Engine RPM: {engine_rpm} RPM")
    print(f"Vehicle Speed: {vehicle_speed_mph} mph")
    print(f"Coolant Temperature: {coolant_temperature_f} °F")
    print(f"Battery Voltage: {battery_voltage} V")
    print()

while True:
    engine_rpm: int = generate_telemetry()
    display_telemetry(engine_rpm)
    time.sleep(1)
