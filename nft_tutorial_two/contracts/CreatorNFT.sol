// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// import "/Users/rahul/Documents/main/personal_learning_projects/fundamentals/node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol";
// import "/Users/rahul/Documents/main/personal_learning_projects/fundamentals/node_modules/@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
// import "/Users/rahul/Documents/main/personal_learning_projects/fundamentals/node_modules/@openzeppelin/contracts/access/Ownable.sol";
// import "/Users/rahul/Documents/main/personal_learning_projects/fundamentals/node_modules/@openzeppelin/contracts/utils/Counters.sol";


// Regular Minting Approach (can't work in marketplace)

/// @custom:security-contact duggalr42@gmail.com
contract CreatorNFT is ERC721, ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    // specify max-nft-supply 
    uint256 private _maxTokenSupply; 

    constructor(string memory tokenName, string memory tokenSymbol, uint256 maxTokenSupply) ERC721(tokenName, tokenSymbol) {
      
        _maxTokenSupply = maxTokenSupply;

    }

    function safeMint(address to) public onlyOwner {

        // ensure max-supply for NFT is enforced.
        require( ERC721Enumerable.totalSupply() < _maxTokenSupply, "NFT max supply reached.");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);

    }

    // The following functions are overrides required by Solidity.

    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

}


