import asyncio

class ClientProtocol(asyncio.Protocol):
    def __init__(self, message, future):
        self.message = message
        self.on_con_lost = future

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('\nData sent: {!r}\n'.format(self.message))

    def data_received(self, data):
        print('\nData received: {!r}\n'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.on_con_lost.set_result(True)