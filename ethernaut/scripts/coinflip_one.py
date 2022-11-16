from brownie import CoinFlip, accounts, web3


def main():
  account_one, account_two = accounts[0], accounts[2]

  large_factor = 57896044618658097711785492504343953926634992332820282019728792003956564819968

  coinflip_contract = CoinFlip.deploy({
    'from': account_one,
    'gas_price': 50000
  })

  block_num = coinflip_contract.getBlockNumber()
  print(f'block-num: {block_num}')

  # previous_block_hash = web3.eth.getBlock(block_num-1)['hash']
  
  # print('prev-block-hash:', previous_block_hash)
  # print('int-of-hash:', int.from_bytes(previous_block_hash, byteorder='big') )
  
  # TODO: 
    # get the int of the hash 
      # for loop that goes through 10 guesses 


  # get blockhash of previous block 


# 0x2de047860953ae91814f5a5bbb4c4189ee4e4074573bf74714eb15bf868b3ef6
# 0x2de047860953ae91814f5a5bbb4c4189ee4e4074573bf74714eb15bf868b3ef6





