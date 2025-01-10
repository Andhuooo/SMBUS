# SMBUS
SMBus Device Scanner and Reader

This Python script is designed to interact with the System Management Bus (SMBus), a subset of the I2C protocol. It provides functionality to:

    Scan the SMBus for connected devices.

    Read data from a specific device and register on the SMBus.

Requirements
Hardware

    A system with SMBus/I2C hardware (e.g., a Raspberry Pi or a similar embedded device).

    Devices connected to the SMBus/I2C bus.

Software

    Python 3.x

    smbus2 library

Installation

    Install Python 3.x on your system if not already installed.

    Install the smbus2 library:
    pip install smbus2

Usage
Code Overview
Constants

    SMBUS_BUS: Specifies the SMBus bus number (e.g., 2 for /dev/i2c-2).

    DEVICE_ADDRESS: The address of the target device (e.g., 0x48 for a temperature sensor).

    REGISTER: The register to read data from (e.g., 0x00).

Functions

    scan_smbus(bus_number):

        Scans the specified SMBus for active devices.

        Returns a list of detected device addresses.

    read_from_smbus(bus_number, device_address, register):

        Reads a byte of data from the specified register on the target device.

    main():

        Scans the SMBus for devices.

        If the target device is found, reads data from its register and prints the result.

Running the Script

    Connect your SMBus/I2C devices to the system.

    Update the constants SMBUS_BUS, DEVICE_ADDRESS, and REGISTER in the script to match your configuration.

    Run the script:
    python smbus_device_scan.py

Example Output

    When devices are found:
    Scanning SMBus...
    Devices found on SMBus 2: 0x48, 0x50
    Data read from device at address 0x48, register 0x00: 25

    When no devices are found:
    Scanning SMBus...
    No devices found on the SMBus.

Troubleshooting

    No devices detected:

        Ensure the devices are properly connected to the SMBus.

        Verify that the correct bus number (SMBUS_BUS) is specified.

    Permission denied:

        Ensure you have the necessary permissions to access the SMBus.

        Run the script with elevated privileges:
        sudo python smbus_device_scan.py

    Incorrect readings:

        Verify the DEVICE_ADDRESS and REGISTER values against the device's datasheet.

Customization

    Modify the DEVICE_ADDRESS and REGISTER constants to target different devices and registers.

    Extend the script to write data to a device using the write_byte_data() method from smbus2.

License

This script is provided under the MIT License. You are free to use, modify, and distribute it as needed.

For more information about SMBus/I2C devices, refer to the device's datasheet or the SMBus/I2C specifications.


