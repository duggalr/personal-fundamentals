// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "./Elevator.sol";


contract BuildingCT {

  // uint private lastFloor = 15;
  Elevator elevatorCT = new Elevator();
  
  function isLastFloor(uint _floor) external returns (bool) {
    bool currentValue = elevatorCT.top();

    if (currentValue == false){
      return true;
    } else {
      return false;
    }

  }

} 




