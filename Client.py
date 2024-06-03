import socket
import threading


port = 11222


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except Exception as e:
            print(f"Error: {e}")
            print("Connection closed by the server.")
            client_socket.close()
            break


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', port))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        if message.lower() == 'exit':
            client_socket.close()
            break
        try:
            client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Send error: {e}")
            client_socket.close()
            break


if __name__ == "__main__":
    start_client()
