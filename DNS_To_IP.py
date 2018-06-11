#!/usr/bin/python
import sys, socket


print ("\n")
filename = raw_input("Enter input file> ")

try:

	infile = open(filename)
	
except EnvironmentError as e:
    print(e)
    sys.exit(1)

print("\nFile {} exists!".format(filename))
print("\nGetting IP addresses for hosts")
print("\n")

for line in infile:
	hostname = line.strip()
	try:
		ipaddr =  socket.gethostbyname(hostname)
		print ipaddr
	except EnvironmentError as e:
		print ("Couldn't find IP address for {}: {}".format(hostname, e))
		continue
else:
		infile.close()
		print ("\nFinished the operation")
		
