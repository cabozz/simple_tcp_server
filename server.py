import socket
import signal
import sys
import os

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 6000))  # Fly.io assigns $PORT

# Create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print(f"SERVIDOR STARTED, listening on {HOST}:{PORT}")

# Handle termination signals gracefully
def shutdown(signum, frame):
    print("Signal received, shutting down server...")
    s.close()
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)

# Accept connections
while True:
    try:
        conn, addr = s.accept()
        print("Client connected:", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received:", data.decode())
            conn.sendall(b"ACK: " + data)
        conn.close()
        print("Client disconnected:", addr)
    except OSError:
        # Socket closed, exit loop
        break
