from brownie import Lottery, accounts
import random



def main():
  deposit_addresses_list = []

  account_zero = accounts[0]
  account_one = accounts[1]
  account_two = accounts[2]

  lottery = Lottery.deploy({"from": account_zero, "gas_price": 25000})
  
  lottery.deposit({"from": account_zero, "value": 27000})
  lottery.deposit({"from": account_one, "value": 50000})
  lottery.deposit({"from": account_two, "value": 100000})
  lottery.deposit({"from": account_two, "value": 500000})

  deposit_addresses_list.append(account_zero)
  deposit_addresses_list.append(account_one)
  deposit_addresses_list.append(account_two)

  # account_zero_dup = lottery.checkDuplicate(account_zero.address)
  # account_one_dup = lottery.checkDuplicate(account_one.address)
  # account_two_dup = lottery.checkDuplicate(account_two.address)

  print(f"Contract Balance: {lottery.balance()} / Current Pool Amount: {lottery.currentPoolAmount()} / All-time Amount: {lottery.totalAmount()}")

  random_idx = random.randrange(0, len(deposit_addresses_list))

  lottery.reward(random_idx, {"from": account_zero, "gas_price": 25000})
  print(f"Random-Idx: {random_idx} / Last Winner Balance: {deposit_addresses_list[random_idx].balance()}")

  print(f"Contract Balance: {lottery.balance()} / Current Pool Amount: {lottery.currentPoolAmount()} / All-time Amount: {lottery.totalAmount()}")

  lottery.deposit({"from": account_zero, "value": 27000})
  lottery.deposit({"from": account_one, "value": 50000})
  lottery.deposit({"from": account_two, "value": 100000})
  lottery.deposit({"from": account_two, "value": 500000})

  lottery.reward(random_idx, {"from": account_zero, "gas_price": 25000})
  print(f"Random-Idx: {random_idx} / Last Winner Balance: {deposit_addresses_list[random_idx].balance()}")

  print(f"Contract Balance: {lottery.balance()} / Current Pool Amount: {lottery.currentPoolAmount()} / All-time Amount: {lottery.totalAmount()}")


