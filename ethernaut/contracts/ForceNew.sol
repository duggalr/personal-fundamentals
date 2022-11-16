// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;


contract ForceNew {

  function transfer() external payable {
    revert();
  }

  receive() external payable {}

  function transferKing(address _from, address _to) external payable {

    // payable(_from).to(_to, msg.value);
    payable(_to).transfer(msg.value);

  }

}



