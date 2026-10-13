# Recovered student coursework; see README.md and PROVENANCE.json for attribution and status.
import hashlib
from pathlib import Path
DATA_DIR = Path(__file__).parent / "data"

m = 400000   # length of bloom filter in bits
k = 13       # number of hash functions used per txn

def main():
    # create a set that includes all of transactions in Alice's block
    txns_in_Alices_block = {line.strip() for line in open(DATA_DIR / "tx_hashes_in_block.txt")}
    true1 = 0
    # create bloom filter
    bloom_filter = m*[False]  # initially Bloom filter bit vector set to all 0/False
    for txn in txns_in_Alices_block:  
        hashes = get_k_hashes(txn, k)   # get the k hashes for a particular txn
        for h in hashes:                
            index = h % m               # corresponding bloom filter index must be between 0 and m-1
            bloom_filter[index] = True
            

            
    
    print ("Bloom filter length: ", len(bloom_filter))
    print ("Bloom sum length: ", sum(bloom_filter))

    print( sum(bloom_filter)/len(bloom_filter) )

    # Bobs reconstructed block contains any transaction from his mempool which pass the Bloom filter
    txns_in_Bobs_reconstructed_block = set()   #no txns added yet
    txns_in_Bobs_mempool = {line.strip() for line in open(DATA_DIR / "tx_hashes_in_mempool.txt")}
    for txn in txns_in_Bobs_mempool:
        if( check_bloom_membership(bloom_filter, txn) == True): # if txn passes Bloom filter membership test
            txns_in_Bobs_reconstructed_block.add( txn )         # add the txn to Bob's block

    if(txns_in_Bobs_reconstructed_block ==  txns_in_Alices_block): # if Bob's and Alice's block are equal
        print("SUCCESS: Block successfully transmitted from Alice to Bob")
    else:
        print("FAIL: Block did not successfully transmitted from Alice to Bob")
        print(f"{len(txns_in_Bobs_reconstructed_block - txns_in_Alices_block)} extra transactions are:")
        print(*(txns_in_Bobs_reconstructed_block - txns_in_Alices_block), sep="\n")


# output list of k hashes of string_to_hash
def get_k_hashes(string_to_hash, k):
    a_hash = hashlib.sha256( string_to_hash.encode() ).hexdigest()
    output = [int(a_hash,16)]
    for _ in range(k-1):
        a_hash = hashlib.sha256( a_hash.encode() ).hexdigest()
        output += [int(a_hash,16)]
    return output

# check set membership using bloom filter
# returns False if txn hashes into a bloom filter bit that is set to 0/False
# return True otherwise
def check_bloom_membership(bloom_filter, txn):
    hashes = get_k_hashes(txn, k)  # Get the k hash values for the transaction
    for h in hashes:
        index = h % m  # Calculate the corresponding Bloom filter index
        if not bloom_filter[index]:  # If any bit is not set to True
            return False  # The transaction is not in the Bloom filter
    return True  # All bits are set to True, so the transaction passes the test

    

if __name__ == "__main__":
    main()
