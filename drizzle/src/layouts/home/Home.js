import React, { Component } from 'react'
import { AccountData, ContractData, ContractForm } from 'drizzle-react-components'

class Home extends Component {

    constructor(props) {
        super(props);
        this.state = {value: ''};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        // alert('A name was submitted: ' + this.state.value);
        //event.preventDefault();
    }

  render() {
    return (
      <main className="container">
        <div className="pure-g">
          <div className="pure-u-1-1 header">
            <h1>Final Project</h1>
            <p>An ERC20 token built for wagering</p>

            <br/><br/>
          </div>

          <div className="pure-u-1-1">
            <h2>Active Account</h2>
            <AccountData accountIndex="0" units="ether" precision="3" />
            <ContractData contract="PredictiveBetToken" method="balanceOf" methodArgs={[this.props.accounts[0]]} /> <ContractData contract="PredictiveBetToken" method="symbol" hideIndicator />

            <br/><br/>
          </div>

          <div className="pure-u-1-1">
            <h2>Wager</h2>
            <p>Place your bets on the winning side.</p>
            <p><strong>Contract Address</strong>: <ContractData contract="Wager" method="thisContractAddr" /></p>
            <p><strong>Side One Volume</strong>: <ContractData contract="Wager" method="sideOneBetTotal" /></p>
            <p><strong>Side Two Volume</strong>: <ContractData contract="Wager" method="sideTwoBetTotal" /></p>
              <h3>Bet Your Side and Amount</h3>
              <ContractForm contract="Wager" method="play" sendArgs={{from: this.props.accounts[0], value: 0, gas: 471238, gasPrice: 15000000000000/4}} labels={['Bet side: 1 or 2', 'PBT Amount']} />
              <p></p>
              <h3>Choose winner (Owner only)</h3>
              <ContractForm contract="Wager" method="draw" sendArgs={{from: this.props.accounts[0], value: 0, gas: 471238, gasPrice: 15000000000000/4}} labels={['Winner']} />

            <br/><br/>
          </div>

          <div className="pure-u-1-1">
            <h2>PredictiveBetToken</h2>
            <p> PBT enables you to wager your tokens for safe, smart betting </p>
            <p><strong>Total Supply</strong>: <ContractData contract="PredictiveBetToken" method="totalSupply" methodArgs={[{from: this.props.accounts[0]}]} /> <ContractData contract="PredictiveBetToken" method="symbol" hideIndicator /></p>
            <p><strong>My Balance</strong>: <ContractData contract="PredictiveBetToken" method="balanceOf" methodArgs={[this.props.accounts[0]]} /></p>
            <h3>Send Tokens</h3>
            <ContractForm contract="PredictiveBetToken" method="transfer" sendArgs={{from: this.props.accounts[0], gas: 471238, gasPrice: 15000000000000/4}} labels={['To friend', 'Amount to Send']} />
            <p></p>
            <h3>Allot contract allowance aka approval</h3>
            <ContractForm contract="PredictiveBetToken" method="approve" sendArgs={{from: this.props.accounts[0], gas: 471238, gasPrice: 15000000000000/4}} labels={['To user', 'Amount to allow']} />
            <p></p>
            <h3> Exchange ETH/PBT</h3>
            <p>1 ETH = 1000 PBT</p>
              <p></p>
            <form onSubmit={this.handleSubmit}>
                <label>
                    <input type="text" value={this.state.value} onChange={this.handleChange} />
                </label>
            </form>
            <ContractForm contract="PredictiveBetToken" method="exchange" sendArgs={{from: this.props.accounts[0], value: this.state.value * 1000000000000000000, gas: 471238, gasPrice: 15000}} labels={['To x', 'Amount to Send']} />

            <br/><br/>
          </div>


        </div>
      </main>
    )
  }
}

export default Home
