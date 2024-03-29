// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;





interface Building {
  function isLastFloor(uint) external returns (bool);
}

contract Elevator {
  bool public top;
  uint public floor;

  function goTo(uint _floor) public {
    Building building = Building(msg.sender);  // msg.sender is BuildingCT contract with isLastFloor implemented

    if (! building.isLastFloor(_floor)) {
      floor = _floor;
      top = building.isLastFloor(floor);
    }
  }
  

}





