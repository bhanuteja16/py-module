##! /bin/python3
import paramiko
import subprocess
import time

'''
def readlines(sock, recv_buffer=4096, delim='\n'):
	buffer = ''
	data = True
	while data:
		data = sock.recv(recv_buffer)
		buffer += data

		while buffer.find(delim) != -1:
			line, buffer = buffer.split('\n', 1)
			yield line
	return

ip = str(input("Enter the IP you want to connect: "))
print ("You have entered: %s"  % ip)
usr = str(input("Enter the Username: "))
print ("You have entered: %s"  % usr)
pwd = str(input("Enter the IPassword: "))
'''
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.150.142", username="bhanu", password="Kronos_16")
'''
while True :
	cmd = str(input("ssh> "))
	if cmd == 'exit':
		break
	stdin, stdout, stderr = ssh.exec_command(cmd)
	print (type(stdin))
	print (stderr.read())
	while True :


		print (stdout.readline(), end='')
		if not stdout.readline() :
			break

stdin, stdout, stderr = ssh.exec_command('sudo tcpdump -i eth0 -v -c 10')
stdin.write('Kronos_16\n')
stdin.flush()
print (stderr.read())
while True :
	print (stdout.readline(), end='')
	if not stdout.readline():
		break
'''
ssh_conn = ssh.invoke_shell()
time.sleep(3)
print (ssh_conn.recv(1000).decode('utf-8'), end='')
#f = open("bhanu.txt", "w")
while True:
	cmd = str(input(""))
	cmd = cmd + '\n'
	ssh_conn.send(cmd)
	time.sleep(.5)
	#f.write(str(ssh_conn.recv(4096)))
	data = ssh_conn.recv(4096).decode('utf-8')
	print (data, end='')
	'''
	for line in data.split('\r\n'):
		if line[0:11] == 'bhanu@ubunt' :
			print ('ssh>', end='')
		else :
			print (line)
'''
ssh_conn.close()
#f.close()



