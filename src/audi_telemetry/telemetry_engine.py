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
    coolant_temperature_f = 70,
    battery_voltage = 14.2
)

def update_telemetry(telemetry: Telemetry) -> None:
    rpm_change: int = random.randint(-5, 5)
    proposed_rpm: int = telemetry.engine_rpm + rpm_change
    telemetry.engine_rpm = max(750, min(proposed_rpm, 900))

    speed_change: int = random.randint(-2, 3)
    proposed_speed: int = telemetry.vehicle_speed_mph + speed_change
    telemetry.vehicle_speed_mph = max(0, min(proposed_speed, 70))

    if telemetry.coolant_temperature_f < 185:
        temperature_change: int = random.randint(1, 3)
    else:
        temperature_change: int = random.randint(-1, 1)

    proposed_temperature: int = telemetry.coolant_temperature_f + temperature_change
    telemetry.coolant_temperature_f = max(70, min(proposed_temperature, 195))

    voltage_change: float = random.uniform(-0.1, 0.1)
    proposed_voltage: float = telemetry.battery_voltage + voltage_change
    telemetry.battery_voltage = round(max(13.5, min(proposed_voltage, 14.8)), 2)



def display_telemetry(telemetry: Telemetry) -> None:
    print("=== Audi Telemetry Snapshot ===")
    print()

    print(f"Engine RPM: {telemetry.engine_rpm} RPM")
    print(f"Vehicle Speed: {telemetry.vehicle_speed_mph} mph")
    print(f"Coolant Temperature: {telemetry.coolant_temperature_f} °F")
    print(f"Battery Voltage: {telemetry.battery_voltage:.2f} V")
    print()

while True:
    update_telemetry(telemetry)
    display_telemetry(telemetry)
    time.sleep(1)
