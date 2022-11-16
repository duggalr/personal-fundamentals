import json
import solcx
from web3 import Web3, HTTPProvider




def deploy_contract():
  compiled_contract = solcx.compile_files(
    ["nft_example.sol"],
    output_values=["abi", "bin"],
    solc_version="0.8.0"
  )

  contract_id, contract_interface = compiled_contract.popitem()
  bytecode = contract_interface['bin']
  abi = contract_interface['abi']


  # # TODO: deploy this on a public testnet / purchase tokens with meta-mask
  # blockchain_address = 'http://127.0.0.1:8545'
  # web3 = Web3(HTTPProvider(blockchain_address))

  # web3.eth.default_account = web3.eth.accounts[0]

  # web3NFT = web3.eth.contract(abi=abi, bytecode=bytecode)

  # # Submit the transaction that deploys the contract
  # tx_hash = web3NFT.constructor('nft one', 'https://solcx.readthedocs.io/', 1000).transact({'from': web3.eth.accounts[0]})
  # tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, 60)
  # print(tx_receipt)



def connect_to_contract():
  
  blockchain_address = 'http://127.0.0.1:8545'
  web3 = Web3(HTTPProvider(blockchain_address))

  compiled_contract = solcx.compile_files(
    ["nft_example.sol"],
    output_values=["abi", "bin"],
    solc_version="0.8.0"
  )

  contract_id, contract_interface = compiled_contract.popitem()
  # bytecode = contract_interface['bin']
  # abi = contract_interface['abi']

  contract_address = "0xe78a0f7e598cc8b0bb87894b0f60dd2a88d6a8ab"
  cs_contract_address = web3.toChecksumAddress(contract_address)
  contract_abi = contract_interface['abi']
  NFTContract = web3.eth.contract(abi=contract_abi, address=cs_contract_address)
  
  print( NFTContract.functions.getTokenTotalSupply().call() )

  print( NFTContract.functions.safeMint('0x9d225E305758483AdD2A372B444acda6c0c21Fb1', 1).call() )



connect_to_contract()






