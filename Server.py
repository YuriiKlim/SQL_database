import socket
import threading
import redis


r = redis.Redis(host='localhost', port=6379, db=0)
port = 11222

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', port))
server_socket.listen()

clients = []


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Client: {message}")
            r.rpush('chat_messages', message)
            broadcast(message, client_socket)
        except Exception as e:
            print(f"Error: {e}")
            if client_socket in clients:
                clients.remove(client_socket)
            client_socket.close()
            break


def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Broadcast error: {e}")
                clients.remove(client)
                client.close()


def handle_server_input():
    while True:
        message = input()
        if message:
            r.rpush('chat_messages', message)
            broadcast(f"Server: {message}")


def start_server():
    print(f"Server started and listening on port {port}")
    threading.Thread(target=handle_server_input).start()
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    start_server()
