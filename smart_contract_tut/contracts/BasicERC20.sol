pragma solidity ^0.8.0;


// Basic ERC-20 Token

contract BasicERC20 {

  // state? 
    // supply of tokens availabe --> public

  mapping(address => uint256) private _balances; 

  uint256 private _totalSupply;
  string private _name; 
  string private _symbol;

  event Transfer(address indexed from, address indexed to, uint256 value);

  /* 
    All two of these values are immutable: they can only be set once during construction.
  */
  constructor(string memory name_, string memory symbol_) {
    _name = name_;
    _symbol = symbol_;
  }


  /* 
    Return Token Name
  */
  function name() public view returns (string memory) {
    return _name;
  }
  
  /* 
    Return Token Symbol
  */
  function symbol() public view returns (string memory){
    return _symbol;
  }

  /*
    Return Decimal Places to use
  */
  function decimals() public view returns (uint8) {
    return 18;
  }

  /* 
    Return Total Supply
  */
  function totalSupply() public view returns (uint256) {
    return _totalSupply;
  }

  /* 
    Returns the amount of tokens owned by `account`.
  */
  // TODO: do we really want this to be public?
  function balanceOf(address account) public view returns (uint256) {
    return _balances[account];
  }

  /* 
    Public function for transfer()
  */
  function transfer(address to, uint256 amount) public returns (bool){
    address from = msg.sender;  // callers address
    _transfer(from, to, amount);
    return true;
  }

  /* 
    Transfer token from one address to another
  */
  function _transfer(address from, address to, uint256 amount) internal {

    // address from = msg.sender;  // callers address
    require(from != address(0), "ERC20: transfer from the zero address");
    require(to != address(0), "ERC20: transfer to the zero address");

      // _beforeTokenTransfer(from, to, amount);

    uint256 fromBalance = _balances[from];
    require(fromBalance >= amount, "ERC20: transfer amount exceeds balance");

    _balances[from] = fromBalance - amount;
    _balances[to] += amount;

    // TODO: test contract; what would happen if I don't emit the Transfer() event?
    emit Transfer(from, to, amount);

  }


  /* 
    Mint Tokens --> publically available for everyone
  */
  function mint(address account, uint256 amount) public {
    require(account != address(0), "ERC20: mint to the zero address");

    _totalSupply += amount;
    _balances[account] += amount;
    emit Transfer(address(0), account, amount);

  }



}




