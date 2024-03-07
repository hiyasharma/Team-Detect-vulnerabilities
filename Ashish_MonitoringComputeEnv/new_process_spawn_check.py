import psutil

def display_new_processes():
    existing_processes = set(psutil.pids())

    print("{:<8} {:<25} {:<40} {:>10} {:>10} {:<25} {:>10} {:>10}".format(
        "PID", "Name", "Command Line", "CPU (%)", "Memory (MB)", "Connection Type", "Sent (KB)", "Recv (KB)"))
    print("-" * 128)

    while True:
        current_processes = set(psutil.pids())
        new_processes = current_processes - existing_processes

        max_name_len = max_cmd_len = 25
        for pid in new_processes:
            try:
                process = psutil.Process(pid)
                name_len = len(process.name())
                cmd_len = len(" ".join(process.cmdline()))
                max_name_len = max(max_name_len, name_len)
                max_cmd_len = max(max_cmd_len, cmd_len)
            except psutil.NoSuchProcess:
                # Handle the case when the process no longer exists
                continue

        for pid in new_processes:
            try:
                process = psutil.Process(pid)

                pid_str = str(process.pid)
                name = process.name()
                cmdline = " ".join(process.cmdline())
                cpu_percent = process.cpu_percent(interval=0.1)
                memory_mb = process.memory_info().rss / (1024 * 1024)  # Convert bytes to MB

                connections = process.connections()
                if connections:
                    connection = connections[0]
                    conn_type = connection.type
                    sent_kb = connection.bytes_sent / 1024  # Convert bytes to KB
                    recv_kb = connection.bytes_recv / 1024  # Convert bytes to KB
                else:
                    conn_type = "N/A"
                    sent_kb = 0
                    recv_kb = 0

                print("{:<8} {:<{name_len}} {:<{cmd_len}} {:>10.2f} {:>10.2f} {:<25} {:>10.2f} {:>10.2f}".format(
                    pid_str, name, cmdline, cpu_percent, memory_mb, conn_type, sent_kb, recv_kb,
                    name_len=max_name_len, cmd_len=max_cmd_len))
            except psutil.NoSuchProcess:
                # Handle the case when the process no longer exists
                continue

        existing_processes = current_processes

if __name__ == "__main__":
    display_new_processes()
