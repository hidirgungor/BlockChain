from web3 import Web3
from solcx import compile_source

# connect to the local Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# compile the Solidity contract
contract_source = '''
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HGGToken {
    string public name = "HGG Token";
    string public symbol = "HGG";
    uint256 public totalSupply = 1000000 * 10**18; // 1 million HGG

    mapping(address => uint256) public balanceOf;

    constructor() {
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address to, uint256 amount) external returns (bool) {
        require(balanceOf[msg.sender] >= amount, "Not enough balance");
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        return true;
    }
}
'''
compiled_contract = compile_source(contract_source)['<stdin>:HGGToken']

# deploy the contract
account = w3.eth.account.create()
bytecode = compiled_contract['bin']
abi = compiled_contract['abi']
tx_hash = w3.eth.contract(abi=abi, bytecode=bytecode).constructor().transact({'from': account.address})
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# get the deployed contract address
contract_address = tx_receipt.contractAddress
print(f'HGGToken deployed at {contract_address}')
