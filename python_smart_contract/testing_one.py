import json
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:8545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]

# Path to the compiled contract JSON file
compiled_contract_path = '/Users/rahul/Documents/main/personal_learning_projects/fundamentals/smart_contract_tut/build/contracts/RahulToken.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0xC89Ce4735882C9F0f0FE26686c53074E09B0D550'

with open(compiled_contract_path) as file:
  contract_json = json.load(file)  # load contract info as JSON
  contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

# Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

# Call contract function (this is not persisted to the blockchain)
token_name = contract.functions.name().call()
token_symbol = contract.functions.symbol().call() 
# message = contract.functions.sayHello().call()

print(token_name, token_symbol)




 


