import socket
import time
# pickle allows us to convert objects to bytes so we can send and receive them 
import pickle


HEADERSIZE =  10

msg = "Welcome to the server!"
print(f"{len(msg):<10}")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    dict = {1: "Caden", 2: "Wilcox"}
    msg = pickle.dumps(dict)

    msg = bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8") + msg

    clientsocket.send(bytes(msg))



# Cool way to send the time to the client after every 3 seconds that pass 
    # while True:
    #     time.sleep(3)
    #     msg = f"the time is: {time.time()}"
    #     msg = f"{len(msg):<{HEADERSIZE}}" + msg
    #     clientsocket.send(bytes(msg, "utf-8"))
