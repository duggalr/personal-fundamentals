// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "./contracts/token/ERC721/ERC721.sol";
import "./contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "./contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "./contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "./contracts/access/Ownable.sol";
import "./contracts/utils/Counters.sol";
import "./contracts/utils/math/SafeMath.sol";
import "./contracts/security/ReentrancyGuard.sol";


/// @custom:security-contact creatorcoin42@gmail.com
contract NFTMain is ERC721, ERC721Enumerable, ERC721URIStorage, ERC721Burnable, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    /// Main Public Key
    address private immutable _platformAddress = 0x4F25F664e5A0fbc4f8f6b5ea2e98c9b9263A84Fa;
    uint256 private immutable _platformFee = 3;

    /// Token Metadata
    uint256 private _maxTokenSupply;
    uint256 private _maxTokenPerSale;
    uint256 private _tokenPrice;  // will be in WEI denomination 
    string private _baseTokenURI;
    address private _deployerAddress;


    constructor(string memory tokenName, string memory tokenSymbol, uint256 totalSupply, uint256 maxNumPerSale, uint256 _userTokenPrice, string memory _userTokenURI) ERC721(tokenName, tokenSymbol) {

        require(maxNumPerSale > 0, "Max Token Per Sale must be >0.");
        require(totalSupply > 0, "Max Token Supply must be >0.");
        require( totalSupply >= maxNumPerSale, "Total Supply must be greater or equal to max token number per sale.");

        _maxTokenSupply = totalSupply;
        _maxTokenPerSale = maxNumPerSale;
        _tokenPrice = _userTokenPrice;  // will be in WEI denomination 
        _baseTokenURI = _userTokenURI;

        _deployerAddress = msg.sender;
 
    }


    function getTokenPrice() external view returns(uint256) {        
        return _tokenPrice;
    }

    function getMaxTokenSupply() external view returns (uint256) {
        return _maxTokenSupply;
    }

    function getCurrentTokenID() external view returns (uint256) {
        return _tokenIdCounter.current();
    }


    function _runMint(uint256 _numTokens) private {

        // Loop to mint amount requested, after the money has been transferred
        for(uint256 i = 0; i < _numTokens; i++) {
            _safeMint(msg.sender, _tokenIdCounter.current());
            _setTokenURI(_tokenIdCounter.current(), _baseTokenURI);
            _tokenIdCounter.increment();
        }

    }

    function safeMint(uint256 _numTokens) external payable nonReentrant {
      
        require( _numTokens > 0 && _numTokens <= _maxTokenPerSale, "Amount of NFTs exceeds the amount of NFTs you can purchase at a single time. Or amount requested is 0.");

        (bool _addBool, uint256 _totalValue) = SafeMath.tryAdd(_tokenIdCounter.current(), _numTokens);
        require(_addBool);
        require(_maxTokenSupply >= _totalValue, "Not enough tokens left to buy.");

        (bool _mulBool, uint256 _totalEthCost) = SafeMath.tryMul(_tokenPrice, _numTokens);
        require(_mulBool);
        require(msg.value == _totalEthCost, "Amount of ether sent not correct.");  // require msg.value to be exactly correct

        // "3%"-Fee, given to platform;
        (bool _mulBoolNew, uint256 _platformInitialCost) = SafeMath.tryMul(_platformFee, msg.value); 
        require(_mulBoolNew);
        (bool _divBool, uint256 _platformCost) = SafeMath.tryDiv(_platformInitialCost, 100);
        require(_divBool);
        (bool _subBool, uint256 _remainingValue) = SafeMath.trySub(msg.value, _platformCost);
        require(_subBool);

            
        _runMint(_numTokens); // check-effects-interactions pattern

        // pay platform
        (bool platformSent, bytes memory platformData) = payable(_platformAddress).call{value: _platformCost}("");  // send to platform
        require(platformSent, "Failed to send Ether");
        
        // pay creator
        (bool sent, bytes memory data) = payable(_deployerAddress).call{value: _remainingValue}("");  // sent to creator
        require(sent, "Failed to send Ether"); 
 
    }


    // Callable by owner to increase supply
    function increaseTokenSupply(uint256 newSupply) public onlyOwner {

        require(newSupply > 0 && newSupply > _maxTokenSupply, "Max Token Supply must be >0 and greater than previous maxTokenSupply.");

        _maxTokenSupply = newSupply;

    }


    // The following functions are overrides required by Solidity.

    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
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


 


 