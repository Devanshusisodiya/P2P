import asyncio
from p2p.network import Network
from p2p.peer import Peer

async def main():
    loop = asyncio.get_running_loop()

    net = Network(loop)

    p1 = Peer(net, "dom1.com", "127.0.0.1", 8888)
    p2 = Peer(net, "dom2.com", "127.0.0.1", 8889)
    p3 = Peer(net, "dom3.com", "127.0.0.1", 8887)

    await net.register(p1)
    await net.register(p2)
    await net.register(p3)

    await asyncio.gather(
        p1.talk("hey from p1", "dom2.com"),
        p1.talk("hey another from p1", "dom2.com"),
        p2.talk("hey from p2", "dom1.com"),
        p3.talk("hey from p3", "dom2.com")
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("\nnetwork closed\n")