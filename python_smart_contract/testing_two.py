import json
from web3 import Web3, HTTPProvider
from solcx import compile_source




def deploy_contract():
  compiled_sol = compile_source(
  '''
  pragma solidity >0.5.0;
    contract Greeter {
      string public greeting;

      constructor() public {
        greeting = 'Hello';
      }

      function setGreeting(string memory _greeting) public {
        greeting = _greeting;
      }
      
      function greet() view public returns (string memory) {
        return greeting;
      }
    }
  ''',
    output_values=['abi', 'bin']
  )

  contract_id, contract_interface = compiled_sol.popitem()
  bytecode = contract_interface['bin']
  abi = contract_interface['abi']

  blockchain_address = 'http://127.0.0.1:8545'
  web3 = Web3(HTTPProvider(blockchain_address))

  web3.eth.default_account = web3.eth.accounts[0]

  Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)

  # Submit the transaction that deploys the contract
  tx_hash = Greeter.constructor().transact({'from': web3.eth.accounts[0]})
  tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, 60)
  print(tx_receipt)




# 0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1
# 0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:8545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# # Set the default account (so we don't need to set the "from" for every transaction call)
# web3.eth.defaultAccount = web3.eth.accounts[0]

# # print(web3)
# print(web3.eth.accounts)
# print(web3.eth.getBalance("0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"))

# deploy_contract()



compiled_sol = compile_source(
  '''
  pragma solidity >0.5.0;
    contract Greeter {
      string public greeting;

      constructor() public {
        greeting = 'Hello';
      }

      function setGreeting(string memory _greeting) public {
        greeting = _greeting;
      }
      
      function greet() view public returns (string memory) {
        return greeting;
      }
    }
  ''',
    output_values=['abi']
)
contract_id, contract_interface = compiled_sol.popitem()
# bytecode = contract_interface['bin']
# abi = contract_interface['abi']


contract_address = "0xe78a0f7e598cc8b0bb87894b0f60dd2a88d6a8ab"
cs_contract_address = web3.toChecksumAddress(contract_address)
contract_abi = contract_interface['abi']
GreeterContract = web3.eth.contract(abi=contract_abi, address=cs_contract_address)

# web3.eth.default_account = web3.eth.accounts[0]
# print( GreeterContract.functions.setGreeting("testing one").transact( {'from': web3.eth.accounts[0]} ) )
print( GreeterContract.functions.greet().call() )

 

# TODO: 
  # go back to web-app 
    # deploy contract to real-testnet from web-app and go from there
      # test for security (minting new tokens? transfer/buy with insufficent funds, etc.)
   


 

