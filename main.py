# Sources:
# Chapter 2.7 of "Computer Networking: A Top Down Approach 7th Edition"
# Office Hours with Jon Frosch and Maher Elshakankiri
# Python Socket API includes: socket(), bind(), listen(), accept(), connect(), connect_ex(), send(), recv(), close()
from socket import *


# Task 1: Using a socket to GET a file
def part1():
    serverHost = "gaia.cs.umass.edu"
    # getURI = "/wireshark-labs/INTRO-wireshark-file1.html" # This is the page we are receiving after sending the below request
    getRequest = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

    # Use TCP
    s = socket(AF_INET, SOCK_STREAM)  # Create a socket that will connect to a server
    s.connect((serverHost, 80))  # Connect to the server. Takes only one value hence the double () to specify the port
    s.send(getRequest.encode())  # Send the getRequest to the website
    whatWasReceived = s.recv(1024)  # Have some sort of var to receive the message. Also grab the first 1024 bytes
    print(whatWasReceived.decode())  # Needs the .decode() so that it is not on one line
    s.close()  # Just like C, when you're done using it stop/close the connection

    '''
    FROM THE BOOK:
    
    serverPort = 12000  # Apparently some random thing, doesn't seem to matter which port is used
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverHost, serverPort))
    sentence = getRequest
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ', modifiedSentence.decode())
    clientSocket.close()
    '''


# Task 2: GET the data for a large file
def part2():
    # Same as before to start
    serverHost = "gaia.cs.umass.edu"
    getRequest = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

    # Use TCP
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((serverHost, 80))
    s.send(getRequest.encode())
    # Need a loop to get all the info, host will break connection when there is nothing more
    while True:
        whatWasReceived = s.recv(1024)
        print(whatWasReceived.decode())
        if whatWasReceived <= bytes(0):
            break
    s.close()


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


# Where to run each part of the program independently of each other
def main():
    while True:
        print("Which function would you like to run?")
        value = input("The options are 1, 2, 3, or n\nYour answer: ")
        print("\n\n")
        if value == '1':
            part1()
            print("\n\nFinished!")
        elif value == '2':
            part2()
            print("\n\nFinished!")
        elif value == '3':
            part3()
            print("\n\nFinished!")
        else:
            break


# Can just comment out each line here if you want an interface or just to test each part independently
if __name__ == "__main__":
    main()
    # part1()
    # part2()
    # part3()
