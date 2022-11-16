import sys
from slither import Slither


# # Init slither
# slither = Slither('Coin.sol')

# for contract in slither.contracts:
#   # Print the contract's name
#   print(f'Contract: {contract.name}')
#   # Print the name of the contract inherited
#   print(f'\tInherit from{[c.name for c in contract.inheritance]}')
#   for function in contract.functions:
#     # For each function, print basic information
#     print(f'\t{function.full_name}:')
#     print(f'\t\tVisibility: {function.visibility}')
#     print(f'\t\tContract: {function.contract}')
#     print(f'\t\tModifier: {[m.name for m in function.modifiers]}')
#     print(f'\t\tIs constructor? {function.is_constructor}')


# if (function.contract != 'Coin'):
#   pass



slither = Slither('coin.sol')
coin = slither.get_contract_from_name('Coin')[0]

# Iterate over all the contracts
for contract in slither.contracts:
   # If the contract is derived from MyContract
   if coin in contract.inheritance:
      # Get the function definition  
      mint = contract.get_function_from_signature('_mint(address,uint256)')
      # If the function was not declarer by coin, there is a bug !  
      print(mint.contract)
      if mint.contract != coin:
           print(f'Error, {contract} overrides {mint}')


