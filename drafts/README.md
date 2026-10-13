# Drafts

The TCP timeout script is retained as an unfinished local socket exercise. Its counter is initialized outside the connection loop, so timeout state carries across clients. Socket cleanup sits beyond an infinite accept loop and is not reliably reached. It uses loopback port 12345, also used by the socket examples. Do not treat it as a robust server implementation.

Only static Python syntax was checked. See the repository [provenance](../PROVENANCE.json).
