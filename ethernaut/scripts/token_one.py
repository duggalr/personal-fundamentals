from brownie import Token, accounts, web3


def main():
  account_one, account_two = accounts[0], accounts[2]

  coinflip_contract = Token.deploy(20, {
    'from': account_one,
    'gas_price': 50000
  })

  account_one_balance = coinflip_contract.balanceOf(account_one)
  print(f"account-one-balance: {account_one_balance}")

  coinflip_contract.transfer(account_two, 22, {'gas_price': 50000})

  account_one_balance = coinflip_contract.balanceOf(account_one, {'gas_price': 50000})
  print(f"account-one-balance: {account_one_balance}")


  # block_num = coinflip_contract.getBlockNumber()
  # print(f'block-num: {block_num}')

 

 

