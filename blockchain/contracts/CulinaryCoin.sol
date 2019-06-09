pragma solidity ^0.5.8;

import "openzeppelin-solidity/contracts/token/ERC20/ERC20.sol";

contract CulinaryCoin is ERC20 {
  string public name = "Culinary Coin";
  string public symbol = "A2CC";
  uint8 public decimals = 2;
  uint public INITIAL_SUPPLY = 10000000;

  constructor() public {
    _mint(msg.sender, INITIAL_SUPPLY);
  }
}
