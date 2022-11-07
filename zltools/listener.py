import threading
import socket

#a read thread, read data from remote
class Reader(threading.Thread):
    encoding = 'utf-8'
    BUFF_SIZE = 1024
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        """ what's this

        Args:
            #arg:
        Raises:
            error:

        """
        while True:
            data = self.client.recv(self.BUFF_SIZE)
            if (data):
                string = bytes.decode(data, encoding=self.encoding)
                print(string, end='')
            else:
                break

            print( f' close : {self.client.getpeername()}')

    def readline(self):
        """ what's this

        Args:
            #arg:
        Raises:
            error:

        """
        rec = self.inputs.readline()
        if rec:
            string = bytes.decode(rec, encoding=self.encoding)
            if len(string) > 2:
                string = string[0:-2]
            else:
                string = ''
        else:
            string = False
        return string

#a listen thread, listen remote connect
#when a remote machine requests to connect, it will create a thread to handle
class Listener(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('0.0.0.0', port))
        self.sock.listen(0)

    def run(self):
        """ what's this

        Args:
            #arg:
        Raises:
            error:

        """
        print('listener started')
        while True:
            client, clt_addr = self.sock.accept()
            Reader(client).start()
            clt_addr = clt_addr

            print( f' accept a connect ')

lst = Listener(9000) #create a listen thread
lst.start() #then start

# Now, you can use telnet to test it, the command is "telnet 127.0.0.1 9011"
# You also can use web broswer to test, input the address of "http://127.0.0.1:9011" and press Enter button
# Enjoy it....