import os
import random
import time
import subprocess

class Device:
    def __init__(self, device_id, bus, status="Enabled"):
        self.device_id = device_id
        self.bus = bus
        self.status = status

    def disable(self):
        if self.status == "Enabled":
            self.status = "Disabled"
            print(f"Device {self.device_id} on bus {self.bus} has been disabled.")
        else:
            print(f"Device {self.device_id} is already disabled.")

    def enable(self):
        if self.status == "Disabled":
            self.status = "Enabled"
            print(f"Device {self.device_id} on bus {self.bus} has been enabled.")
        else:
            print(f"Device {self.device_id} is already enabled.")

class DeviceNode:
    def __init__(self, handle, path, device_id):
        self.handle = handle
        self.path = path
        self.device_id = device_id

    def delete(self):
        print(f"Deleted device node {self.path}")

    def rename(self, new_path):
        print(f"Renamed device node {self.path} to {new_path}")
        self.path = new_path

class DiskGeometry:
    def __init__(self, disk_id, size):
        self.disk_id = disk_id
        self.size = size

class Partition:
    def __init__(self, partition_id, start_sector, size):
        self.partition_id = partition_id
        self.start_sector = start_sector
        self.size = size

class DeviceManager:
    def __init__(self):
        self.devices = {}
        self.device_nodes = {}
        self.disk_partitions = {}

    def register_device(self, device_id, bus):
        if device_id not in self.devices:
            self.devices[device_id] = Device(device_id, bus)
            print(f"Registered device {device_id} on bus {bus}.")
        else:
            print(f"Device {device_id} is already registered.")

    def disable_device_on_bus(self, device_id, bus):
        if device_id in self.devices and self.devices[device_id].bus == bus:
            self.devices[device_id].disable()
        else:
            print(f"Device {device_id} not found on bus {bus}.")

    def disable_device(self, device_id):
        if device_id in self.devices:
            self.devices[device_id].disable()
        else:
            print(f"Device {device_id} not found.")

    def enable_devices_on_bus(self, bus):
        for device_id, device in self.devices.items():
            if device.bus == bus:
                device.enable()

    def enable_all_devices(self):
        for device_id, device in self.devices.items():
            device.enable()

    def create_device_node(self, device_id, path):
        if device_id in self.devices:
            handle = random.randint(1000, 9999)
            node = DeviceNode(handle, path, device_id)
            self.device_nodes[handle] = node
            print(f"Created device node {path} for device {device_id}.")
            return handle
        else:
            print(f"Device {device_id} not found.")

    def delete_device_node(self, handle):
        if handle in self.device_nodes:
            self.device_nodes[handle].delete()
            del self.device_nodes[handle]
        else:
            print(f"Device node with handle {handle} not found.")

    def rename_device_node(self, handle, new_path):
        if handle in self.device_nodes:
            self.device_nodes[handle].rename(new_path)
        else:
            print(f"Device node with handle {handle} not found.")

    def decode_disk_partitions(self, disk_id, partitions):
        disk = DiskGeometry(disk_id, random.randint(100, 1000))
        self.disk_partitions[disk_id] = [Partition(i, random.randint(0, disk.size), random.randint(1, 100)) for i in range(partitions)]
        print(f"Decoded disk partitions for disk {disk_id}")

    def based_open(self, root_fd, path, flags):
        print(f"Opened file {path} with flags {flags} relative to directory with file descriptor {root_fd}")

    def freadlink(self, file_fd, buffer_size):
        print(f"Reading content of symlink with file descriptor {file_fd} into buffer with size {buffer_size}")

def generate_graph(manager):
    dot_file = "device_management.dot"
    with open(dot_file, "w") as f:
        f.write("digraph DeviceManagement {\n")
        for device_id, device in manager.devices.items():
            f.write(f'    {device_id} [label="Device {device_id}\\n{device.bus}\\n{device.status}", shape="box", color="blue", style="filled", fillcolor="lightblue"];\n')
        for handle, node in manager.device_nodes.items():
            f.write(f'    node_{handle} [label="Device Node\\nHandle: {handle}\\nPath: {node.path}", shape="ellipse", color="green", style="filled", fillcolor="lightgreen"];\n')
        for disk_id, partitions in manager.disk_partitions.items():
            for partition in partitions:
                f.write(f'    {partition.partition_id} [label="Partition {partition.partition_id}\\nDisk: {disk_id}\\nStart Sector: {partition.start_sector}\\nSize: {partition.size}", shape="diamond", color="red", style="filled", fillcolor="lightcoral"];\n')
                f.write(f'    {partition.partition_id} -> {disk_id} [color="gray"];\n')
        for handle, node in manager.device_nodes.items():
            f.write(f'    {node.device_id} -> node_{handle} [color="green"];\n')
        f.write("}\n")
    return dot_file

def render_graph(dot_file):
    output_file = dot_file.replace(".dot", ".png")
    subprocess.run(["dot", "-Tpng", dot_file, "-o", output_file], check=True)
    print(f"Graphviz output saved to {output_file}")

# Example usage with graph generation
def main():
    manager = DeviceManager()

    manager.register_device(1, "pci")
    manager.register_device(2, "pci")
    manager.register_device(3, "usb")

    manager.disable_device_on_bus(2, "pci")
    manager.enable_devices_on_bus("pci")
    manager.enable_all_devices()

    handle = manager.create_device_node(1, "/dev/device1")
    manager.rename_device_node(handle, "/dev/new_device1")
    manager.delete_device_node(handle)

    manager.decode_disk_partitions(1, 4)

    manager.based_open(10, "file.txt", os.O_RDONLY)
    manager.freadlink(20, 256)

    dot_file = generate_graph(manager)
    render_graph(dot_file)

if __name__ == "__main__":
    main()
