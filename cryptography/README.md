# Cryptography

toy-ciphers.ipynb demonstrates a Vigenere-style letter cipher and symmetric XOR wrapping. The historical publicKey/privateKey parameter names do not make it public-key encryption. Original classroom messages, keys, and a personal joke phrase were replaced by three synthetic inline messages and explicit demonstration keys; the loop now uses those fixture lengths. These ciphers are intentionally educational and unsuitable for protecting real information.

The Bloom-filter script reads the clearly synthetic demo-transaction identifiers in data/ using a path relative to the script. It illustrates membership filtering and block reconstruction without contacting a cryptocurrency network. The selfish-mining Monte Carlo script is a simplified historical model: its state carries across parameter settings and sampling is not seeded, so results need model review. A separate draft whose loop condition could never terminate was excluded. The main double-spend project remains in its dedicated public repository.

Only static Python syntax was checked. See the repository [provenance](../PROVENANCE.json).
