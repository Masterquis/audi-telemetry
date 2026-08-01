import random
import time

def generate_telemetry() -> tuple[int, int, int, float]:
    engine_rpm: int = random.randint(750, 900)
    vehicle_speed_mph: int = 0
    coolant_temperature_f: int = 190
    battery_voltage: float = 12.6

    return engine_rpm, vehicle_speed_mph, coolant_temperature_f, battery_voltage

def display_telemetry(engine_rpm: int, vehicle_speed_mph: int, coolant_temperature_f: int, battery_voltage: float) -> None:
    print("=== Audi Telemetry Snapshot ===")
    print()

    print(f"Engine RPM: {engine_rpm} RPM")
    print(f"Vehicle Speed: {vehicle_speed_mph} mph")
    print(f"Coolant Temperature: {coolant_temperature_f} °F")
    print(f"Battery Voltage: {battery_voltage} V")
    print()

while True:
    engine_rpm, vehicle_speed_mph, coolant_temperature_f, battery_voltage = generate_telemetry()
    display_telemetry(engine_rpm, vehicle_speed_mph, coolant_temperature_f, battery_voltage)
    time.sleep(1)
