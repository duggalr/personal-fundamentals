from brownie import Fallback, accounts



def main():
  account_one, account_two = accounts[0], accounts[2]

  fallback_contract = Fallback.deploy({
    'from': account_one,
    'gas_price': 50000
  })
  # print(fallback_contract)

  # Deployed on Account-One 
  sender_contrib = fallback_contract.getContribution({'from': account_one})
  print('sender-contrib:', sender_contrib)

  main_balance = fallback_contract.getBalance()
  print('main-balance:', main_balance)

  # Account-Two
  print('account-two:', account_two)
  contract_owner = fallback_contract.getOwner({'from': account_two})
  print('contract-owner:', contract_owner)


  # fallback_contract.withdraw({'from': account_two, 'gas_price': 50000})  ## should fail right  now
  
  fallback_contract.contribute({
    'from': account_two, 
    'value': 5,
    'gas_price': 50000
  })

  acc_two_contribution = fallback_contract.getContribution({
    'from': account_two
  })
  print('acc-two-contrib:', acc_two_contribution)

  # this is to transfer ETH from one account to the other (or to a contract)
  account_two.transfer(fallback_contract, 100, priority_fee="10 gwei")

  contract_owner = fallback_contract.getOwner({'from': account_two})
  print(f'account-two: {account_two} / contract-owner: {contract_owner}')

  print(f'contract-balance: {fallback_contract.balance()}')

  fallback_contract.withdraw({
    'from': account_two,  
    'gas_price': 50000
  })

  print(f'contract-balance: {fallback_contract.balance()}')




  # token_price_eth = 0.1
  # token_price_gwei = 0.1 * (10**19)
  # creator_contract = CreatorNFT.deploy("RahulTestOne", "RTO", 500, 20, token_price_gwei, "https://docs.soliditylang.org/", {"from": account_one})

  # token_name = creator_contract.name()
  # token_symbol = creator_contract.symbol()
  # token_price = creator_contract.getTokenPrice()

  # print(f"token-name: {token_name} / token-symbol: {token_symbol} / token-price: {token_price}")
  
  # # val = creator_contract.getValue()
  # # print('val:', val)

  # creator_contract.safeMint(2, {'value': (0.1 * (10**19))*2, 'from': account_two})
  # print( 'main-account-balance:', accounts[0].balance() )
  # print( 'other-account-balance:', accounts[2].balance() )
  # print('platform-account-balance:', accounts[-1].balance())
  


  # creator_contract.safeMint(1, {'value': 0.1 * (10**19)})
  
  # total_token_supply = creator_contract.totalSupply()
  # print(f"current-token-supply: {total_token_supply}")

  # balance_account_one = creator_contract.balanceOf(account_one) 
  # balance_account_two = creator_contract.balanceOf(account_two)
  # print(f"account-one-balance: {balance_account_one} / account-two-balance: {balance_account_two}")

  # token_id = creator_contract.tokenByIndex(0)
  # print(f"current-token: {token_id}")

  # token_uri = creator_contract.tokenURI(token_id)
  # print(f"token-uri:", token_uri)

  # creator_contract.safeMint(account_two, 100)
  # total_supply = creator_contract.totalSupply()
  # print('ts:', total_supply)

  # basic_contract.storeNumber(101, {'from': account})
  # current_num = basic_contract.readNumber()
  # print(f"current-number: {current_num}")


# 0x9d225E305758483AdD2A372B444acda6c0c21Fb1
# 82fce336756c0134b9144e4cb360a299369372f8248722fda0b37b5573a08128
 
 
# string memory tokenName, string memory tokenSymbol, uint256 totalSupply, uint256 maxNumPerSale, uint256 _tokenPrice






