pragma solidity ^0.4.24;

import "openzeppelin-solidity/contracts/token/ERC20/StandardToken.sol";


contract PredictiveBetToken is StandardToken {

  string public name = "PredictiveBetToken";
  string public symbol = "PBT";
  uint public decimals = 18;
  uint public initialPrice = 1000000000000000;

  address public addr = address(this);
  
  uint public INITIAL_SUPPLY = 10000 * (10 ** uint256(decimals));

  constructor() public payable {
    totalSupply_ = INITIAL_SUPPLY;
    balances[addr] = INITIAL_SUPPLY;
  }

  function exchange() payable public {
	require(msg.value > 0);
      
    //balance[msg.sender] += msg.value;
    //balance[addr] -= msg.value
        
    this.transfer(msg.sender, msg.value / initialPrice);
	}
}
