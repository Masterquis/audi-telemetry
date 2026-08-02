from dataclasses import dataclass
import random
import time

@dataclass 
class Telemetry:
    engine_rpm: int
    vehicle_speed_mph: int
    coolant_temperature_f: int
    battery_voltage: float

telemetry: Telemetry = Telemetry(
    engine_rpm = 850, 
    vehicle_speed_mph = 0, 
    coolant_temperature_f = 190,
    battery_voltage = 12.6
)

def update_telemetry(telemetry: Telemetry) -> None:
    rpm_change: int = random.randint(-5, 5)
    proposed_rpm: int = telemetry.engine_rpm + rpm_change

    telemetry.engine_rpm = max(750, min(proposed_rpm, 900))


def display_telemetry(telemetry: Telemetry) -> None:
    print("=== Audi Telemetry Snapshot ===")
    print()

    print(f"Engine RPM: {telemetry.engine_rpm} RPM")
    print(f"Vehicle Speed: {telemetry.vehicle_speed_mph} mph")
    print(f"Coolant Temperature: {telemetry.coolant_temperature_f} °F")
    print(f"Battery Voltage: {telemetry.battery_voltage} V")
    print()

while True:
    update_telemetry(telemetry)
    display_telemetry(telemetry)
    time.sleep(1)
