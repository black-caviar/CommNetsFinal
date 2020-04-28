import socket

UDP_IP  = "127.0.0.1"
UDP_PORT = 6969

STATE = 'idle'
BLOCK = 0
FILE = None

def openFile(msg):
    global STATE
    global FILE
    fields = msg[2:-1].split(b'\0')
    print(fields)
    
    if fields[1] == b'netascii':
        FILE = open(fields[0], "r")
    elif fields[1] == b'octet':
        FILE = open(fields[0], "rb")
    else:
        print("Bad file type")
        STATE = 'idle'

def parseMSG(msg):
    global STATE
    opcode = msg[1]
    if opcode == 1:
        print('RRQ')
        if STATE == 'idle':
            openFile(msg)
            STATE = 'write'
        else:
            print("Duplicate read request, error")
            STATE = 'idle'
        return 'RRQ'
    elif opcode == 2:
        print("WRQ")
        print("Not implemented")
        STATE = 'idle'
        #return 'RRQ'
    elif opcode == 3:
        print("DATA")
        print("Not implemented")
        STATE = 'idle'
        #return 'DATA'
    elif opcode == 4:
        print("ACK")
        STATE = 'write'
        #return 'ACK'
    elif opcode == 5:
        print("ERROR", msg[3])
        print(msg[3:-1])
        STATE = 'idle'
        #return 'ERROR'
    else:
        print("Unknown opcode")
        STATE = 'idle'
        #return None


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("Received message:", data)
    print("Message from:", addr)
    msgType = parseMSG(data)
    print(STATE)
    if STATE == 'write' and msgType == 'RRQ':
        newsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        newsock.bind((UDP_IP, 55555))
        print('hello there')
        #make this some random good port
        BLOCK = 0
        while True:
            #data, addr = newsock.recvfrom(1024)
            #msgType = parseMSG(data)
            #print("Received new message:", data)
            if STATE == 'write':
                tx = FILE.read(512)
                print(len(tx))
                print(type(tx))
                BLOCK = BLOCK + 1
                if type(tx) == str:
                    print(tx.encode())
                    tx_msg = b'\0' + b'\3' + BLOCK.to_bytes(2,'big') + tx.encode()
                else:
                    tx_msg = b'\0' + b'\3' + BLOCK.to_bytes(2,'big') + tx
                print(tx_msg)
                print(type(tx_msg))
                newsock.sendto(tx_msg, (addr))
                state = 'wait'
                if len(tx) < 512:
                    STATE = 'idle'
                    break
            if STATE == 'wait':
                newmsg = newsock.recv()
                parseMSG(newmsg)
                
    

#state NULL, wait, transmit, receive 
#open transmit wait transmit end
        
