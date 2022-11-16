module.exports = async function main (callback) {
  try {

    const Box = artifacts.require('RahulToken');
    const box = await Box.deployed();

    const tokenName = await box.name();
    const tokenSymbol = await box.symbol();
    console.log('tokenName/symbol:', tokenName, tokenSymbol);

    const mainPubKeyAddress = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1";
    const otherPubKeyAddress = "0xFFcf8FDEE72ac11b5c542428B35EEF5769C409f0";

    const tokenSupply = await box.totalSupply();
    console.log('token supply:', tokenSupply.toString());
      
    const pkBalance = await box.balanceOf(mainPubKeyAddress
      );
    console.log('pkBalance:', pkBalance.toString());

    // const amt = 5; // assume 5 tokens were bought
    // const transferSuccess = await box.transfer(otherPubKeyAddress, amt);
    // console.log('transfer-success:', transferSuccess);
    



    callback(0);
    
  } catch (error) {
    
    console.error(error);
    callback(1);

  }


}