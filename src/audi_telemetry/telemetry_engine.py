from dataclasses import dataclass
import random
import time

@dataclass 
class Telemetry:
    engine_rpm: int
    vehicle_speed_mph: int
    coolant_temperature_f: int
    battery_voltage: float

def generate_telemetry() -> Telemetry:
    engine_rpm: int = random.randint(750, 900)
    vehicle_speed_mph: int = 0
    coolant_temperature_f: int = 190
    battery_voltage: float = 12.6

    return Telemetry(
        engine_rpm=engine_rpm, 
        vehicle_speed_mph=vehicle_speed_mph, 
        coolant_temperature_f=coolant_temperature_f,
        battery_voltage=battery_voltage
    )

def display_telemetry(telemetry: Telemetry) -> None:
    print("=== Audi Telemetry Snapshot ===")
    print()

    print(f"Engine RPM: {telemetry.engine_rpm} RPM")
    print(f"Vehicle Speed: {telemetry.vehicle_speed_mph} mph")
    print(f"Coolant Temperature: {telemetry.coolant_temperature_f} °F")
    print(f"Battery Voltage: {telemetry.battery_voltage} V")
    print()

while True:
    telemetry: Telemetry = generate_telemetry()
    display_telemetry(telemetry)
    time.sleep(1)
