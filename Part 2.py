# Sources:
# Chapter 2.7 of "Computer Networking: A Top Down Approach 7th Edition"
# Office Hours with Jon Frosch and Maher Elshakankiri
from socket import *


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


part2()
