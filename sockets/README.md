# Sockets

The TCP and UDP clients and servers use loopback port 12345. Run only one protocol pair at a time to avoid conflicting listeners. In separate terminals, start tcp_server.py then tcp_client.py, or udp_server.py then udp_client.py. The clients accept keyboard input; a dot ends the client session. These examples demonstrate send/receive behavior, not production framing, concurrency, or secure transport. Standard-library Python only; no listener was started during preparation.

Only static Python syntax was checked. See the repository [provenance](../PROVENANCE.json).
