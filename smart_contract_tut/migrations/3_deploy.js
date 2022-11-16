// migrations/2_deploy.js
const Box = artifacts.require('BasicERC20');

module.exports = async function (deployer) {
  await deployer.deploy(Box, 'Token Testing One', 't_one' );
};



