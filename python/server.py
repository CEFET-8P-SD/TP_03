from datetime import datetime
import time
import zmq

menssages = []
class Chat_Python:

    @staticmethod
    def connect(port):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind(f"tcp://*:{port}")

        return socket

    @staticmethod
    def connect_java(port):

        context2 = zmq.Context()
        socket2 = context2.socket(zmq.REQ)
        socket2.connect(f"tcp://localhost:{port}")

        return socket2


    @staticmethod
    def broadcast_menssage(socket, menssage):
        socket.connect(f"tcp://localhost:5555")
        to_send = bytes(f"{menssage}", 'utf-8')
        socket.send(to_send)

    @staticmethod
    def send_to_java(socket, menssage):
        to_send = bytes(f"{menssage}", 'utf-8')
        socket.send(to_send)

    @staticmethod
    def read_msg(name):
        menssage = input("Say anything: \n")

        hora = datetime.now().strftime('%H:%M:%S')
        final_menssage = f"{hora} {name}: {menssage}"

        return final_menssage

    @staticmethod
    def set_name():
        print("----------------------------------")
        print("     Welcome to Python Chat       ")
        print("----------------------------------")

        name = input("What is your name? \n")

        return name

    def run(self):

        name = self.set_name()

        socket = self.connect(port='5555')

        socket_java = self.connect_java(port='5556')

        while True:
            menssage = self.read_msg(name)
            self.send_to_java(socket_java, menssage)
            socket_java.recv()

            time.sleep(0.5)
            msg = socket.recv()

            socket.send(b"Recebido")

            msg_string = msg.decode("utf-8")
            print(msg_string)

server = Chat_Python()
server.run()
