import socket, logging
from threading import Thread

logging.basicConfig(filename="main.log", level=logging.DEBUG)

## static var
id=-1
def trash_way_to_make_static_var():
	global id
	id += 1
	return id

class services():
	def __init__(self):
		self.ID = trash_way_to_make_static_var()
		self.LHOST = None
		self.LPORT = None

	def setLHOST(self, host):
		try:
			self.LHOST = str(host)
			logging.info("{0}:LHOST => '{1}'".format(self.ID, self.LHOST))

		except Exception as e:
			self.LHOST = None
			logging.error("{0}:{1}".format(self.ID, e))
			print("{0}:{1}".format(self.ID, e))

	def setLPORT(self, port):
		try:
			int(port)

		except TypeError:
			self.LHOST = None
			logging.error("{0}:Invalid port type.".format(self.ID))
			print("{0}:Invalid port type.".format(self.ID))
			return

		try:
			self.LPORT = int(port)
			logging.info("{0}:LPORT => '{1}'".format(self.ID, self.LPORT))

		except Exception as e:
			self.LHOST = None
			logging.error("{0}:{1}".format(self.ID, e))
			print("{0}:{1}".format(self.ID, e))

	def run(self):
		if self.LHOST == None:
			logging.error("{0}:LHOST has not been set.".format(self.ID))
			print("{0}:LHOST has not been set.".format(self.ID))
			return

		if self.LPORT == None:
			logging.error("{0}:LPORT has not been set.".format(self.ID))
			print("{0}:LPORT has not been set.".format(self.ID))
			return
		try:
			sock = socket.socket()
			sock.bind((self.LHOST, self.LPORT))
			sock.listen(2)

			logging.info("{0}:Starting Server on Port {1}.".format(self.ID, self.LPORT))
			print("{0}:Starting Server on Port {1}.".format(self.ID, self.LPORT))

			while True:
				client, addr = sock.accept()
				logging.info("{0}:Incoming connection from {1[0]}".format(self.ID, addr))
				print("{0}:Incoming connection from {1[0]}".format(self.ID, addr))
				client.send("Thank you for connecting to port {0}".format(self.LPORT).encode())
				client.close()

		except Exception as e:
			logging.error("{0}:{1}".format(self.ID, e))
			print("{0}:{1}".format(self.ID, e))


def main():
	## array of services
	serv = list()
	serv.append(services())
	serv.append(services())
	serv.append(services())
	serv.append(services())

	serv[0].setLHOST("127.0.0.1")
	serv[0].setLPORT(21)

	serv[1].setLHOST("127.0.0.1")
	serv[1].setLPORT(22)

	serv[2].setLHOST("127.0.0.1")
	serv[2].setLPORT(443)

	serv[3].setLHOST("127.0.0.1")
	serv[3].setLPORT(4444)

	for i in range(len(serv)):
		thread = Thread(target=serv[i].run, args=())
		thread.start()


if __name__ == "__main__":
	main()


