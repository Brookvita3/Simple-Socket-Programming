import socket
import threading


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 65432))
nickname = input("Enter your nickname: ")


# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
            elif message == "quit":
                print("you disconnected")
                client.close()
                break
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        message = input("")
        if message == "quit":
            client.send("quit".encode("ascii"))
            client.close()
            break
        else:
            message = nickname + ": " + message
            client.send(message.encode("ascii"))


if __name__ == "__main__":

    receive_thread = threading.Thread(
        target=receive,
    )
    receive_thread.start()

    write_thread = threading.Thread(
        target=write,
    )
    write_thread.start()
