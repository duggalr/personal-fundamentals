pragma solidity ^0.8.0;




contract TestingOne {

  function seeSender() public view returns(address) {
    
    address caller = msg.sender;
    return caller;

  }

}


// TODO: 
  // deploy actual ERC721 (from button-click on web-app)
    // test functionality (buying, minting, transfering, etc.)



 

