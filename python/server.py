import time
import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    msg = socket.recv()

    msg_string = msg.decode("utf-8")

    print(f"{msg_string}")

    #  Do some 'work'
    time.sleep(0.5)

    to_send = bytes(f"{msg_string}", 'utf-8')

    #  Send reply back to client
    socket.send(to_send)
