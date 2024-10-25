# nested_segwit_transaction.py

from bitcoinlib.wallets import HDWallet
from bitcoinlib.transactions import Transaction
from bitcoinlib.keys import Key

def create_nested_segwit_address(uncompressed_public_key):
    """
    Creates a Nested SegWit P2SH-P2WPKH address from an uncompressed public key.
    
    Parameters:
    uncompressed_public_key (str): Uncompressed public key in hex format.
    
    Returns:
    str: The Nested SegWit address.
    str: The redeem script for the address.
    """
    redeem_script = f"0014{Key(uncompressed_public_key).hash160()}"
    nested_address = Key.from_redeem_script(redeem_script).address
    return nested_address, redeem_script

def create_and_sign_transaction(txid, vout, destination_address, amount, fee, redeem_script, private_key_wif):
    """
    Creates and signs a transaction from a Nested SegWit address.
    
    Parameters:
    txid (str): The transaction ID of the UTXO.
    vout (int): The index of the UTXO in the transaction.
    destination_address (str): The address to send the funds to.
    amount (float): The amount to send in BTC.
    fee (float): The transaction fee in BTC.
    redeem_script (str): The redeem script for the Nested SegWit address.
    private_key_wif (str): Private key in Wallet Import Format (WIF).
    
    Returns:
    str: The raw signed transaction in hex format.
    """
    tx = Transaction(network='bitcoin')
    tx.add_input(txid, vout, redeem_script=redeem_script)
    tx.add_output(destination_address, int(amount * 1e8))  # Convert BTC to satoshis

    # Sign the transaction
    input = tx.inputs[0]
    input.sign(private_key_wif)
    
    return tx.as_hex()

if __name__ == "__main__":
    # Replace these with your own values
    UNCOMPRESSED_PUBLIC_KEY = "YOUR_UNCOMPRESSED_PUBLIC_KEY"
    PRIVATE_KEY_WIF = "YOUR_PRIVATE_KEY_WIF"
    TXID = "UTXO_TXID"  # Transaction ID of the UTXO
    VOUT = 0  # Index of the UTXO
    DESTINATION_ADDRESS = "DESTINATION_ADDRESS"  # Address to send the funds
    AMOUNT_TO_SEND = 0.0001  # Amount to send in BTC
    FEE = 0.00001  # Transaction fee in BTC

    # Generate Nested SegWit address and redeem script
    nested_address, redeem_script = create_nested_segwit_address(UNCOMPRESSED_PUBLIC_KEY)
    print(f"Nested SegWit P2SH-P2WPKH Address: {nested_address}")
    print(f"Redeem Script: {redeem_script}")

    # Create and sign the transaction
    try:
        raw_transaction = create_and_sign_transaction(TXID, VOUT, DESTINATION_ADDRESS, AMOUNT_TO_SEND, FEE, redeem_script, PRIVATE_KEY_WIF)
        print("Raw Transaction:", raw_transaction)
    except Exception as e:
        print("Error creating transaction:", e)
