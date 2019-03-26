from socket import socket,AF_INET,SOCK_STREAM

host="localhost"
port=50008

def server():
    sock=socket(AF_INET,SOCK_STREAM)
    sock.bind(("",port))
    sock.listen(5)
    while True:
        conn,addr=sock.accept()
        data=conn.recv(1024)
        reply="server got: [%s]"%data
        conn.send(reply.encode())

def client(name):
    sock=socket(AF_INET,SOCK_STREAM)
    sock.connect((host,port))
    sock.send(name.encode())
    reply=sock.recv(1024)
    sock.close()
    print("clent got: [%s]"%reply)

if __name__ == "__main__":
    from threading import Thread
    server_thread=Thread(target=server)
    server_thread.daemon=True
    server_thread.start()
    for i in range(5):
        Thread(target=client,args=("client %s "% i,)).start()