import secrets
import json
import solcx
from web3 import Web3, HTTPProvider
from hexbytes import HexBytes






# TODO: fix the import and go from there
def deploy_new():
  # compiled_contract = solcx.compile_files(
  #   [
  #     "./CreatorLazyNFT.sol",
  #   ],
  #   output_values=["abi", "bin"],
  #   solc_version="0.8.4"
  # )

  compiled_contract = solcx.compile_files(
    [
      "./CreatorNFTOne.sol",
    ],
    output_values=["abi", "bin"],
    solc_version="0.8.4"
  )
  
  contract_id, contract_interface = compiled_contract.popitem()
  bytecode = contract_interface['bin']
  abi = contract_interface['abi']

  print(contract_interface)

  # # with open('CreatorLazyNFT.json', 'w') as f:
  # #   json.dump(abi, f)

  # with open('NewOne.json', 'w') as f:
  #   json.dump(abi, f)

  web3.eth.default_account = web3.eth.accounts[0]
  web3NFT = web3.eth.contract(abi=abi, bytecode=bytecode)

  # print( Web3.toHex( bytes( web3.eth.accounts[0], encoding="utf-8" ) ) )

  ## Submit the transaction that deploys the contract
  # web3NFT.constructor( ).transact({'from': Web3.toHex( bytes( web3.eth.accounts[0], encoding="utf-8" ) ) })
    
  # tx_hash = web3NFT.constructor(123).transact( {'from': Web3.toChecksumAddress(web3.eth.accounts[0]), 'gas': 3400000} )
  # print(tx_hash)
  # deployed_contract_address = Web3.toChecksumAddress("0xc89ce4735882c9f0f0fe26686c53074e09b0d550")
  # deployed_contract = web3.eth.contract(abi=abi, address=deployed_contract_address)
  # print( deployed_contract.functions.helloWorld().call() )


  ## Info
  # tx_hash = web3NFT.constructor().transact({'from': web3.eth.accounts[0]})
  # tx_hash = web3NFT.transact( {'from': web3.Web3.toChecksumAddress(web3.eth.accounts[0]), 'gas': 3400000} )
  # print(tx_hash)
  # deployed_contract_address = Web3.toChecksumAddress('0x254dffcd3277c0b1660f6d42efbb754edababc2b')
  # deployed_contract = web3.eth.contract(abi=abi, address=deployed_contract_address)
  # print( deployed_contract.functions.helloWorld().call() )

  # # tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, 60)
  # # print(tx_receipt)



def deploy_main_one():
  compiled_contract = solcx.compile_files(
    [
      "./NewOne.sol",
    ],
    output_values=["abi", "bin"],
    solc_version="0.8.4"
  )

  # compiled_contract = solcx.compile_source(
  #   "contract Foo { function bar() public { return; } }",
  #   output_values=["abi", "bin"],
  #   solc_version="0.8.4"
  # )
  
  contract_id, contract_interface = compiled_contract.popitem()
  bytecode = contract_interface['bin']
  abi = contract_interface['abi']

  # with open('NewOne.json', 'w') as f:
  #   json.dump(abi, f)

  web3.eth.default_account = web3.eth.accounts[0]
  web3NFT = web3.eth.contract(abi=abi, bytecode=bytecode)
  print( web3NFT.constructor( HexBytes(b'adad') ).transact( { 'from': web3.toChecksumAddress(web3.eth.accounts[0]), 'gas': 3400000 } ) )
  # tx_hash = web3NFT.constructor().transact( {'from': (web3.eth.accounts[0]).encode(), 'gas': 3400000 } )

  # tx_hash = web3NFT.transact( {'from': web3.Web3.toChecksumAddress(web3.eth.accounts[0]), 'gas': 3400000} )
  # print(tx_hash)
  # deployed_contract_address = Web3.toChecksumAddress('0x254dffcd3277c0b1660f6d42efbb754edababc2b')
  # deployed_contract = web3.eth.contract(abi=abi, address=deployed_contract_address)
  # print( deployed_contract.functions.helloWorld().call() )






if __name__ == "__main__":
  blockchain_address = 'http://127.0.0.1:8545'
  web3 = Web3(HTTPProvider(blockchain_address))

  # connect_to_contract()

  # deploy_contract()
  # web3.eth.default_account = web3.eth.accounts[0]
  # print(web3.eth.accounts)
  
  # tx_hash = '0x6746c5a833f1d8b55fd28651d5f803905bef0d7644c2e9d1af598da555122f9c'
  # print( web3.eth.getTransaction(tx_hash) )

  # deploy_contract()
  # deploy_new()
  
  deploy_main_one()


# User creates token
  # save details in django
  # deploy lazy-mint contract on ETH-main-net with user's saved info / sig.
  # interact (buy <-- only real 'functionality' on C.C for v1) with solcx/python function calls

# TODO: 
  # deploy with web.js <-- ignore the python version for now?
 




