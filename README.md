# Nested SegWit Transaction from Uncompressed Public Key

This script allows you to create and sign a transaction from a Nested SegWit (P2SH-P2WPKH) address that is derived from an uncompressed public key. It uses the `bitcoinlib` library to handle key generation, transaction creation, and signing.

## Prerequisites

1. Install Python 3.
2. Install `bitcoinlib`:
   ```bash
   pip install bitcoinlib
   ```
## Usage

Clone this repository.

Open nested_segwit_transaction.py.

Replace the placeholders in the script with your actual values:

UNCOMPRESSED_PUBLIC_KEY: Your uncompressed public key in hex format.
PRIVATE_KEY_WIF: Private key in Wallet Import Format (WIF).
TXID: The transaction ID of the UTXO you want to spend.
VOUT: The output index of the UTXO in the transaction.
DESTINATION_ADDRESS: The address to send the satoshis.
AMOUNT_TO_SEND: The amount in BTC to send.
FEE: The transaction fee in BTC.

 ```bash
python nested_segwit_transaction.py
```

## Output
The script will print the generated Nested SegWit P2SH-P2WPKH address, redeem script, and the raw signed transaction in hex format. You can broadcast this raw transaction using a Bitcoin node or any tool that supports raw transactions.

