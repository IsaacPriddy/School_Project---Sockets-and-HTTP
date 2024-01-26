# Sources:
# Chapter 2.7 of "Computer Networking: A Top Down Approach 7th Edition"
# Office Hours with Jon Frosch and Maher Elshakankiri
from socket import *


# Task 1: Using a socket to GET a file
def part1():
    serverHost = "gaia.cs.umass.edu"
    serverPort = 80
    # getURI = "/wireshark-labs/INTRO-wireshark-file1.html" # This is the page we are receiving after sending the below request
    getRequest = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

    # Use TCP
    s = socket(AF_INET, SOCK_STREAM)  # Create a socket that will connect to a server
    s.connect(
        (serverHost, serverPort))  # Connect to the server. Takes only one value hence the double () to specify the port
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


part1()
