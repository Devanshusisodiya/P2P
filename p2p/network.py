from asyncio import AbstractEventLoop
from p2p.peer_base import PeerBase

class Network:
    def __init__(self, loop: AbstractEventLoop) -> None:
        self.loop = loop
        self.nodes = {}

    async def register(self, peer: PeerBase):
        if len(self.nodes) > 0:
            for domain in self.nodes:
                await peer.talk("hey! i just joined the network", domain)
            
        self.nodes[peer.domain] = peer
        await peer.setup_server()

    def resolve(self, domain: str):
        return (self.nodes[domain].host, self.nodes[domain].port)

