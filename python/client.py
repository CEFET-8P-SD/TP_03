from datetime import datetime
import time
import zmq


class Client:

    def __init__(self):
        print("----------------------------------")
        print("     Welcome to Python Chat…      ")
        print("----------------------------------")

        self.name = input("What is your name? ")

    @staticmethod
    def get_mensage(socket):
        msg_server = socket.recv()
        msg_string = msg_server.decode("utf-8")

        return msg_string

    @staticmethod
    def send_mensage(socket, mensage):
        msg_bytes = bytes(mensage, 'utf-8')
        socket.send(msg_bytes)

    def connect(self):

        context = zmq.Context()

        print("----------------------------------")
        print("   Connecting to Python server…   ")
        print("----------------------------------")

        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")

        while True:
            # Read the mensage from terminal
            mensage = input("Say anything: ")

            hora = datetime.now().strftime('%H:%M:%S')
            final_menssage = f"{hora} {self.name}: {mensage}"

            self.send_mensage(socket, final_menssage)
            print(f"{final_menssage}")

            # Wait a litle while
            time.sleep(0.5)

            msg_string = self.get_mensage(socket)
            print(f"{msg_string}")


client = Client()
client.connect()
