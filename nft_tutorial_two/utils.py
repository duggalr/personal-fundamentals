import secrets
import json
import solcx
from web3 import Web3, HTTPProvider



def deploy_contract():
  compiled_contract = solcx.compile_files(
    [
      "contracts/CreatorNFT.sol", 
      "/Users/rahul/Documents/main/personal_learning_projects/fundamentals/node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol", 
      "/Users/rahul/Documents/main/personal_learning_projects/fundamentals/node_modules/@openzeppelin/contracts/access/Ownable.sol",
      "/Users/rahul/Documents/main/personal_learning_projects/fundamentals/node_modules/@openzeppelin/contracts/utils/Counters.sol"
    ],
    output_values=["abi", "bin"],
    solc_version="0.8.4"
  )
  
  contract_id, contract_interface = compiled_contract.popitem()
  bytecode = contract_interface['bin']
  abi = contract_interface['abi']
  
  print('contract-abi:', abi)

  # with open('CreatorNFTABI.json', 'w') as f:
  #   json.dump(abi, f)
 
  # # TODO:  
  #   # get abi into JSON <-- don't believe the current contract is deployed (change name to match contract-class) and redeploy
  #   # get it to show in javascript
  #   # interact directly from JS with contract     

 
  # web3.eth.default_account = web3.eth.accounts[0]

  # web3NFT = web3.eth.contract(abi=abi, bytecode=bytecode)

  # # Submit the transaction that deploys the contract
  # tx_hash = web3NFT.constructor('nft one', 'https://solcx.readthedocs.io/', 1000).transact({'from': web3.eth.accounts[0]})
  # tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, 60)
  # print(tx_receipt)





def connect_to_contract():

  web3.eth.defaultAccount = web3.eth.accounts[0]

  # compiled_contract = solcx.compile_files(
  #   ["contracts/CreatorNFT.sol"],
  #   output_values=["abi", "bin"],
  #   solc_version="0.8.4"
  # )

  # contract_id, contract_interface = compiled_contract.popitem()



  f = open('CreatorNFTABI.json')
  contract_abi = json.load(f)

  contract_address = "0x254dffcd3277C0b1660F6d42EFbB754edaBAbC2B"
  cs_contract_address = web3.toChecksumAddress(contract_address)
  # contract_abi = contract_interface['abi']
  NFTContract = web3.eth.contract(abi=contract_abi, address=cs_contract_address)

  # print( NFTContract.functions.seeSender().call() )

  print( NFTContract.functions.totalSupply().call() )
  print( NFTContract.functions.balanceOf('0xa160F6b9Cb594906a601c551c25C501DdAb5107A').call() )



 

def deploy_new():
  compiled_contract = solcx.compile_files(
    [
      "contracts/CreatorLazyNFT.sol", 
      "/Users/rahul/Documents/main/personal_learning_projects/fundamentals/node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol",
      "/Users/rahul/Documents/main/personal_learning_projects/fundamentals/node_modules/@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol",
      "/Users/rahul/Documents/main/personal_learning_projects/fundamentals/node_modules/@openzeppelin/contracts/access/AccessControl.sol",
      "/Users/rahul/Documents/main/personal_learning_projects/fundamentals/node_modules/@openzeppelin/contracts/utils/cryptography/ECDSA.sol",
      "/Users/rahul/Documents/main/personal_learning_projects/fundamentals/node_modules/@openzeppelin/contracts/utils/cryptography/draft-EIP712.sol"
    ],
    base_path="/Users/rahul/Documents/main/personal_learning_projects/fundamentals/nft_tutorial_two",
    allow_paths="*",
    output_values=["abi", "bin"],
    solc_version="0.8.4"
  )
  
  contract_id, contract_interface = compiled_contract.popitem()
  bytecode = contract_interface['bin']
  abi = contract_interface['abi']
  
  with open('CreatorLazyNFT.json', 'w') as f:
    json.dump(abi, f)


  web3.eth.default_account = web3.eth.accounts[0]
  web3NFT = web3.eth.contract(abi=abi, bytecode=bytecode)

  # Submit the transaction that deploys the contract
  tx_hash = web3NFT.constructor().transact({'from': web3.eth.accounts[0]})
  tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, 60)
  print(tx_receipt)





if __name__ == "__main__":
  blockchain_address = 'http://127.0.0.1:8545'
  web3 = Web3(HTTPProvider(blockchain_address))

  # connect_to_contract()

  # deploy_contract()
  # web3.eth.default_account = web3.eth.accounts[0]
  # print(web3.eth.accounts)
  
  # tx_hash = '0x6746c5a833f1d8b55fd28651d5f803905bef0d7644c2e9d1af598da555122f9c'
  # print( web3.eth.getTransaction(tx_hash) )
  

  deploy_contract()
  # deploy_new()





