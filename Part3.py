# Sources:
# Chapter 2.7 of "Computer Networking: A Top Down Approach 7th Edition"
# Office Hours with Jon Frosch and Maher Elshakankiri
from socket import *


# Task 3: The world’s simplest HTTP server
def part3():
    localHost = '127.0.0.1'  # The local IP that I will need to connect to
    serverPort = 1842  # Roughly the year Ada Lovelace created programming
    data = "HTTP/1.1 200 OK\r\n" \
           "Content-Type: text/html; charset=UTF-8\r\n\r\n" \
           "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

    serverSocket = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket
    serverSocket.bind((localHost, serverPort))
    serverSocket.listen(1)  # Set the socket to listen for anyone, max number of connections is at least 1
    print('The server is ready: ')
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        print(sentence, "\n")  # Print the GET request from the client, also added the newlines to break apart requests

        # Just a little spot for the user on the server to know what is being sent and when
        print("Sending >>>>>>>>>>")
        print(data)
        print("<<<<<<<<<<\n")

        connectionSocket.send(data.encode())  # The actual sending of data to wherever it wants to go
        connectionSocket.close()  # Once the data has been sent the socket can just close
    serverSocket.close()

    '''
    serverSocket = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket
    serverSocket.bind((localHost, somePort))
    serverSocket.listen(1)  # Set the socket to listen for anyone
    print('The server is ready to receive')
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        # capitalizedSentence = sentence.upper()    # Felt like I could just skip the middle man in this case
        connectionSocket.send(sentence.upper().encode())
        connectionSocket.close()  # Once the data has been sent the socket can just close
    serverSocket.close()
    '''


part3()
