
import socket
import sys
import time


usage = "python3 portscan.py TARGET START_PORT END_PORT"

print("-"*100)
print("Port Scanner saranya")
print("-"*100)

if(len(sys.argv) !=4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error : ")
    sys.exit()



start_port = int(sys.argv[2])
end_port = int(sys.argv[3])
print("Scanning target",target)

for port in range(start_port , end_port):
    print("Scanning port:",port)

    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target , port))
    if(not conn):
        print("Port {} is OPEN", format(port))
    s.close()

