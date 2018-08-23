import PredictiveBetToken from './../build/contracts/PredictiveBetToken.json'
import Wager from './../build/contracts/Wager.json'


const drizzleOptions = {
  web3: {
    block: false,
    fallback: {
      type: 'ws',
      url: 'ws://127.0.0.1:8545'
    }
  },
  contracts: [
    PredictiveBetToken,
    Wager
  ],
  events: {
  },
  polls: {
    accounts: 1500
  }
}

export default drizzleOptions