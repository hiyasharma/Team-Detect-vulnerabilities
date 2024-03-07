import psutil

def display_specific_processes(process_name=None, process_id=None, command_line=None):
    existing_processes = set(psutil.pids())

    print("{:<8} {:<25} {}".format("PID", "Name", "Command Line"))
    print("-" * 50)

    while True:
        current_processes = set(psutil.pids())
        new_processes = current_processes - existing_processes

        for pid in new_processes:
            process = psutil.Process(pid)

            if process_name and process_name.lower() not in process.name().lower():
                continue

            if process_id and pid != process_id:
                continue

            if command_line and command_line not in " ".join(process.cmdline()):
                continue

            pid_str = str(process.pid)
            name = process.name()
            cmdline = " ".join(process.cmdline())
            print("{:<8} {:<25} {}".format(pid_str, name, cmdline))

        existing_processes = current_processes

if __name__ == "__main__":
    process_name_filter = input("Enter process name filter (leave empty for all processes): ")
    process_id_filter = input("Enter process ID filter (leave empty for all processes): ")
    command_line_filter = input("Enter command line filter (leave empty for all processes): ")

    try:
        process_id_filter = int(process_id_filter)
    except ValueError:
        process_id_filter = None

    display_specific_processes(process_name=process_name_filter, process_id=process_id_filter, command_line=command_line_filter)
