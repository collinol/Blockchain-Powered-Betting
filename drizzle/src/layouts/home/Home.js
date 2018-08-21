import React, { Component } from 'react'
import { AccountData, ContractData, ContractForm } from 'drizzle-react-components'
import logo from '../../logo.png'

class Home extends Component {
  render() {
    return (
      <main className="container">
        <div className="pure-g">
          <div className="pure-u-1-1 header">
            <img src={logo} alt="drizzle-logo" />
            <h1>Drizzle Examples</h1>
            <p>Examples of how to get started with Drizzle in various situations.</p>

            <br/><br/>
          </div>

          <div className="pure-u-1-1">
            <h2>Active Account</h2>
            <AccountData accountIndex="0" units="ether" precision="3" />

            <br/><br/>
          </div>

          <div className="pure-u-1-1">
            <h2>Wager</h2>
            <p>We wagering now.</p>
            <p><strong>Side One Volume</strong>: <ContractData contract="Wager" method="sideOneBetTotal" /></p>
            <p><strong>Side Two Volume</strong>: <ContractData contract="Wager" method="sideTwoBetTotal" /></p>
              <p><strong>Your Bet</strong>: Bet blank on Side blank </p>
              <h3>Bet Your Side and Amount</h3>
              <ContractForm contract="Wager" method="play" sendArgs={{from: this.props.accounts[0], value: 10000000000000000}} labels={['Side']} />
              <ContractForm contract="Wager" method="draw" labels={['Winner']} />

            <br/><br/>
          </div>

          <div className="pure-u-1-1">
            <h2>TutorialToken</h2>
            <p>Here we have a form with custom, friendly labels. Also note the token symbol will not display a loading indicator. We've suppressed it with the <code>hideIndicator</code> prop because we know this variable is constant.</p>
            <p><strong>Total Supply</strong>: <ContractData contract="TutorialToken" method="totalSupply" methodArgs={[{from: this.props.accounts[0]}]} /> <ContractData contract="TutorialToken" method="symbol" hideIndicator /></p>
            <p><strong>My Balance</strong>: <ContractData contract="TutorialToken" method="balanceOf" methodArgs={[this.props.accounts[0]]} /></p>
            <h3>Send Tokens</h3>
            <ContractForm contract="TutorialToken" method="transfer" sendArgs={{from: this.props.accounts[0], value: 100000000000000000}} labels={['To x', 'Amount to Send']} />

            <br/><br/>
          </div>


        </div>
      </main>
    )
  }
}

export default Home
