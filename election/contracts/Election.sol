pragma solidity 0.4.24;

contract Election {

	struct Candidate{
		uint id;
		string name;
		uint voteCount;
	}

	mapping(uint => Candidate) public candidates;
	mapping(address => bool) public voters;

	uint public candidatesCount;

	function addCandidate (string _name) private {
		candidatesCount ++;
		candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
	}

	// Constructor
	constructor() public {
		addCandidate("Candidate 1");
		addCandidate("Candidate 2");	
	}


	event votedEvent (
		uint indexed _candidateId
	);

	function vote (uint _candidateId) public {
		//require that they haven't yet voted
		require(!voters[msg.sender]);

		//require a valid candidate
		require(_candidateId > 0 && _candidateId <= candidatesCount);

		//require that a voter has voted
		voters[msg.sender] = true;

		//update candidate vote count
		candidates[_candidateId].voteCount ++;
		
		//trigger voted event
		votedEvent(_candidateId);
	}

}
