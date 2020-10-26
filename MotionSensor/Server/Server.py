import socket
import sys

def start_server():
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket to the port
	server_address = ('localhost', 6969)
	print ("Starting server on port:", server_adress[1], "; ip:", server_adress[0])
	sock.bind(server_address)

	# Listen for incoming connections
	sock.listen(1)

	# Wait for a connection
	print('waiting for a connection')
	return sock.accept()


def main():

	# Try to start up server (In Bri'ish accent)
	while True:
		try:

			connection, client_adress = start_server()
			break
		except Exception as e:

			print("Error in starting server")
			print(e)
			sys.exit()




	



if __name__ == "main":
	main()
