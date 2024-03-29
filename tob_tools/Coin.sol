// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

contract Coin{

    address owner = msg.sender;

    mapping(address => uint) balances;

    // _mint must not be overriden
    function _mint(address dst, uint val) internal virtual{
        require(msg.sender == owner);
        balances[dst] += val;
    }

    function mint(address dst, uint val) public{
        _mint(dst, val);
    }

}

contract MyCoin is Coin{

    event Mint(address, uint);

    // function _mint(address dst, uint val) internal override{
    //     balances[dst] += val;
    //     emit Mint(dst, val);
    // }

}

