import usb.core
import usb.util

# Find the USB device
vendor_id = 0x1234  # Replace with actual vendor ID
product_id = 0x5678  # Replace with actual product ID
dev = usb.core.find(idVendor=vendor_id, idProduct=product_id)

if dev is None:
    raise ValueError('Device not found')

# Initialize the device
dev.set_configuration()
endpoint = dev[0][(0, 0)][0]

# Capture fingerprint image
try:
    print("Place your thumb on the scanner...")
    while True:
        data = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
        # Process data here
except KeyboardInterrupt:
    pass
finally:
    usb.util.dispose_resources(dev)
