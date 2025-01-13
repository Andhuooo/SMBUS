README for SMBus/I2C Device Tool
Description

This Python script provides tools for interacting with SMBus/I2C devices. It supports scanning for devices, reading from and writing to device registers, saving scan results, and real-time data monitoring.
Features

    Scan SMBus: Identify active I2C devices on the bus.
    Read Data: Read a byte of data from a specific device register.
    Write Data: Write a byte of data to a specific device register.
    Save Scan Results: Save detected device addresses to a JSON file.
    Real-Time Monitoring: Continuously read and display data at regular intervals.

Requirements

    Python 3
    smbus2 library: Install using pip install smbus2.

    Note: The script is designed for Linux systems, as Windows does not support smbus2 due to the dependency on fcntl.

Usage

Run the script with the following command-line arguments:

    Scan SMBus:

python smbus.py <bus_number> --scan

Save Scan Results to File:

python smbus.py <bus_number> --scan --save <filename>

Read from Device:

python smbus.py <bus_number> --read <device_address> <register>

Example:

python smbus.py 2 --read 0x48 0x00

Write to Device:

python smbus.py <bus_number> --write <device_address> <register> <data>

Example:

python smbus.py 2 --write 0x48 0x01 100

Real-Time Monitoring:

python smbus.py <bus_number> --monitor <device_address> <register> <interval> <duration>

Example:

    python smbus.py 2 --monitor 0x48 0x00 1 10

Notes

    Replace <bus_number>, <device_address>, <register>, etc., with the appropriate values for your system and devices.
    The SMBus number corresponds to i2c-X on Linux (e.g., 2 for /dev/i2c-2).

