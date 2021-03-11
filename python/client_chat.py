import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    msg = input("Fala uma coisa aí zé:   ")

    msg_bytes = bytes(msg, 'utf-8')

    print(f"Sending request {request} …")
    socket.send(msg_bytes)

    #  Get the reply.
    msg_server = socket.recv()

    msg_string = msg_server.decode("utf-8")

    print(f"Received reply {request} [ {msg_string} ]")