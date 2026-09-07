from dataclasses import dataclass, replace
import logging
import random
import time
import sqlite3
import datetime
import argparse

SAMPLE_INTERVAL_SECONDS = 1
DATABASE_PATH = "telemetry.db"
LOG_LEVEL = logging.INFO


logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

@dataclass 
class Telemetry:
    engine_rpm: int
    vehicle_speed_mph: int
    coolant_temperature_f: int
    battery_voltage: float
    captured_at: datetime.datetime





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


def capture_telemetry(telemetry: Telemetry) -> Telemetry:
    snapshot: Telemetry = replace(telemetry, captured_at = datetime.datetime.now(datetime.timezone.utc)
)
    return snapshot


def display_telemetry(snapshot: Telemetry) -> None:
    local_time = snapshot.captured_at.astimezone()
    formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")


    print("=== Audi Telemetry Snapshot ===")
    print()

    print(f"Engine RPM: {snapshot.engine_rpm} RPM")
    print(f"Vehicle Speed: {snapshot.vehicle_speed_mph} mph")
    print(f"Coolant Temperature: {snapshot.coolant_temperature_f} °F")
    print(f"Battery Voltage: {snapshot.battery_voltage:.2f} V")
    print(f"Timestamp: {formatted_time}")
    print()


def save_telemetry(cursor: sqlite3.Cursor, snapshot: Telemetry) -> None:
    cursor.execute(
        """
        INSERT INTO telemetry(
            captured_at,
            engine_rpm,
            vehicle_speed_mph,
            coolant_temperature_f,
            battery_voltage
        )
        VALUES(?,?,?,?,?)
        """,
        (
            snapshot.captured_at.isoformat(),
            snapshot.engine_rpm,
            snapshot.vehicle_speed_mph,
            snapshot.coolant_temperature_f,
            snapshot.battery_voltage
        )
    )


def initialize_database(connection: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS telemetry (
        id INTEGER PRIMARY KEY,
        captured_at TEXT NOT NULL,
        engine_rpm INTEGER NOT NULL,
        vehicle_speed_mph INTEGER NOT NULL,
        coolant_temperature_f INTEGER NOT NULL,
        battery_voltage REAL NOT NULL
        )
    """)

    connection.commit()

def display_statistics(cursor: sqlite3.Cursor) -> None:
    print()
    print("Telemetry collection stopped.")
    print()

    cursor.execute("""
                    SELECT MAX(engine_rpm),
                    COUNT(*),
                    AVG(battery_voltage),
                    MAX(vehicle_speed_mph),
                    MAX(coolant_temperature_f)
                    FROM telemetry
                """)
            
    highest_rpm, count, avg_voltage, highest_speed, highest_temperature = cursor.fetchone()

    print("=== Telemetry History Statistics ===")

    if count == 0:
        print("No telemetry data available.")
    else:
        print(f"Highest RPM: {highest_rpm} RPM")
        print(f"History Count: {count} entries")
        print(f"Average Battery Voltage: {avg_voltage:.2f} V")
        print(f"Highest Speed: {highest_speed} mph")
        print(f"Highest Coolant Temperature: {highest_temperature} °F")

def positive_float(value: str) -> float:
    try:
        interval = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            "sample interval must be a number greater than 0 seconds"
        )

    if interval <= 0:
        raise argparse.ArgumentTypeError(
            "sample interval must be a number greater than 0 seconds"
        )

    return interval

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--interval",
        type = positive_float,
        default = SAMPLE_INTERVAL_SECONDS,
        help = "Telemetry sample interval in seconds."
    )
    args = parser.parse_args()
    return args

def main() -> None:

    args = parse_arguments()

    print()
    logger.info("Telemetry collector started")
    logger.info("Sample interval: %s seconds", args.interval)
    print()
    telemetry: Telemetry = Telemetry(
        engine_rpm = 850, 
        vehicle_speed_mph = 0, 
        coolant_temperature_f = 70,
        battery_voltage = 14.2,
        captured_at = datetime.datetime.now(datetime.timezone.utc)
    )
    
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    try:

        try:
            initialize_database(connection, cursor)
            logger.info("Database initialized")
        except sqlite3.Error:
            logger.exception("Failed to initialize database.")
            raise

        try:
            while True:
                update_telemetry(telemetry)

                snapshot: Telemetry = capture_telemetry(telemetry)

                try:
                    save_telemetry(cursor, snapshot)
                    connection.commit()
                except sqlite3.Error:
                    logger.exception("Failed to save telemetry snapshot.")
                    raise
                    
                display_telemetry(snapshot)

                time.sleep(args.interval)

        except KeyboardInterrupt:
            logger.info("Telemetry collector stopped by user")
            display_statistics(cursor)
        
    finally:
        connection.close()
        print()
        logger.info("Database connection closed")

if __name__ == "__main__":
    main()