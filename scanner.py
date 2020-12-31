import socket, logging, time
from threading import Thread

logging.basicConfig(filename="scanner.log", level=logging.DEBUG)
dataRecv = dict()

def scan(host, port):
	try:
		sock = socket.socket()
		sock.connect((host, port))

		logging.info("Port {0} is open.".format(port))
		print("Port {0} is open.".format(port))

		sock.settimeout(2.0)
		dataRecv[port] = "{0}".format(sock.recv(1024))

	except ConnectionRefusedError:
		logging.info("Port {0} is closed.".format(port))
		print("Port {0} is closed.".format(port))

	except socket.timeout:
		pass

	finally:
		sock.close()


def main():
	host = "127.0.0.1"
	ports = (21, 22, 80, 443)

	logging.info("Connecting to {0}".format(host))
	print("Attempting to connect to {0}".format(host))

	for i in range(len(ports)):
		thread = Thread(target=scan, args=(host, ports[i]))
		thread.start()

	time.sleep(2)
	print("Retrieving data...")

	for port in dataRecv:
		print("Message from port {0} : {1}".format(port, dataRecv[port]))

main()
