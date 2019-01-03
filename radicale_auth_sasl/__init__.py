#!/usr/bin/env python
import socket
import struct
import radicale

class Auth(radicale.auth.BaseAuth):
    def is_authenticated(self, login, password):
        authid, realm = [value.encode("utf-8") for value in login.split("@")]
        password = password.encode("utf-8")
        service = b"caldav"

        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect('/var/sasl2/mux')

        query = struct.pack('!H', len(authid))
        query += authid
        query += struct.pack('!H', len(password))
        query += password
        query += struct.pack('!H', len(service))
        query += service
        query += struct.pack('!H', len(realm))
        query += realm


        sock.sendall(query)
        resplen, = struct.unpack('!H', sock.recv(2))
        resp = sock.recv(resplen)

        return resp == b"OK"
