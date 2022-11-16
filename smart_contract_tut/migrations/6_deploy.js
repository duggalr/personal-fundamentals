// migrations/4_deploy.js
const Box = artifacts.require('RahulToken');

module.exports = async function (deployer) {
  await deployer.deploy(Box);
};

