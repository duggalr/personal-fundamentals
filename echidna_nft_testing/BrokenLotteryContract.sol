// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;



contract BrokenLottery {

  // mapping(address => uint) public balances;

  address private _owner;
  uint256 totalAmount;

  constructor() {

    _owner = msg.sender;

  }

  // Reward Event
  event Reward(address _to);

  modifier onlyOwner {
    require(msg.sender == _owner, "Function only callable by owner.");
    _;
  }

  function deposit(uint256 _amount) external payable {

    // balances[msg.sender] += amount;
    totalAmount += _amount;  // Prone to overflow

  }

  // Broken and always give reward to owner
  function reward() onlyOwner external payable {
    
    totalAmount = 0;
    (bool success, bytes memory data) = _owner.call{value:totalAmount}("");
    require(success, "Transaction Failed...");

    emit Reward(msg.sender);

  }

}


