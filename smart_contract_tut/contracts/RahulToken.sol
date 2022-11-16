// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @custom:security-contact duggalr42@gmail.com
contract RahulToken is ERC20, ERC20Burnable, Ownable {
    constructor() ERC20("Rahul Token", "RD") {
        _mint(msg.sender, 10000 * 10 ** decimals());
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}


// greeter = web3.eth.contract(
//     address=tx_receipt.contractAddress,
//     abi=abi
// )

// fix the wait-for-transaction-error and go from there

 


 