import json
import solcx
from web3 import Web3, HTTPProvider




def deploy_contract():
  compiled_contract = solcx.compile_files(
    ["NFT_testing_one.sol"],
    output_values=["abi", "bin"],
    solc_version="0.8.4"
  )

  contract_id, contract_interface = compiled_contract.popitem()
  bytecode = contract_interface['bin']
  abi = contract_interface['abi']

  blockchain_address = 'http://127.0.0.1:8545'
  web3 = Web3(HTTPProvider(blockchain_address))

  web3.eth.default_account = web3.eth.accounts[0]

  web3NFT = web3.eth.contract(abi=abi, bytecode=bytecode)

  # Submit the transaction that deploys the contract
  tx_hash = web3NFT.constructor('nft one', 'https://solcx.readthedocs.io/', 1000).transact({'from': web3.eth.accounts[0]})
  tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, 60)
  print(tx_receipt)
  


def connect_to_contract():
  
  blockchain_address = 'http://127.0.0.1:8545'
  web3 = Web3(HTTPProvider(blockchain_address))

  # print(web3.eth.accounts)

  web3.eth.defaultAccount = "0x22d491Bde2303f2f43325b2108D26f1eAbA1e32b"

  compiled_contract = solcx.compile_files(
    ["NFT_testing_one.sol"],
    output_values=["abi", "bin"],
    solc_version="0.8.4"
  )

  contract_id, contract_interface = compiled_contract.popitem()
  # bytecode = contract_interface['bin']
  # abi = contract_interface['abi']

  contract_address = "0x254dffcd3277C0b1660F6d42EFbB754edaBAbC2B"
  cs_contract_address = web3.toChecksumAddress(contract_address)
  contract_abi = contract_interface['abi']
  NFTContract = web3.eth.contract(abi=contract_abi, address=cs_contract_address)

  print( NFTContract.functions.seeSender().call() )




# deploy_contract()
connect_to_contract()


# 0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1
# 0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1


# TODO: 
  # how to prevent someone from calling from owner?


