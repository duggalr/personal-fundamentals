// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import './ExampleToken.sol';


contract EchidnaTokenTest is ExampleToken{

  // balance must be >= 0
  function echidna_balance_gte_zero() public view returns(bool){
    return balances[msg.sender] >= 0;
  }

}


// TODO: 
  // create a harder, realistic contract (inputs/assertions, etc.)
  // use echidna on that
  // create a lottery contract? 


