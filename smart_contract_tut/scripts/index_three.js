module.exports = async function main (callback) {
  try {

    const Box = artifacts.require('BasicNFT');
    const box = await Box.deployed();

    const tokenName = await box.name();
    const tokenSymbol = await box.symbol();
    console.log('tokenName/symbol:', tokenName, tokenSymbol);

    const pubKeyAddress = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1";

    // Mint NFT
    // const nftTokenID = await box.createNewToken(pubKeyAddress, "https://game.example/item-id-8u5h2m.json");
    // console.log('nft-token-id:', nftTokenID);
    // console.log('nft-token-string:', parseInt(nftTokenID) );

    // // Get Owner Balance
    const ownerBalance = await box.balanceOf(pubKeyAddress)
    console.log('owner-balance:', ownerBalance.toString());

    const tokenID = 1
    const ownerAddress = await box.ownerOf(tokenID);
    console.log('owner-addr:', ownerAddress);

    const tokenMetaData = await box.tokenURI(tokenID);
    console.log('token-metadata:', tokenMetaData);

    callback(0);
    
  } catch (error) {
    console.error(error);
    callback(1);
  }


}


// TODO: 
  // get current-supply 
    // how to specify a max-supply?  (ie. 100 available only)
  // get current token-id
  // burn token
  // roles/permissions <-- how will smart-contract work for our web-app?
  

  // deploy this on main-net
    // interact with python

// 0x0c88659aed57fc4f079fcd3a9763873fea71d890c5694be914ecb1057ed5d012

// 0x90f8bf6a479f320ead074411a4b0e7944ea8c9c1
// 0xc89ce4735882c9f0f0fe26686c53074e09b0d550





