import socket
import sys
import time
from typing import Optional


class TorControlPortClient:
    control_address: str
    control_port: int
    control_password: Optional[str]

    def __init__(
            self,
            control_address: str,
            control_port: int,
            control_password: Optional[str]
    ):
        self.control_address = control_address
        self.control_port = control_port
        self.control_password = control_password

    def change_connection_ip(self, seconds_wait: int = 5) -> bool:
        time.sleep(seconds_wait)
        try:
            tor_connection = socket.create_connection((self.control_address, self.control_port))
            password_value = self.control_password if self.control_password is not None else ''
            message = f'AUTHENTICATE "{password_value}"\r\nSIGNAL NEWNYM\r\n'
            tor_connection.send(message.encode('utf-8'))
            response = tor_connection.recv(1024)
            if response != b'250 OK\r\n250 OK\r\n':
                sys.stderr.write('Unexpected response from Tor control port: {}\n'.format(response))
                return False
            return True
        except Exception as e:
            print(e)
            sys.stderr.write('Error connecting to Tor control port: {}\n'.format(repr(e)))
            return False
