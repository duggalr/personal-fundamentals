module.exports = async function main (callback) {
  try {
    
    const Box = artifacts.require('BasicERC20');
    const box = await Box.deployed();

    const tokenName = await box.name();
    const tokenSymbol = await box.symbol();
    console.log('tokenName/symbol:', tokenName, tokenSymbol);
        
    const pubKeyAddress = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1";

    // await box.mint(pubKeyAddress, 1000);

    const addrBalance = await box.balanceOf(pubKeyAddress);
    console.log('addr-balance:', addrBalance.toString());


    // const pkAddressTwo = "0x22d491Bde2303f2f43325b2108D26f1eAbA1e32b";
 
    // const transferSuccess = await box.transfer(pkAddressTwo, 2.75);
    // console.log('transferSuccess:', transferSuccess);

    // const secondAddrBalance = await box.balanceOf(pkAddressTwo);
    // console.log('second-addr-balance:', secondAddrBalance.toString());
    


    // // Set up a Truffle contract, representing our deployed SimpleStorage instance

    // const Box = artifacts.require('SimpleStorage');
    // const box = await Box.deployed();

    // // Call the get() function of the deployed SimpleStorage contract
    // const oldValue = await box.get();
    // console.log('SimpleStorage value is', oldValue.toString());

    // // used to estimate the gas cost of a specific function in the contract
    // const estimatedGas = await box.set.estimateGas(42)
    // // console.log('est-gas:', estimatedGas)

    // await box.set(23);

    // // Call the get() function of the deployed SimpleStorage contract
    // const newValue = await box.get();
    // console.log('SimpleStorage value is', newValue.toString());
    
    callback(0);

  } catch (error) {
    console.error(error);
    callback(1);
  }

};



    


