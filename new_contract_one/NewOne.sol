//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.4;
pragma abicoder v2; // required to accept structs as function parameters


import "./contracts/token/ERC721/ERC721.sol";
// import "./contracts/token/ERC721/extensions/ERC721Enumerable.sol";
// import "./contracts/access/Ownable.sol";
// import "./contracts/utils/Counters.sol";



contract empty1 is ERC721{

  string public userString;

  constructor(string memory testing) ERC721("LazyNFT", "LAZ") {

    userString = testing;

  }
    
  function helloWorld() public pure returns(string memory) {
    return "Hello World!";
  }

  // function simple_add(uint256 a, uint256 b) public pure returns (uint256){
  //   return a+b;
  // }

}






