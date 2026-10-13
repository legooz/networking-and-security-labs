# Routing

The original airport-network coursework was adapted for a local demonstration: SERVER is forced to 127.0.0.1, and the machine-specific CSV path now resolves passengers.example.csv beside the script. The two passenger records are newly written synthetic fixtures. The original Tech With Tim, GeeksforGeeks, and ChatGPT assistance comments remain. Historical command shape: python airport-routing.py HUB ANC or python airport-routing.py SPOKE FAI. This prototype is partial: it attempts repeated connects on the same socket, only acknowledges a layover instead of forwarding traffic, and can reference an unset acknowledgement for unexpected routes. Review and repair these behaviors before attempting a multi-terminal demo.

Only static Python syntax was checked. See the repository [provenance](../PROVENANCE.json).
