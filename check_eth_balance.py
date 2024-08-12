from web3 import Web3
from web3.middleware import geth_poa_middleware

# Connect to the Blast chain using WebSocket
blast_rpc_url = "wss://blast-rpc.publicnode.com"
web3 = Web3(Web3.WebsocketProvider(blast_rpc_url))

# Inject the PoA middleware if needed
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Check if connected
if web3.is_connected():
    print("Connected to the Blast chain")

    # List of Ethereum addresses to check
    eth_addresses = [
        "0xYOURADDRESS",
        "0xYOURADDRESS"
    ]

    # Initialize total balance in Ether
    total_balance_eth = 0

    # Iterate over each address and get the balance
    for eth_address in eth_addresses:
        try:
            # Get the balance
            balance_wei = web3.eth.get_balance(eth_address)

            # Convert balance from Wei to Ether
            balance_eth = web3.from_wei(balance_wei, 'ether')

            # Add to the total balance
            total_balance_eth += balance_eth

            print(f"Balance for address {eth_address}: {balance_eth} ETH")
        except Exception as e:
            print(f"Error retrieving balance for {eth_address}: {str(e)}")

    # Print the total balance
    print(f"\nTotal balance for all addresses: {total_balance_eth} ETH")

else:
    print("Failed to connect to the Blast chain")
