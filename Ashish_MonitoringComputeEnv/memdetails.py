import psutil

def bytes_to_kb(bytes_value):
    return bytes_value / 1024

def get_memory_details(pid):
    try:
        process = psutil.Process(pid)
        memory_info = process.memory_full_info()

        base_address = hex(memory_info.uss)
        memory_type = "Private" if memory_info.private else "Mapped"
        size_kb = bytes_to_kb(memory_info.rss)
        protection_kb = bytes_to_kb(memory_info.rss)
        use_kb = bytes_to_kb(memory_info.uss)
        total_ws_kb = bytes_to_kb(memory_info.vms)
        private_ws_kb = bytes_to_kb(memory_info.private)
        shareable_ws_kb = total_ws_kb - private_ws_kb

        print(f"Memory Details for Process with PID {pid}:")
        print("Base Address:", base_address)
        print("Type:", memory_type)
        print("Size:", size_kb, "KB")
        print("Protection:", protection_kb, "KB")
        print("Use:", use_kb, "KB")
        print("Total WS:", total_ws_kb, "KB")
        print("Private WS:", private_ws_kb, "KB")
        print("Shareable WS:", shareable_ws_kb, "KB")

    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}")
    except psutil.AccessDenied:
        print("Access denied. Run the script as an administrator or with appropriate permissions.")

if __name__ == "__main__":
    target_pid = int(input("Enter the pid from newly created process: "))  # Replace with the PID of the process you want to examine
    get_memory_details(target_pid)
