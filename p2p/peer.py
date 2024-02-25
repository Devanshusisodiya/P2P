from p2p.network import Network
from p2p.server_protocol import ServerProtocol
from p2p.client_protocol import ClientProtocol
from p2p.peer_base import PeerBase

class Peer(PeerBase):
    def __init__(self, network: Network, domain: str, host: str, port: int) -> None:
        self.domain = domain
        self.host = host
        self.port = port
        self.network = network
        self.server = None
    
    async def setup_server(self) -> None:
        # instantiate server instance
        self.server = await self.network.loop.create_server(
            lambda: ServerProtocol(),
            self.host, self.port
        )

    async def talk(self, message: str, domain: str):
        future = self.network.loop.create_future()
        host, port = self.network.resolve(domain)

        transport, _ = await self.network.loop.create_connection(
            lambda : ClientProtocol(message, future),
            host, port
        )

        try:
            await future
        finally:
            transport.close()
    
    