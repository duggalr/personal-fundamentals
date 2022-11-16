const Box = artifacts.require('Greeter');

module.exports = async function (deployer) {
  await deployer.deploy(Box);
};

