from brownie import Elevator, BuildingCT, accounts, web3


def main():
  account_one, account_two = accounts[0], accounts[2]

  elevator_contract = Elevator.deploy({
    'from': account_one,
    'gas_price': 50000
  })


  current_top_value = elevator_contract.top()
  print(f"current-top-value: {current_top_value}")

  building_contract = BuildingCT.deploy({
    'from': account_one,
    'gas_price': 50000
  })

  # place some money in building_contract first, for gas fees 
  elevator_contract.goTo(15, {
    'from': building_contract.address,
    'gas_price': 50000
  })

  current_top_value = elevator_contract.top()
  print(f"current-top-value: {current_top_value}")




