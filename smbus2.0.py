import smbus2
import argparse
import time
import json

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
    """
    Read a single byte of data from a specific register of an SMBus device.
    """
    try:
        bus = smbus2.SMBus(bus_number)
        data = bus.read_byte_data(device_address, register)
        bus.close()
        return data
    except Exception as e:
        print(f"Error reading from device: {e}")
        return None

def write_to_smbus(bus_number, device_address, register, data):
    """
    Write a single byte of data to a specific register of an SMBus device.
    """
    try:
        bus = smbus2.SMBus(bus_number)
        bus.write_byte_data(device_address, register, data)
        bus.close()
        print(f"Successfully wrote {data} to register 0x{register:02X} on device 0x{device_address:02X}.")
    except Exception as e:
        print(f"Error writing to device: {e}")

def save_results_to_file(filename, results):
    """
    Save scan results to a JSON file.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(results, file, indent=4)
        print(f"Scan results saved to {filename}.")
    except Exception as e:
        print(f"Error saving scan results: {e}")

def monitor_device(bus_number, device_address, register, interval, duration):
    """
    Monitor real-time data from a device and print it at specified intervals.
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        data = read_from_smbus(bus_number, device_address, register)
        if data is not None:
            print(f"Real-time data from device 0x{device_address:02X}, register 0x{register:02X}: {data}")
        time.sleep(interval)

def main():
    parser = argparse.ArgumentParser(description="Enhanced SMBus/I2C Device Tool")
    parser.add_argument("bus_number", type=int, help="The SMBus number to use (e.g., 2 for i2c-2).")
    parser.add_argument("--scan", action="store_true", help="Scan the SMBus for devices.")
    parser.add_argument("--read", nargs=2, metavar=("DEVICE_ADDRESS", "REGISTER"), help="Read data from a device register.")
    parser.add_argument("--write", nargs=3, metavar=("DEVICE_ADDRESS", "REGISTER", "DATA"), help="Write data to a device register.")
    parser.add_argument("--save", metavar="FILENAME", help="Save scan results to a file.")
    parser.add_argument("--monitor", nargs=4, metavar=("DEVICE_ADDRESS", "REGISTER", "INTERVAL", "DURATION"),
                        help="Monitor real-time data from a device.")
    
    args = parser.parse_args()

    if args.scan:
        print("Scanning SMBus...")
        devices = scan_smbus(args.bus_number)
        if devices:
            print(f"Devices found on SMBus {args.bus_number}: {', '.join([f'0x{addr:02X}' for addr in devices])}")
        else:
            print("No devices found on the SMBus.")
        if args.save:
            save_results_to_file(args.save, devices)
    
    if args.read:
        device_address = int(args.read[0], 16)
        register = int(args.read[1], 16)
        data = read_from_smbus(args.bus_number, device_address, register)
        if data is not None:
            print(f"Data read from device 0x{device_address:02X}, register 0x{register:02X}: {data}")
    
    if args.write:
        device_address = int(args.write[0], 16)
        register = int(args.write[1], 16)
        data = int(args.write[2], 10)
        write_to_smbus(args.bus_number, device_address, register, data)
    
    if args.monitor:
        device_address = int(args.monitor[0], 16)
        register = int(args.monitor[1], 16)
        interval = float(args.monitor[2])
        duration = float(args.monitor[3])
        monitor_device(args.bus_number, device_address, register, interval, duration)

if __name__ == "__main__":
    main()
