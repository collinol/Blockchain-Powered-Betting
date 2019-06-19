var HDWalletProvider = require("truffle-hdwallet-provider");

var infura_apikey ="7c98627257b34de18c5e02c3a38baef7XXXXXX";
var mnemonic = "issue tape voyage cruel term deal disorder wrist happy cruel eight piano";

module.exports = {
  migrations_directory: "./migrations",
  networks: {
    development: {
      host: "localhost",
      port: 8545,
      network_id: "*" // Match any network id
    },
    ropsten: {
      provider: function() {
        return new HDWalletProvider(mnemonic, "https://ropsten.infura.io/"+infura_apikey)},
      network_id: 3
    },
    ropsten2: {
       network_id: 3,
       host: "localhost",
       port:  8545,
       gas:   2900000
    }
  },
  solc: {
    optimizer: {
      enabled: true,
      runs: 500
    }
  }, 
};
