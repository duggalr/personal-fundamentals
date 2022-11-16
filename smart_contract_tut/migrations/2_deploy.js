// migrations/2_deploy.js
const Box = artifacts.require('SimpleStorage');

module.exports = async function (deployer) {
  await deployer.deploy(Box);
};



