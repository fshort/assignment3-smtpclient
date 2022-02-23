from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    #run python3 -m smtpd -c DebuggingServer -n 127.0.0.1:1025 in a wsl terminal window to start up a test smtp server to test this script against

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    """ print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.') """

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    """ print(recv1) 
    if recv1[:3] != '250':
        print('250 reply not received from server.') """

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailCmd = "MAIL FROM: <fred.short@nyu.edu>\r\n"
    clientSocket.send(mailCmd.encode())
    recvMail = clientSocket.recv(1024).decode()
    """ if recvMail[:3] != '250':
        print('250 reply not received from server.') """
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptCmd = "RCPT TO: <fshort3@gmail.com>\r\n"
    clientSocket.send(rcptCmd.encode())
    recvRcpt = clientSocket.recv(1024).decode()
    """ if recvRcpt[:3] != '250':
        print('250 reply not received from server.') """
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCmd = "DATA \r\n"
    clientSocket.send(dataCmd.encode())
    recvData = clientSocket.recv(1024).decode()
    """ if recvData[:3] != '354':
        print('354 reply not received from server.') """
    # Fill in end

    # Send message data.
    # Fill in start
    msg = "This is a test.\nThanks,\nFred\r\n"
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    eom = ".\r\n"
    clientSocket.send(eom.encode())
    recvEOM = clientSocket.recv(1024).decode()
    """ if recvEOM[:3] != '250':
        print('250 reply not received from server.') """
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCmd = "QUIT\r\n"
    clientSocket.send(quitCmd.encode())
    recvQuit = clientSocket.recv(1024).decode()
    """ if recvQuit[:3] != '221':
        print('221 reply not received from server.') """
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')