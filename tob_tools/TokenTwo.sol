// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;


contract Ownership{
  address owner = msg.sender;

  function Owner() internal{
      owner = msg.sender;
  }

  modifier isOwner(){
      require(owner == msg.sender);
      _;
  }

}

contract Pausable is Ownership{
  
  bool is_paused;

  modifier ifNotPaused(){
    require(!is_paused);
    _;
  }

  function paused() isOwner public{
    is_paused = true;
  }

  function resume() isOwner private{
    is_paused = false;
  }

}

contract Token is Pausable{
  mapping(address => uint) public balances;

  function transfer(address to, uint value) ifNotPaused public{
      uint256 initialSenderBalance = balances[msg.sender];
      uint256 initialToBalance = balances[msg.sender];

      balances[msg.sender] -= value;
      balances[to] += value;
      assert(balances[msg.sender] <= initialSenderBalance);
      assert(balances[to] >= initialToBalance );
  }
  
}


// // Exercise 4
contract TestToken is Token{

  address echidna_caller = msg.sender;

  constructor() {
    balances[echidna_caller] = 10000;
    paused(); // pause the contract
    owner = address(0x0); // lose ownership
  }

  function echidna_transfer() public view returns (bool) {
    return balances[echidna_caller] <= 10000;
  }

}



// contract MintableToken is Token{

//   int totalMinted;
//   int totalMintable;

//   constructor(int _totalMintable) {
//     totalMintable = _totalMintable;
//   }

//   function mint(uint value) isOwner() public{ // prone to overflow which allows balance to go to 0, and msg.sender to mint more
//     int c = int(value) + totalMinted;
//     require(c > 0 && c < totalMintable, "overflow");
//     totalMinted += int(value);
//     balances[msg.sender] += value;
//   }

// }


// // This is for exercises 1-2
// contract TestToken is Token{
  
//   address echidna_caller = msg.sender;

//   constructor() {
//     balances[echidna_caller] = 10000;
//     paused(); // pause the contract
//     owner = address(0x0); // lose ownership

//   }

//   function echidna_test_balance() public view returns (bool) {
//     return balances[echidna_caller] <= 10000;
//   }

//   function echidna_no_transfer() public view returns (bool) {
//     return is_paused == true;
//   }

// }


// // Exercise 3
// contract TestToken is MintableToken(10000) {
//   address echidna_caller = msg.sender;  

//   // update the constructor
//   constructor() {
//     owner = echidna_caller;
//   }

//   // add the property
//   function echidna_test_balance() public view returns (bool) {
//     return balances[echidna_caller] <= 10000;
//   }

// }





