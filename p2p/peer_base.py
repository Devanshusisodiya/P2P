from abc import abstractmethod

class PeerBase:
    @abstractmethod
    async def setup_server(self) -> None:
        pass

    @abstractmethod
    async def talk(self, message: str, domain: str):
        pass
    
    