module.exports = async function main (callback) {
  try {
    // Our code will go here

    // // Retrieve accounts from the local node
    const accounts = await web3.eth.getAccounts();
    console.log(accounts)

    // const hashRate = await web3.eth.getHashrate()
    // console.log(hashRate)

    const Balance = await web3.eth.getBalance('0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1')
    console.log(Balance)

    const addrCode = await web3.eth.getCode('0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1')
    console.log(addrCode
      )

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


// TODO: 
  // what information can I get from the local blockchain? 
    // number of contracts, state of contract?

  // deploy an erc-20 token or nft <-- really master this stuff here 
    // 'add multi-user-support' and test with fake-users created by me first...
 

    


