// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./contracts/utils/math/SafeMath.sol";

// TODO: 
  // verify contract logic is good 
    // add tests 
    // test with Slither / Echidna 
  

contract Lottery {

  address private _owner;
  uint256 public totalAmount = 0;
  uint256 public currentPoolAmount = 0;
  address[] public addresses;
  address[] public previousWinners;

  // Reward Event
  event Reward(address _to, uint256 _amount);

  // Owner Protection Modifier
  modifier onlyOwner {
    require(msg.sender == _owner, "Function only callable by owner.");
    _;
  }

  constructor() {
    _owner = msg.sender;
  }


  function addressLength() external view returns (uint256){

    return addresses.length;

  }


  function checkDuplicate(address _addr) public view returns (bool){
    
    if (addresses.length == 0){
      return false;
    } else {

      require( addresses.length > 0, " <0? something weird is happening...");

      for (uint i=0; i <= addresses.length-1; i++ ){
        if ( addresses[i] == _addr ) {
          return true;          
        }
      }
      return false;

    }

  }


  function deposit() external payable {
    
    require(msg.value > 0, "Deposit must be > 0.");

    bool dup = checkDuplicate(msg.sender);
    if (!dup){
      
      addresses.push(msg.sender);  // can't have duplicates; must be unique or else, unfavourable odds

    }

    (bool _addBoolOne, uint256 _totalValueOne) = SafeMath.tryAdd(currentPoolAmount, msg.value);
    currentPoolAmount = _totalValueOne;
    (bool _addBoolTwo, uint256 _totalValueTwo) = SafeMath.tryAdd(totalAmount, msg.value);
    totalAmount = _totalValueTwo;
    require( _addBoolOne, "error when adding amount to pool" );
    require( _addBoolTwo, "error when adding amount to pool" );
    
  }


  function reward(uint256 randomNumber) external payable onlyOwner {
 
    require( addresses.length > 0, "No Pool, thus no reward...");
    require( currentPoolAmount > 0, "No Pool, thus no reward..." );
    require (randomNumber >= 0 && randomNumber < addresses.length, "Random Number not in correct range." );

    address winner = addresses[randomNumber];
    previousWinners.push(winner);

    emit Reward(winner, currentPoolAmount);

    currentPoolAmount = 0;
    (bool success, bytes memory data) = winner.call{value: currentPoolAmount}("");
    require(success, "Transfer did not succeed");

  }
  

  // Last Resort, incase something goes wrong...
  function destory() external payable onlyOwner{

    selfdestruct( payable(msg.sender) );

  }  
  

}

