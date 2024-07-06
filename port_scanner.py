import socket
import threading
from queue import Queue

# this is target
target = input("Enter the host to be scanned: ")
# the range of ports to be scanned
port_range = input("Enter the range of ports to scan (e.g. 1-1000): ")
start_port, end_port = map(int, port_range.split('-'))

# Queue to hold the ports to be scanned
queue = Queue()
# List to hold the open ports
open_ports = []



# Function to scan a single port
def scan_port(port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout
        s.settimeout(1)
        # Attempt to connect to the target on the specified port
        s.connect((target, port))
    except:
        # Connection failed, port is closed
        return
    else:
        # Connection succeeded, port is open
        open_ports.append(port)
    finally:
        # Close the socket
        s.close()

# Worker function to process the ports in the queue
def worker():
    while not queue.empty():
        # Get a port from the queue
        port = queue.get()
        # Scan the port
        scan_port(port)
        # Indicate that the task is done
        queue.task_done()

# Populate the queue with the ports to be scanned
for port in range(start_port, end_port + 1):
    queue.put(port)



# Create and start the threads
threads = []
for _ in range(100):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# Wait for all the threads to finish
for t in threads:
    t.join()




# Print the results
if open_ports:
    print(f"Open ports on {target}:")
    for port in open_ports:
        print(port)
else:
    print(f"No open ports found on {target} within the range {start_port}-{end_port}.")
