from web3 import Web3, HTTPProvider
from eth_account import Account

# Connect to Ethereum network using Infura
w3 = Web3(HTTPProvider("https://mainnet.infura.io/v3/your-project-id"))

# Generate a new account to be used as the contract owner
owner = Account.create()

# Define the HGG token contract data
token_data = {
    'name': 'HGG Token',
    'symbol': 'HGG',
    'decimals': 18,
    'totalSupply': 1000000000
}

# Compile the HGG token contract code
with open('HGGToken.sol', 'r') as f:
    contract_code = f.read()

compiled_contract = w3.eth.compile.solidity(contract_code)

# Deploy the HGG token contract to Ethereum network
Contract = w3.eth.contract(
    abi=compiled_contract['<stdin>:HGGToken']['abi'],
    bytecode=compiled_contract['<stdin>:HGGToken']['bin']
)

tx_hash = Contract.constructor(**token_data).transact({'from': owner.address})

# Wait for the transaction to be mined and get the contract address
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
contract_address = tx_receipt.contractAddress

print(f"HGG token contract deployed at address: {contract_address}")
