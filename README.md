# Networking, systems, and security labs

A selection of Python coursework exploring sockets, scheduling, routing, and cryptography. These are small historical educational demonstrations with course-scaffold attribution. Known partial implementations are labeled explicitly; static syntax checks do not establish runtime correctness.

| Topic | Contents | Status |
| --- | --- | --- |
| [Sockets](sockets/) | TCP and UDP echo client/server pairs | Local loopback demonstrations |
| [Routing](routing/) | Threaded airport hub-and-spoke prototype | Partial; connection reuse and forwarding unfinished |
| [Systems](systems/) | CPU scheduling simulator | Historical prototype; feedback scheduling needs repair |
| [Cryptography](cryptography/) | Toy cipher, Bloom filter, selfish-mining experiment | Educational simulations with documented limits |
| [Drafts](drafts/) | Socket timeout experiment | Partial timeout/cleanup handling |

The Python scripts use the standard library. The cipher notebook needs a Python Jupyter kernel. No packet captures, real passenger records, original message/key files, credentials, or student records are included. Synthetic fixtures are clearly marked. Scripts were parsed for syntax; network listeners, downloaded code, and simulations were not executed during preparation.

See [PROVENANCE.json](PROVENANCE.json) and [NOTICE.md](NOTICE.md) for source and scaffold attribution. The routing source retains its Tech With Tim tutorial, GeeksforGeeks reference, and ChatGPT threading-assistance comments.

The more substantial cryptocurrency capstone is maintained at [Bitcoin double-spend website](https://github.com/legooz/bitcoin-double-spend-website); this collection contains supplementary exercises. C/C++ systems work is organized separately in [C/C++ portfolio](https://github.com/legooz/c-cpp-portfolio).

[Engineering portfolio](https://github.com/legooz/engineering-portfolio)
