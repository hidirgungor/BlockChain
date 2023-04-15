# connect to the contract using the deployed address and ABI
contract = w3.eth.contract(address=contract_address, abi=abi)

# check the total supply of HGG
total_supply = contract.functions.totalSupply().call()
print(f'Total supply of HGG: {total_supply}')

# transfer some HGG from the creator to another address
to_address = '0x1234567890123456789012345678901234567890'
amount = 1000 * 10**18
tx_hash = contract.functions.transfer(to_address, amount).transact({'from': account.address})
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print(f'Transferred {amount} HGG to {to_address}')
