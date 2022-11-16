pragma solidity ^0.8.0;



// Basic ERC721 Token

contract BasicERC721 {

  // Mapping from token ID to owner address
  mapping(uint256 => address) private _owners;

  // Mapping owner address to token count
  mapping(address => uint256) private _balances;

  string private _name; 
  string private _symbol;

  event Transfer(address indexed from, address indexed to, uint256 value);


  constructor(string memory name_, string memory symbol_) {
    _name = name_;
    _symbol = symbol_;
  }


  /*
    Return Name
  */
  function name() public view returns (string memory) {
    return _name;
  }

  /*
    Return Symbol
  */
  function symbol() public view returns (string memory) {
    return _symbol;
  }

  /*
    Get balance, given owner address
  */
  function balanceOf(address owner) public view returns (uint256) {
    require(owner != address(0), "ERC721: address zero is not a valid owner");
    return _balances[owner];
  }

  /* 
    Return owner, given token-id
  */
  function ownerOf(uint256 tokenId) public view virtual returns (address) {
    address owner = _owners[tokenId];
    require(owner != address(0), "ERC721: invalid token ID");
    return owner;
  }

  /*
    transfer NFT-token ownership from one address to another
  */
  function transferFrom(
    address to,
    uint256 tokenId
  ) public returns (bool){

    // require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: caller is not token owner nor approved");
    // _transfer(from, to, tokenId);

    address from = msg.sender;  // callers address

    address owner = _owners[tokenId];
    require(owner == from, "ERC721: caller is not token owner");

    _transfer(from, to, tokenId);
    return true;
  

  }

  /* 
    private transfer method  
  */
  function _transfer(
    address from,
    address to,
    uint256 tokenId
  ) internal {

    require(to != address(0), "ERC20: transfer to the zero address");

    _balances[from] -= 1;
    _balances[to] += 1;
    _owners[tokenId] = to;

    emit Transfer(from, to, tokenId);

  }

  /* 
    mint
  */
  function _mint(address to, uint256 tokenId) internal{

    require(to != address(0), "ERC721: mint to the zero address");
    require(!(_owners[tokenId] != address(0)), "ERC721: token already minted");

    _balances[to] += 1;
    _owners[tokenId] = to;

    emit Transfer(address(0), to, tokenId);

  }



}



// NFT Process: 
  // Mint --> this is when 'nft-token-id' is created and specific owner is assigned (deployer of contract)
    // approval: 
      // when owner sells to another person, approval-access of previous-owner is gone; transferred to new owner






