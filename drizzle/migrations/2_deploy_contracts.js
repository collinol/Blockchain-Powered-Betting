var PredictiveBetToken = artifacts.require("PredictiveBetToken");
var Wager = artifacts.require("Wager");


module.exports = (deployer) => {

  deployer.deploy(PredictiveBetToken).then(function() {
    return deployer.deploy(Wager, PredictiveBetToken.address)
  });
};