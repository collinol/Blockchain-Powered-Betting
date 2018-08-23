pragma solidity ^0.4.24;

import "./PredictiveBetToken.sol";

contract Wager {
    
    uint public sideOneBetTotal;
    uint public sideTwoBetTotal;

    string public test;

    address Owner;

    address public thisContractAddr = address(this);
    
    Player[] public sideOnePlayers;
    Player[] public sideTwoPlayers;

    struct Player {
        address addr;
        uint betAmount;
    }
    
    mapping (address => bool) public uniquePlayers;
    
    constructor(address _contactAddress) public payable {
        Owner = _contactAddress;
    }

    modifier onlyOwnerOf() {
        require(msg.sender == Owner);
        _;
    }

    function play(uint _side, uint _amount) payable public {
        require (uniquePlayers[msg.sender] == false);
        PredictiveBetToken instance = PredictiveBetToken(Owner);
		require(instance.allowance(msg.sender, this) > 0);
		
        if (_side == 1) {
            sideOnePlayers.push(Player(msg.sender, _amount));
            sideOneBetTotal += _amount;
        } else {
            sideTwoPlayers.push(Player(msg.sender, _amount));
            sideTwoBetTotal += _amount;
        }
        uniquePlayers[msg.sender] = true;
        instance.transferFrom(msg.sender, address(this), _amount);
    }
    
    function draw(uint _winningSide) external {
        
        uint betAmount;
        uint i;
        uint winnings;
        PredictiveBetToken instance = PredictiveBetToken(Owner);

        
        if (_winningSide == 1) {
            for (i = 0; i < sideOnePlayers.length; i++){
                betAmount = sideOnePlayers[i].betAmount;
                winnings = betAmount + ((betAmount/sideOneBetTotal) * sideTwoBetTotal);
                // sideOnePlayers[i].addr.transfer(winnings);
                instance.transfer(sideOnePlayers[i].addr, winnings);
            }
        } else {
            for (i = 0; i < sideTwoPlayers.length; i++){
                betAmount = sideOnePlayers[i].betAmount;
                winnings = betAmount + ((betAmount/sideOneBetTotal) * sideOneBetTotal);
                // sideTwoPlayers[i].addr.transfer(winnings);
                instance.transfer(sideTwoPlayers[i].addr, winnings);

            }
        }
       sideOneBetTotal = 0;
       sideTwoBetTotal = 0;

    }
}
