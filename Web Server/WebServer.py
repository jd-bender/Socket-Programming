from socket import *
def main():
	serverPort = 6789
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.bind(('', serverPort))
	serverSocket.listen(1)
	print 'Up on port:', serverPort
	while True:
		print 'Ready to go!'
		connectionSocket, addr = serverSocket.accept()
		try:
			message = connectionSocket.recv(1024)
			print message,'::', message.split()[0],':', message.split()[1]
			filename = message.split()[1]
			print filename, '||', filename[1:]
			f = open(filename[1:])
			outputdata = f.read()
			print outputdata
			connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
			connectionSocket.send(outputdata)
			connectionSocket.close()
		except IOError:
			pass
			print "404 Not Found"
			connectionSocket.send('\HTTP/1.1 404 Not Found\n\n')
		break
	pass
if __name__ == '__main__':
	main()