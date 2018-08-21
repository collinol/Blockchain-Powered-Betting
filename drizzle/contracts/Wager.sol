pragma solidity ^0.4.24;

contract Wager {
    
    uint public sideOneBetTotal;
    uint public sideTwoBetTotal;

    string public test;

    Player[] public sideOnePlayers;
    Player[] public sideTwoPlayers;

    struct Player {
        address addr;
        uint betAmount;
    }
    
    mapping (address => bool) public uniquePlayers;
    
    constructor() public payable {
        test = "is this working?";
    }

    function play(uint _side) payable public {
        require (msg.value >= 1000000000000000);
        require (uniquePlayers[msg.sender] == false);
        if (_side == 1) {
            sideOnePlayers.push(Player(msg.sender, msg.value));
            sideOneBetTotal += msg.value;
        } else {
            sideTwoPlayers.push(Player(msg.sender, msg.value));
            sideTwoBetTotal += msg.value;
        }
        uniquePlayers[msg.sender] = true;
    }
    
    function draw(uint _winningSide) external {
        
        uint betAmount;
        uint i;
        uint winnings;
        
        if (_winningSide == 1) {
            for (i = 0; i < sideOnePlayers.length; i++){
                betAmount = sideOnePlayers[i].betAmount;
                winnings = betAmount + ((betAmount/sideOneBetTotal) * sideTwoBetTotal);
                sideOnePlayers[i].addr.transfer(winnings);
            }
        } else {
            for (i = 0; i < sideTwoPlayers.length; i++){
                betAmount = sideOnePlayers[i].betAmount;
                winnings = betAmount + ((betAmount/sideOneBetTotal) * sideOneBetTotal);
                sideTwoPlayers[i].addr.transfer(winnings);
            }
        }
    }
}
