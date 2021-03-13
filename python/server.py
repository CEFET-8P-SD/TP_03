import time
import zmq

menssages = []
class Server:

    @staticmethod
    def connect(port):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind(f"tcp://*:{port}")

        return socket

    @staticmethod
    def broadcast_menssage(socket, menssage):
        socket.connect(f"tcp://localhost:5555")
        to_send = bytes(f"{menssage}", 'utf-8')
        socket.send(to_send)

    @staticmethod
    def send_to_node(socket, menssage):
        socket.connect("tcp://localhost:5556")
        to_send = bytes(f"{menssage}", 'utf-8')
        socket.send(to_send)


    def run(self):

        socket = self.connect(port='5555')

        while True:

            #  Wait for next request from client
            msg = socket.recv()

            msg_string = msg.decode("utf-8")

            print(f"{msg_string}")

            # Wait a litle while
            time.sleep(0.5)
            self.send_to_node(socket,msg_string)
            self.broadcast_menssage(socket, msg_string)


server = Server()
server.run()
