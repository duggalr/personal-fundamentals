pragma solidity ^0.8.0;



// TODO:
  // deploy this on local/public-testnets
    // test with python and Solidity testing tools (**max supply)
    // create and run tests <-- fuzzy?
    // before moving forward with CC <-- **go through a good amount of the Ethernaut exercises to get very comfortable with solidity
      // pretty positive there are risks in below code


// Basic NFT Example with openzep
contract ERC721 {

  address private _contractOwner;

  string private _name;
  string private _uri;
  uint256 private _totalSupply;
  uint256 private _currentSupply;

  mapping(address => uint256) private _balances;  // keep track of ownership through this
  mapping(uint256 => address) private _owners;  // mapping from tokenId to owner address

  event Transfer(address indexed from, address indexed to, uint256 value); // used in transfer and minting


  constructor(string memory name, string memory uri, uint256 totalSupply){
    address from = msg.sender; // callers address
    assert( from != address(0) );  // should never be possible but still here (https://ethereum.stackexchange.com/questions/15166/difference-between-require-and-assert-and-the-difference-between-revert-and-thro)
    _contractOwner = from;  // the caller is the owner; during initial deployment, this is set, not mutable afterwards.

    _name = name;
    _uri = uri;
    _totalSupply = totalSupply;  // max-supply (minting not possible if greater than this value)
    _currentSupply = 0;  // set te current-supply = 0

  }

  function getName() public view returns (string memory) {
    return _name;
  }

  function getTokenURI() public view returns (string memory) {
    return _uri;
  }

  function getTokenTotalSupply() public view returns (uint256) {
    return _totalSupply;
  }

  function getCurrentNFTSupply() public view returns (uint256) {
    return _currentSupply;
  }


  function _exists(uint256 tokenId) internal view virtual returns (bool) {
    return _owners[tokenId] != address(0);
  }


  function _mint(address to, uint256 tokenId) internal {

    require(to != address(0), "ERC721: mint to zero address.");
    require(!_exists(tokenId), "ERC721: token already minted.");

    _balances[to] += 1;
    _owners[tokenId] = to;

    _currentSupply += 1;
    _totalSupply -= 1;

    emit Transfer(address(0), to, tokenId);  // address-(0) when minting

  }


  function getBalance(address to) public view returns (uint256) {

    require(to != address(0), "ERC721: zero address.");

    return _balances[to];

  }


  // TODO: tricky part with security here is, can user input 'corrupted-input' which can cause memory-leak/overflow/comprise?
  function getTokenOwner(uint256 tokenId) public view returns (address){
    
    address tokenOwner = _owners[tokenId];
    return tokenOwner;

  }



  function _checkOwner() internal view virtual {
    require(_contractOwner == msg.sender, "Ownable: caller is not the owner");

  }

  function safeMint(address to, uint256 tokenId) public { 

    _checkOwner();

    uint256 newSupply = _currentSupply + 1;    
    require( (newSupply <= _totalSupply), "You have reached the max supply of total tokens." );

    _mint(to, tokenId);

  }


  function _transfer(address from, address to, uint256 tokenId) internal {

    require(to != address(0), "ERC20: transfer to the zero address");

    _balances[from] -= 1;
    _balances[to] += 1;
    _owners[tokenId] = to;
    emit Transfer(from, to, tokenId);    

  }


  function transferFrom(address to, uint256 tokenId) public returns (bool) {
    address from = msg.sender;  // callers address

    assert( from != address(0) );  // should never be possible but still here (https://ethereum.stackexchange.com/questions/15166/difference-between-require-and-assert-and-the-difference-between-revert-and-thro)

    address tokenOwner = _owners[tokenId];
    
    require(from == tokenOwner, "Token owner public-key address must be same as caller's public-key address.");
    require(to != address(0), "ERC20: transfer to the zero address");

    _transfer(from, to, tokenId);

    return true;    
 
  }



}






