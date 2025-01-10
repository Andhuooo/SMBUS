import smbus2

# Define the SMBus bus number
SMBUS_BUS = 2  # Change this based on your system's SMBus (e.g., i2c-2)

# The address of the SMBus device (replace this with your device's address)
DEVICE_ADDRESS = 0x48  # For example, LM75 temperature sensor address

# Register to read from (the register depends on the device)
REGISTER = 0x00  # Register to read (0x00 is often the temperature register for some sensors)

def scan_smbus(bus_number):
    """
    Scan the SMBus and return a list of active device addresses.
    """
    bus = smbus2.SMBus(bus_number)
    devices = []
    try:
        for address in range(0x03, 0x78):  # Common SMBus/I2C address range
            try:
                bus.write_quick(address)
                devices.append(address)
            except OSError:
                pass  # Device not found at this address
    except Exception as e:
        print(f"Error during SMBus scan: {e}")
    finally:
        bus.close()
    return devices

def read_from_smbus(bus_number, device_address, register):
    try:
        # Initialize the SMBus
        bus = smbus2.SMBus(bus_number)
        
        # Read one byte of data from the device at the given register
        data = bus.read_byte_data(device_address, register)
        
        # Close the bus
        bus.close()
        
        # Return the read data
        return data
    except Exception as e:
        print(f"Error reading from device: {e}")
        return None

def main():
    # Scan the SMBus for devices
    print("Scanning SMBus...")
    devices = scan_smbus(SMBUS_BUS)
    
    if devices:
        print(f"Devices found on SMBus {SMBUS_BUS}: {', '.join([f'0x{addr:02X}' for addr in devices])}")
    else:
        print("No devices found on the SMBus.")
        return

    # Read data from the specified device
    if DEVICE_ADDRESS in devices:
        data = read_from_smbus(SMBUS_BUS, DEVICE_ADDRESS, REGISTER)
        
        if data is not None:
            print(f"Data read from device at address 0x{DEVICE_ADDRESS:02X}, register 0x{REGISTER:02X}: {data}")
        else:
            print("Failed to read data from the specified device.")
    else:
        print(f"Device at address 0x{DEVICE_ADDRESS:02X} not found in scan results.")

if __name__ == "__main__":
    main()
