from socket import *

mailServer='smtp.csus.edu'
mailPort=25
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'

helloCommand = 'HELO Alice\r\n'
clientSocket.send(helloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

mailfromCommand = 'MAIL FROM: <darkmanflgg@gmail.com>\r\n'
clientSocket.send(mailfromCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

rcpttoCommand = 'RCPT TO: <jdbender64@gmail.com>\r\n'
clientSocket.send(rcpttoCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

dataCommand = 'DATA\r\n'
print dataCommand
clientSocket.send(dataCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '354':
	print '354 reply not received from server'

message = 'SUBJECT: SMTP Mail Client Test\n'
message2 = '\r\nI love networks!'
endmsg = '\r\n.\r\n'
clientSocket.send(message)
clientSocket.send(message2)
clientSocket.send(endmsg)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server'

quitCommand = 'QUIT\r\n'
print quitCommand
clientSocket.send('QUIT\r\n')
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '221':
	print '221 reply not received'

