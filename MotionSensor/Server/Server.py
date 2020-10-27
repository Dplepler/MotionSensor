import socket
import sys
import time
import bluetooth

def start_server():
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket to the port
	server_address = ('localhost', 6969)
	print ("Starting server on port:", server_address[1], "; ip:", server_address[0])
	sock.bind(server_address)

	# Listen for incoming connections
	sock.listen(1)

	# Wait for a connection
	print('waiting for a connection')
	return sock.accept()



def find_address(device_name):
	if device_name == "lamp":
		target_name = 'F-Light-D2E'
	else:
		raise Exception("Unknown device name")
	
	target_address = None

	nearby_devices = bluetooth.discover_devices(lookup_names=True)
	
	# Print nearby devices
	print("Found {} devices.".format(len(nearby_devices)))
	for addr, name in nearby_devices:
		print("  {} - {}".format(addr, name))

	for bdaddr, name in nearby_devices:	
		if target_name == ( name ):
			target_address = bdaddr
			break
	
	if target_address is not None:
		print ("found target bluetooth device with address ", target_address)
		return target_address
	else:
		raise Exception("could not find target bluetooth device nearby")



def connect_bluetooth(addr):
	# Create the client socket
	sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	
	service_matches = bluetooth.find_service(name= 'F-Light-D2E', address= addr)
	
	if len(service_matches) == 0:
		raise Exception("couldn't find the SampleServer service =(")

	first_match = service_matches[0]
	port = first_match["port"]
	name = first_match["name"]
	host = first_match["host"]


	sock.connect((addr, port))

	return sock



def main():

	# Try to Connect to bluetooth audio (In Sco'ish accent)
	print('---------------------------Bluetooth---------------------------')
	while True:
		#try:
			
			bt_connection = connect_bluetooth( find_address(input("Enter Deivce name: ")) )
			break

		#except Exception as e:
		#	print("Error connecting to bluetooth device")
		#	print(e)

	print('\n\n\n')

	# Try to start up server (In Bri'ish accent)
	while True:
		try:
			print('--------------------------Server start--------------------------')
			connection, client_address = start_server()
			break

		except Exception as e:
			print("Error in starting server")
			print(e)






if __name__ == "__main__":
	main()
